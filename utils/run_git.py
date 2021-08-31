import os


HOME_DIRECTORY = os.path.expanduser("~")

def find_git_repositories():
    """Crawls through every directory in HOME_DIRECTORY to find git repos
    Args:
    - None
    Returns:
    - respositories: list[str] absolute paths to every git repo found
    """
    repositories = []
    os.chdir(HOME_DIRECTORY)
    for file in os.listdir():
        if os.path.isdir(file):
            directory = os.path.join(HOME_DIRECTORY, file)
            if ".git" in os.listdir(directory):
                repositories.append(directory)
    return repositories


def find_git_status(repositories):
    """Checks git status of every repo found and pretty prints the result
    Args:
    - repositories: list[str] absolute paths to every git repo found
    Returns:
    - None
    """
    line_break_size = int(os.popen("tput cols").read())
    for repository in repositories:
        print("In Repository:", repository)
        path = os.path.join(HOME_DIRECTORY, repository)
        os.chdir(path)
        os.system("git status")
        print("{symbol}".format(symbol="*" * line_break_size))


if __name__ == "__main__":
    repositories = find_git_repositories()
    find_git_status(repositories)
