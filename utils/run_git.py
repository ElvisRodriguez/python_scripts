import os
import sys


HOME_DIRECTORY = os.getcwd()
LINE_BREAK_SIZE = 100


def find_git_directories():
    directories = []
    os.chdir(HOME_DIRECTORY)
    for directory in os.listdir():
        if os.path.isdir(directory) and '.config' not in directory:
            directory_path = os.path.join(HOME_DIRECTORY, directory)
            if '.git' in os.listdir(directory_path):
                directories.append(directory)
    return directories


def find_git_status(directories):
    for directory in directories:
        print('In Directory:', directory)
        path = os.path.join(HOME_DIRECTORY, directory)
        os.chdir(path)
        os.system('git status')
        print('*{symbol}*'.format(symbol='*' * LINE_BREAK_SIZE))


if __name__ == '__main__':
    directories = find_git_directories()
    find_git_status(directories)
