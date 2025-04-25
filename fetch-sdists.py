# /// script
# dependencies = [
#     "urllib3>=2",
# ]
# ///

import concurrent.futures
import shutil
import tarfile
import time
import traceback
import zipfile
from io import BytesIO
from pathlib import Path

import urllib3

PACKAGES_URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages.min.json'

ROOT = Path(__file__).resolve().parent
SDIST_ROOT = ROOT / 'pypi-sdists'
SDIST_ROOT.mkdir(exist_ok=True)
EXTRACTED_ROOT = ROOT / 'extracted'
EXTRACTED_ROOT.mkdir(exist_ok=True)

http = urllib3.PoolManager()

# Only keep interesting source files
FILE_EXTENSIONS = frozenset({
    '.c', '.h',
    '.cc', '.hh',
    '.c++', '.cpp', '.cxx', '.h++', '.hpp', '.ipp',
    '.cs',
    '.f', '.f90', '.f95',
    '.go',
    '.java',
    '.pl',
    '.php',
    '.py', '.pyi', '.pyw', '.pyx', '.pxd',
    '.rb',
    '.rs',
    '.s',
    '.zig',
})  # fmt: skip
METADATA_FILES = frozenset({
    'PKG-INFO',
    'pyproject.toml',
})
DIRECTORY_BLACKLIST = frozenset({
    # SCM directories
    '.git', '.hg', '.jj', '.svn',
    # Virtual environments
    'venv', '.venv', '.eggs',
    # Project-related directories
    '.tox', '.nox',
    '.idea', '.vs', '.vscode',
    # Non-project directories
    'deps', 'extern', 'external', 'externals', 'external_libs',
    'pybind', 'pybind11',
    'third_party',
    '_vendor', 'vendor', 'vendored', 'vendored-meson',
})  # fmt: skip


def main() -> int:
    start = time.perf_counter()

    rows = http.request('GET', PACKAGES_URL).json()['rows'][:1_500]
    project_names = [row['project'] for row in rows]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(process_project, index, proj)
            for index, proj in enumerate(project_names, start=1)
        }
        sdists = {fut.result() for fut in concurrent.futures.as_completed(futures)}
    sdists.discard(None)

    dt = time.perf_counter() - start
    print(f'Processed {len(sdists)} sdists ({dt:.3f}s)')
    return 0


def process_project(index, proj):
    try:
        if (url := sdist_url(http, proj)) is None:
            return None
        filename = url.rpartition('/')[2]
        archive_data = http.request('GET', url).data
        print(f'{index:6,}: Downloaded {filename} for {proj!r}')
        extract_archive(filename, archive_data, proj)
        return filename
    except Exception:
        print(f'Fetching {proj!r} failed')
        traceback.print_exc()


def sdist_url(http: urllib3.PoolManager, project_name: str) -> str | None:
    data = http.request('GET', f'https://pypi.org/pypi/{project_name}/json').json()
    for entry in data['urls']:
        if entry['packagetype'] == 'sdist':
            return entry['url']
    print(f'No source distribution for {project_name!r}')
    return None


def extract_archive(filename: str, content: bytes, project_name: str):
    print(f'Extracting {filename!r}')
    stream = BytesIO(content)
    if filename.endswith(('.tar.gz', '.tgz')):
        return extract_archive_tar_gzip(filename, stream, project_name)
    if filename.endswith('.tar.bz2'):
        return extract_archive_tar_bzip2(filename, stream, project_name)
    if filename.endswith('.zip'):
        return extract_archive_zip(filename, stream, project_name)
    return None


def extract_archive_tar_gzip(filename: str, stream: BytesIO, project_name: str):
    with tarfile.TarFile.gzopen(filename, mode='r', fileobj=stream) as tar:
        return extract_archive_tar(tar, project_name)


def extract_archive_tar_bzip2(filename: str, stream: BytesIO, project_name: str):
    with tarfile.TarFile.bz2open(filename, mode='r', fileobj=stream) as tar:
        return extract_archive_tar(tar, project_name)


def extract_archive_tar(tar: tarfile.TarFile, /, project_name: str):
    while (member := tar.next()) is not None:
        if not member.isfile():
            continue

        path = Path(member.name)
        if not keep_file(path):
            continue

        if (size_mb := member.size / 1000 / 1000) > 5:
            print(f'Skipping {path} (too large: {size_mb:.2f}MB)')
            continue

        parts_rm_first = valid_cross_platform_path(path).parts[1:]
        dest_path = EXTRACTED_ROOT.joinpath(project_name, *parts_rm_first)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            tar.makefile(member, dest_path)
        except OSError:
            print(f'Failed to extract {path!r} to {dest_path!r}!')


def extract_archive_zip(filename: str, stream: BytesIO, project_name: str):
    zip = zipfile.ZipFile(stream)
    zip.filename = filename
    with zip:
        for member in zip.filelist:
            if member.is_dir():
                continue
            path = Path(member.filename)
            if not keep_file(path):
                continue

            # Remove large files
            if (size_mb := member.file_size / 1000 / 1000) > 5:
                print(f'Skipping {path} (too large: {size_mb:.2f}MB)')
                continue

            # Remove version from archive filename
            parts_rm_first = valid_cross_platform_path(path).parts[1:]
            dest_path = EXTRACTED_ROOT.joinpath(project_name, *parts_rm_first)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with zip.open(member) as source, open(dest_path, 'wb') as target:
                    shutil.copyfileobj(source, target)

            except OSError:
                print(f'Failed to extract {path!r} to {dest_path!r}!')


def keep_file(path: Path) -> bool:
    if any(part.lower() in DIRECTORY_BLACKLIST for part in path.parts):
        return False
    if path.name in METADATA_FILES:
        return True
    if path.suffix.lower() in FILE_EXTENSIONS:
        return True
    return False


PATH_RESERVED = dict.fromkeys((*range(0x20), *rb'?<>\:*|"'), '_')


def valid_cross_platform_path(path: Path, /) -> Path:
    # Make filenames valid for Windows
    if path.name.endswith((' ', '.')):
        return path.with_name(f'{path}_')
    return Path(*(p.translate(PATH_RESERVED) for p in path.parts))


if __name__ == '__main__':
    raise SystemExit(main())
