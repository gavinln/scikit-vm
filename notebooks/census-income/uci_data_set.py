'''
Downloads data sets from https://archive.ics.uci.edu/ml/datasets.html
'''
import sys
import logging
from pathlib import Path
from urllib.parse import urljoin

from urllib.request import urlopen
from shutil import copyfileobj

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent.resolve()


def create_dir(path):
    ' creates path dir if does not exist '
    if not path.exists():
        path.mkdir()
    return path.exists()


def download_url_to_file(url_base, file_base, file_name):
    ' downloads file from url_base to directory file_base '
    url = urljoin(url_base, file_name)
    data_file = file_base / file_name

    log.info('download {} to {}'.format(url, data_file))
    with urlopen(url) as in_stream, open(data_file, 'wb') as out_file:
        copyfileobj(in_stream, out_file)


def main():
    url_base = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/'

    data_root = Path.home() / 'uci_data'
    if not create_dir(data_root):
        sys.exit('Cannot create directory {}'.format(data_root))

    data_adult = data_root / 'adult'
    if not create_dir(data_adult):
        sys.exit('Cannot create directory {}'.format(data_adult))

    train_data = 'adult.data'
    test_data = 'adult.test'
    names_data = 'adult.names'

    download_url_to_file(url_base, data_adult, train_data)
    download_url_to_file(url_base, data_adult, test_data)
    download_url_to_file(url_base, data_adult, names_data)


if __name__ == '__main__':
    main()
