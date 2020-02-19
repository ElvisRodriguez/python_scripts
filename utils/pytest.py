import os
import sys


SCRIPT_TEMPLATE = '''
import os
import random
import sys
import unittest

import {filename}


class Test{filename}(unittest.TestCase):
    def setUp(self):
        self.{filename_object} = {filename}.{filename}()


if __name__ == '__main__':
    unittest.main()
'''


def camelcase_to_snakecase(string):
    new_string = []
    for char in string:
        if char.isupper() and len(new_string) > 0:
            new_string.append('_')
        new_string.append(char)
    return ''.join(new_string).lower()


def create_test_file(filename, template=SCRIPT_TEMPLATE):
    test_file = '{filename}_test.py'.format(filename=filename)
    os.chdir(os.getcwd())
    with open(test_file, 'w') as new_file:
        filename_object = camelcase_to_snakecase(filename)
        template = template.format(
            filename=filename, filename_object=filename_object
        )
        new_file.write(template)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_test_file(sys.argv[1])
    else:
        print('Python test filename not given')
