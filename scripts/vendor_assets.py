"""Bundle pinned renderer assets so readers do not need a third-party CDN."""
import io
import tarfile
import urllib.request
from pathlib import Path
root = Path(__file__).resolve().parents[1] / 'docs' / '_static' / 'vendor'
for package, version, subtree in [('mermaid', '11.12.2', 'dist'), ('mathjax', '3.2.2', 'es5')]:
    url = f'https://registry.npmjs.org/{package}/-/{package}-{version}.tgz'
    data = urllib.request.urlopen(url, timeout=120).read()
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        count = 0
        for member in archive.getmembers():
            if not member.isfile():
                continue
            relative = Path(member.name).relative_to('package')
            if '..' in relative.parts:
                raise ValueError('Invalid package path')
            keep = str(relative).startswith(subtree + '/') or relative.name.startswith(('LICENSE', 'COPYRIGHT'))
            if not keep or relative.suffix in ('.map', '.ts'):
                continue
            if package == 'mermaid' and relative.suffix not in ('.mjs', '') and not relative.name.startswith('LICENSE'):
                continue
            dest = root / package / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(archive.extractfile(member).read())
            count += 1
    print(f'{package}@{version}: {count} files from {url}')
