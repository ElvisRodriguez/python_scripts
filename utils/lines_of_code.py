#!/home/elvisrodriguez1992/anaconda3/bin/python3
'''
Counts the total LOC in the current directory and it's sub directories
'''
import os

VALID_EXTENSIONS = ['.py', '.css', '.html', 'js', '.cpp', '.h', '.cc', '.java']


def find_all_valid_files(path, starting_path):
    '''Returns all files with extensions in VALID_EXTENSIONS'''
    os.chdir(path)
    valid_files = []
    for item in os.listdir(os.getcwd()):
        item_path = os.path.join(os.getcwd(), item)
        if os.path.isfile(item_path):
            extension = os.path.splitext(item_path)[1]
            if extension in VALID_EXTENSIONS:
                valid_files.append(item_path)
        if os.path.isdir(item_path):
            valid_files.extend(
                find_all_valid_files(
                    path=item_path, starting_path=starting_path
                )
            )
    os.chdir(starting_path)
    return valid_files


def count_lines_of_code(files):
    '''Count all file lines in files list'''
    lines_of_code = 0
    for file in files:
        with open(file, 'r') as f:
            lines_of_code += len(f.readlines())
    return lines_of_code


if __name__ == '__main__':
    path = os.getcwd()
    print('Finding all valid project files...')
    files = find_all_valid_files(path, starting_path=path)
    lines_of_code = count_lines_of_code(files)
    print('Total lines of code:', lines_of_code)
