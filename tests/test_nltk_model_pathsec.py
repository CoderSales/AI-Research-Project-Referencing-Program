"""Regression coverage for GHSA-8mgp-746c-j5xp (model path containment)."""
import json
import pickle
from types import SimpleNamespace
from unittest.mock import MagicMock

import numpy as np
import pytest
from nltk import pathsec
from nltk.data import FileSystemPathPointer
from nltk.classify.maxent import load_maxent_params, save_maxent_params
from nltk.parse import transitionparser as transition
from nltk.tag.perceptron import AveragedPerceptron, PerceptronTagger


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    allowed = tmp_path / 'allowed'
    outside = tmp_path / 'outside'
    allowed.mkdir()
    outside.mkdir()
    monkeypatch.setattr(pathsec, 'ENFORCE', True)
    # NLTK normally permits temp directories; isolate policy for these tests.
    monkeypatch.setattr(pathsec, '_get_allowed_roots', lambda: {allowed.resolve()})
    return allowed, outside


def invoke(api, path, monkeypatch):
    if api == 'averaged_save':
        model = AveragedPerceptron()
        model.weights = {'bias': {'NN': 1.0}}
        model.save(path)
    elif api == 'averaged_load':
        model = AveragedPerceptron()
        model.load(path)
        return model.weights
    elif api == 'tagger_save':
        PerceptronTagger(load=False).save_to_json(lang='eng', loc=str(path.parent))
    elif api == 'maxent_save':
        save_maxent_params(np.array([1.0]), {('f', 'v', 'NN'): 0},
                           ['NN'], {'NN': 0}, str(path.parent))
    else:
        parser = transition.TransitionParser('arc-standard')
        if api == 'transition_parse':
            return parser.parse([], str(path))
        # Isolate model persistence from expensive statistical training.
        monkeypatch.setattr(parser, '_create_training_examples_arc_std', lambda *args: None)
        monkeypatch.setattr(transition, 'load_svmlight_file',
                            lambda *args: (MagicMock(), []), raising=False)
        monkeypatch.setattr(transition, 'svm',
                            SimpleNamespace(SVC=lambda **kwargs: MagicMock()), raising=False)
        monkeypatch.setattr(transition.pickle, 'dump', lambda model, stream: stream.write(b'model'))
        parser.train([], str(path), verbose=False)


CASES = [
    ('averaged_save', 'weights.json', 'w'),
    ('averaged_load', 'weights.json', 'r'),
    ('transition_train', 'parser.pickle', 'wb'),
    ('transition_parse', 'parser.pickle', 'rb'),
    ('tagger_save', 'averaged_perceptron_tagger_eng.weights.json', 'w'),
    ('maxent_save', 'weights.txt', 'w'),
]


@pytest.mark.parametrize('api,filename,mode', CASES)
@pytest.mark.parametrize('escape', ['absolute', 'traversal', 'symlink'])
def test_outside_path_matches_negative_control(sandbox, monkeypatch, api, filename, mode, escape):
    allowed, outside = sandbox
    target = outside / filename
    original = pickle.dumps({}) if api == 'transition_parse' else b'{"bias": {"NN": 1.0}}'
    target.write_bytes(original)
    if escape == 'absolute':
        attempted = target
    elif escape == 'traversal':
        attempted = allowed / '..' / 'outside' / filename
    else:
        link = allowed / 'link'
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            pytest.skip('Symlink creation unavailable')
        attempted = link / filename
    before = {p.name: p.read_bytes() for p in outside.iterdir()}
    # Same path and I/O direction: the guarded control must reject it first.
    with pytest.raises(PermissionError):
        with pathsec.open(attempted, mode):
            pytest.fail('Control unexpectedly opened outside path')
    with pytest.raises(PermissionError):
        invoke(api, attempted, monkeypatch)
    assert {p.name: p.read_bytes() for p in outside.iterdir()} == before


@pytest.mark.parametrize('api,filename,mode', CASES)
def test_allowed_path_still_works(sandbox, monkeypatch, api, filename, mode):
    allowed, _ = sandbox
    target = allowed / filename
    if api == 'averaged_load':
        target.write_text('{"bias": {"NN": 1.0}}')
    elif api == 'transition_parse':
        target.write_bytes(pickle.dumps({}))
    result = invoke(api, target, monkeypatch)
    with pathsec.open(target, 'rb') as stream:
        assert stream.read()
    if api == 'averaged_load':
        assert result == {'bias': {'NN': 1.0}}
    elif api == 'averaged_save':
        assert json.loads(target.read_text()) == {'bias': {'NN': 1.0}}
    elif api == 'transition_parse':
        assert result == []
    elif api == 'tagger_save':
        tagger = PerceptronTagger(load=False)
        tagger.load_from_json(lang='eng', loc=str(allowed))
        assert tagger.model.weights == {}
    elif api == 'maxent_save':
        weights, mapping, labels, alwayson = load_maxent_params(FileSystemPathPointer(str(allowed)))
        assert weights.tolist() == [1.0]
        assert mapping == {('f', 'v', 'NN'): 0}
        assert labels == ['NN']
        assert alwayson == {'NN': 0}


@pytest.mark.parametrize('api,filename', [('tagger_save', CASES[4][1]), ('maxent_save', 'weights.txt')])
def test_denied_directory_is_not_created(sandbox, monkeypatch, api, filename):
    _, outside = sandbox
    parent = outside / 'new-model'
    with pytest.raises(PermissionError):
        with pathsec.open(parent / filename, 'w'):
            pass
    with pytest.raises(PermissionError):
        invoke(api, parent / filename, monkeypatch)
    assert not parent.exists()
