"""Rebuild the pinned, locally patched NLTK wheel. Run from any directory."""
import base64
import csv
import hashlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '3.10.3+pathsec1'
UPSTREAM_SHA256 = 'ff9598a8e20518ee0d557745890cc4435b9578489e2dcbc69c4f81fa060caf7c'


def main():
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        subprocess.run([sys.executable, '-m', 'pip', 'download', '--no-deps',
                        '--only-binary=:all:', 'nltk==3.10.3', '-d', tmp], check=True)
        wheel = work / 'nltk-3.10.3-py3-none-any.whl'
        if hashlib.sha256(wheel.read_bytes()).hexdigest() != UPSTREAM_SHA256:
            raise RuntimeError('Unexpected upstream wheel checksum')
        source = work / 'source'
        with zipfile.ZipFile(wheel) as archive:
            archive.extractall(source)
        with (ROOT / 'vendor/nltk/model-pathsec.patch').open() as patch:
            subprocess.run(['patch', '-p1', '--batch', '--fuzz=0'], cwd=source,
                           stdin=patch, check=True)
        old_info = source / 'nltk-3.10.3.dist-info'
        info = source / f'nltk-{VERSION}.dist-info'
        old_info.rename(info)
        metadata = info / 'METADATA'
        metadata.write_text(metadata.read_text().replace(
            'Version: 3.10.3\n', f'Version: {VERSION}\n', 1))
        (source / 'nltk/VERSION').write_text(VERSION)
        (info / 'RECORD').unlink()
        entries = {}
        records = []
        for path in sorted(source.rglob('*')):
            if path.is_file():
                name = path.relative_to(source).as_posix()
                data = path.read_bytes()
                entries[name] = data
                digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b'=').decode()
                records.append([name, 'sha256=' + digest, str(len(data))])
        record_name = f'nltk-{VERSION}.dist-info/RECORD'
        records.append([record_name, '', ''])
        stream = io.StringIO(newline='')
        csv.writer(stream).writerows(records)
        entries[record_name] = stream.getvalue().encode()
        output = ROOT / f'vendor/nltk/nltk-{VERSION}-py3-none-any.whl'
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(entries.items()):
                entry = zipfile.ZipInfo(name, date_time=(2026, 9, 7, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                archive.writestr(entry, data)
        print(output)
        print('SHA256:', hashlib.sha256(output.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
