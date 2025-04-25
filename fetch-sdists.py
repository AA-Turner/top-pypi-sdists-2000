# /// script
# dependencies = [
#     "urllib3>=2",
# ]
# ///

import concurrent.futures
import time
import traceback
from pathlib import Path

import urllib3

PACKAGES_URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages.min.json'

ROOT = Path(__file__).resolve().parent
SDIST_ROOT = ROOT / 'pypi-sdists'
SDIST_ROOT.mkdir(exist_ok=True)

http = urllib3.PoolManager()


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
        urls = http.request('GET', f'https://pypi.org/pypi/{proj}/json').json()['urls']
        for entry in urls:
            if entry['packagetype'] == 'sdist':
                url = entry['url']
                break
        else:
            print(f'No source distribution for {proj!r}')
            return None
        del urls
        response = http.request('GET', url)
        filename = url.rpartition('/')[2]
        print(f'{index:6,}: Writing {filename} for {proj!r}')
        SDIST_ROOT.joinpath(filename).write_bytes(response.data)
        del response
        return filename
    except Exception:
        print(f'Fetching {proj!r} failed')
        traceback.print_exc()


if __name__ == '__main__':
    raise SystemExit(main())
