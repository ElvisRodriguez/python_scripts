import os
import sys


SCRIPT_TEMPLATE = '''#Write a description of this class using a docstring.
import os
import sys


class {filename}(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    print(sys.argv[0])
'''


def create_new_file(filename, template=SCRIPT_TEMPLATE):
    script = '{filename}.py'.format(filename=filename)
    os.chdir(os.getcwd())
    with open(script, 'w') as new_file:
        if filename[0].islower():
            filename = filename.title()
        template = template.format(filename=filename)
        new_file.write(template)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_new_file(sys.argv[1])
    else:
        print('Python filename not given')
