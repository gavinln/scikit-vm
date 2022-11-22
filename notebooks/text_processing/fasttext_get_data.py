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
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, path=data_dir)


if __name__ == '__main__':
    main()
