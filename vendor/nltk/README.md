# Local NLTK model-path security patch

This project installs `nltk 3.10.3+pathsec1` from the adjacent wheel via
`requirements.txt`. This is a project-maintained patch, not an official NLTK
release. It addresses the model-artifact bypass described in
[GHSA-8mgp-746c-j5xp](https://github.com/nltk/nltk/security/advisories/GHSA-8mgp-746c-j5xp)
(Dependabot alert #13). The advisory listed no patched release when checked on
2026-09-07. Do not dismiss the alert merely because this local artifact is used;
GitHub may continue to flag the underlying version or may not resolve local
wheel dependencies.

## Installation

From the repository root, with your virtual environment active:

```sh
python -m pip install -r requirements.txt
python -m pytest
```

The existing GitHub Actions install step uses this same requirements file.
Keep the wheel, patch, build script and tests together in version control.
The local `.venv2` has not been modified by patch preparation.

NLTK tokenizer/tagger data remains a separate installation:

```sh
python -m nltk.downloader punkt_tab averaged_perceptron_tagger_eng
```

## Changes

`model-pathsec.patch` changes NLTK source, not application bibliography reads:

- `TransitionParser.train` validates the model destination before training and
  writes through a context-managed `pathsec.open`; `parse` reads through it,
  retaining the existing allowlisting unpickler.
- `AveragedPerceptron.save` and `load` use `pathsec.open`.
- `PerceptronTagger.save_to_json` validates the destination before creating a
  directory, retains the POSIX private-directory check, and uses full-path
  `pathsec.open` with a required model root for every output. It no longer
  automatically authorizes a caller-selected save directory. The centralized
  pathsec opener now performs the file-opening checks instead of the former
  per-method descriptor-relative opener.
- `save_maxent_params` validates the directory before creating it and uses
  `pathsec.open` for all four output files, scoped to that directory.

These changes enforce NLTK's configured path policy. They do not make pathsec a
complete operating-system sandbox, change its allowed-root defaults, or repair
other NLTK vulnerabilities. Users saving models to custom locations must
explicitly authorize those locations through NLTK's data-path configuration.
Do not disable enforcement to accommodate untrusted paths.

## Rebuild and provenance

Run with Python, pip, and the system `patch` command available:

```sh
python tools/build_nltk_wheel.py
```

The script downloads the official 3.10.3 wheel, verifies its SHA-256, applies the
source patch without fuzzy matching, sets a local version, and regenerates the
wheel metadata and RECORD hashes. ZIP timestamps and entry ordering are fixed.
All upstream license files remain in the wheel.

Upstream wheel SHA-256:
`ff9598a8e20518ee0d557745890cc4435b9578489e2dcbc69c4f81fa060caf7c`

Patched wheel SHA-256:
`2cfa2f4d898d368cf9fa1f00078b9ec9eb3f7a33de81571b21bfd8fc2fcb301d`

## Validation

`tests/test_nltk_model_pathsec.py` covers each of the six affected APIs with a
same-path, same-mode `pathsec.open` negative control. Cases include absolute
outside-root paths, `..` traversal and directory symlink escapes. Outside files
must remain unchanged. Separate cases confirm rejected save destinations do not
create directories, and allowed destinations still work, including tagger and
maxent save/load round trips.

The test fixture restricts allowed roots explicitly because NLTK normally permits
system temporary paths. Transition-parser statistical training is stubbed to
exercise persistence without requiring scikit-learn; this is not an end-to-end
parser accuracy test. Tokenization and POS tagging were also smoke-tested using
existing local NLTK data.

Verified on macOS with Python 3.12.14 (the CI Python version) and Python 3.14:
46 total tests passed, including 26 security tests; blocking Flake8 check passed.
Against unpatched NLTK 3.10.3, the security suite produced 19 failures and 7 passes,
confirming the tests detect the bypasses rather than merely testing the policy
helper. Linux/Windows results must be confirmed by CI or those platforms.

Replace this wheel with an official fixed release once available and verified
against these tests. Retain the regression tests when removing the local patch.

## AI assistance

This local patch, rebuild script, regression tests and documentation were
prepared with assistance from OpenAI Codex on 2026-09-07.
References: [ChatGPT](https://chatgpt.com/) and
[OpenAI Codex](https://openai.com/codex/).
