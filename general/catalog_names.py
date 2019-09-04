'''
Script to sort a stream of names and populate them into a txt file
'''

import os


class NameSorter:
    def __init__(self, filename='roster.txt'):
        self.names = []
        self.filename = filename

    def collect_names(self):
        name = ''
        print('Enter names, enter \'end\' when finished.')
        while name != 'end':
            name = str(input('Name: '))
            self.names.append(name)
        self.names.pop(-1)

    def populate_file(self):
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, self.filename)
        self.names = sorted(self.names)
        with open(full_path, 'w') as file:
            for name in self.names:
                file.write(name + '\n')
        print('Done')


if __name__ == '__main__':
    name_sorter = NameSorter()
    name_sorter.collect_names()
    name_sorter.populate_file()
