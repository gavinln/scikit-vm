'''
Get data for fasttext example

'''
import pathlib
import logging

import tarfile
import urllib.request
import gzip
import sys

from IPython import embed


SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__file__)


# def extract_file(gz_file, dest_dir):
#     if not dest_dir.exists():
#         sys.exit('{} does not exist'.format(dest_dir))
#     if not dest_dir.is_dir():
#         sys.exit('{} is not a directory'.format(dest_dir))
#     if not gz_file.exists():
#         sys.exit('{} does not exist'.format(gz_file))
#     if not gz_file.is_file():
#         sys.exit('{} is not a file'.format(gz_file))
#     with gzip.open(str(gz_file), 'rb') as f:
#         new_file = dest_dir / gz_file.with_suffix('').name
#         new_file.write_bytes(f.read())
#     return new_file


def main():
    '''
wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/cooking.stackexchange.tar.gz
tar xvzf cooking.stackexchange.tar.gz
    '''

    data_dir = SCRIPT_DIR / 'fasttext_data'
    text_file_name = 'cooking.stackexchange.tar.gz'
    file_url = 'https://s3-us-west-1.amazonaws.com/fasttext-vectors/{}'.format(
            text_file_name)

    if not data_dir.exists():
        sys.exit('directory {} does not exist'.format(data_dir))

    text_file = data_dir / text_file_name
    local_filename, headers = urllib.request.urlretrieve(
        file_url, filename=text_file)
    print(local_filename)

    with tarfile.open(local_filename, "r|gz") as tar:
        tar.extractall(path=data_dir)

    # embed()


if __name__ == '__main__':
    main()
