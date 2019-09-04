import os
import pkg_resources
import sys


PATH = '/home/elvisrodriguez1992/py_scripts/general'


def get_package_names():
    packages = pkg_resources.working_set
    package_names = []
    for package in packages:
        package_names.append(package.project_name)
    return package_names


def write_package_names_to_file(package_names):
    os.chdir(PATH)
    file_path = os.path.join(PATH, 'pip_packages.txt')
    with open(file_path, 'w') as file:
        for name in package_names:
            file.write('{name}\n'.format(name=name))


def get_package_names_from_file():
    package_names = []
    os.chdir(PATH)
    file_path = os.path.join(PATH, 'pip_packages.txt')
    with open('pip_packages.txt', 'r') as file:
        for line in file.readlines():
            name = line.strip('\n')
            package_names.append(name)
    return package_names


def reinstall_packages(package_names):
    for name in package_names:
        os.system('pip install --user {module}'.format(module=name))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode in ['backup', 'restore']:
            if mode == 'backup':
                print('Backing up your pip packages...')
                package_names = get_package_names()
                write_package_names_to_file(package_names)
                print('Done.')
            if mode == 'restore':
                print('Reinstalling your pip packages...')
                package_names = get_package_names_from_file()
                reinstall_packages(package_names)
                print('Done')
        else:
            print('Only backup and restore modes are supported.')
    else:
        print('Must enter a mode: backup or restore')
