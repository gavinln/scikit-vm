'''
Get data for fasttext example

'''
import pathlib

import tarfile
import urllib.request
import sys


SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()


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


if __name__ == '__main__':
    main()
