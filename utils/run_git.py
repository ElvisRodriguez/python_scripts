import collections
import datetime
import json
import os
from pathlib import Path

HOME_DIRECTORY = os.path.expanduser("~")
SCRIPT_DIRECTORY = Path(os.path.realpath(__file__)).parent.absolute()
CACHE_FILE = os.path.join(SCRIPT_DIRECTORY, "cache.json")

def load_cache():
    """Opens and converts cache.json into a dict.
    Args:
    - None
    Returns:
    - cache(dict): JSON object used to keep track of git repos in HOME_DIRECTORY.
    """
    with open(CACHE_FILE, 'r') as file:
        cache = json.load(file)
    return cache

def is_cache_outdated(cache):
    """Checks if cache.json has been updated today.
    Args:
    - cache(dict): JSON object used to keep track of git repos in HOME_DIRECTORY.
    Returns:
    - (bool): A flag checking if cache.json's last write date is today's date.
    """
    current_datetime = datetime.datetime.today()
    current_date = str(datetime.datetime.date(current_datetime))
    return cache["current-date"] != current_date

def update_cache(cache, repositories):
    """Checks if cache.json has been updated today.
    Args:
    - cache(dict): JSON object used to keep track of git repos in HOME_DIRECTORY.
    - respositories(list: str): absolute paths to every git repo in HOME_DIRECTORY.
    Returns:
    - None
    """
    current_datetime = datetime.datetime.today()
    current_date = str(datetime.datetime.date(current_datetime))
    cache["current-date"] = current_date
    cache["git-repos"] = repositories
    with open(CACHE_FILE, 'w') as file:
        json.dump(cache, file, indent=4)

def find_git_repositories():
    """Recursively crawls through every directory in HOME_DIRECTORY to find git repos.
    Args:
    - None
    Returns:
    - respositories(list:str): absolute paths to every git repo found
    """
    repositories = []
    os.chdir(HOME_DIRECTORY)
    files = [os.path.join(HOME_DIRECTORY, file) for file in os.listdir()]
    file_queue = collections.deque(files)
    while file_queue:
        file = file_queue.popleft()
        if os.path.isdir(file):
            directory_contents = os.listdir(file)
            if ".git" in directory_contents:
                repositories.append(file)
            else:
                full_path_directory_contents = [
                    os.path.join(file, directory) for directory in directory_contents]
                only_directories = [
                    directory for directory in full_path_directory_contents if os.path.isdir(directory)]
                file_queue.extend(only_directories)
    return repositories


def find_git_status(repositories):
    """Checks git status of every repo found and pretty prints the result
    Args:
    - repositories(list:str): absolute paths to every git repo found
    Returns:
    - None
    """
    line_break_size = int(os.popen("tput cols").read())
    print("Checking status of all repos...")
    for repository in repositories:
        print("In Repository:", repository)
        os.chdir(repository)
        os.system("git status")
        print("{symbol}".format(symbol="*" * line_break_size))


if __name__ == "__main__":
    cache = load_cache()
    if is_cache_outdated(cache):
        print("Cache out of date, crawling directory tree for git repos...")
        repositories = find_git_repositories()
        update_cache(cache, repositories)
    else:
        repositories = cache["git-repos"]
    find_git_status(repositories)
