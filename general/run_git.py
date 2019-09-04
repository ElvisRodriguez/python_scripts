import os
import sys


HOME_DIRECTORY = '/home/elvisrodriguez1992'


def find_git_directories():
    directories = []
    os.chdir(HOME_DIRECTORY)
    for directory in os.listdir():
        if os.path.isdir(directory):
            directory_path = os.path.join(HOME_DIRECTORY, directory)
            if '.git' in os.listdir(directory_path):
                directories.append(directory)
    return directories


def find_git_status(directories, push=False):
    for directory in directories:
        print('In Directory:', directory)
        path = os.path.join(HOME_DIRECTORY, directory)
        os.chdir(path)
        os.system('git status')
        print('*{symbol}*'.format(symbol='*' * 50))
        if push:
            username = sys.argv[2]
            password = sys.argv[3]
            os.system('git add .')
            os.system('git commit -m "git automatically pushed by daemon"')
            push_command = 'git push https://{username}:{password}@{directory}.biz/file.git --all'
            push_command = push_command.format(username=username, password=password, directory=directory)
            os.system(push_command)


if __name__ == '__main__':
    directories = find_git_directories()
    try:
        push = sys.argv[1]
        push = True
    except IndexError:
        push = False
    find_git_status(directories, push)
