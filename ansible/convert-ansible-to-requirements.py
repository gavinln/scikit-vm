'''
Converts an Ansible Python playbook file to a requirements.txt file
This requirements.txt file can be used with pipenv to create a Pipfile

pipenv install -r requirements.txt
'''
import logging
import pathlib
import yaml


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()


def get_library_name(lib_options):
    ''' returns library name given lib_options

        lib_options is of a format "name=pandas state=present"
    '''
    options = lib_options.split()
    name_prefix = 'name='
    for option in options:
        if option.startswith(name_prefix):
            if len(option) > len(name_prefix):
                return option[len(name_prefix):]
    return None


def get_pip_libs(pip_item):
    lib_names = []
    if isinstance(pip_item, dict) and 'pip' in pip_item:
        for key, val in pip_item.items():
            if key == 'pip':
                lib_name = get_library_name(val)
                if lib_name:
                    lib_names.append(lib_name)
    return lib_names


def display_yaml_file(file_name):
    with file_name.open() as stream:
        try:
            pip_libs = []
            for item in yaml.safe_load(stream):
                new_pip_libs = get_pip_libs(item)
                if len(new_pip_libs) > 0:
                    pip_libs.extend(new_pip_libs)

            if len(pip_libs) > 0:
                print('## {}'.format(file_name))
                print('\n'.join(pip_libs))
        except yaml.YAMLError as exc:
            print(exc)


def main():
    yaml_dir = SCRIPT_DIR
    files = yaml_dir.glob('*.yml')
    for file_name in files:
        # print(file_name.resolve())
        display_yaml_file(file_name)


if __name__ == "__main__":
    main()
