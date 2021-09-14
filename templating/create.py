import argparse
import os
import sys

TEMPLATES = {
    "class": "class_module.txt",
    "test": "test_module.txt"
}

def get_script_directory():
    """Grabs this script's directory path.
    Args:
        None.
    Returns:
        directory_path(str): absolute path to this script excluding script filename.
    """
    file_path = os.path.realpath(__file__)
    path_components = file_path.split('/')
    path_components.pop(-1)
    directory_path = '/'.join(path_components)
    return directory_path

def create_new_file(filename, template):
    """Creates a python module based off available templates.
    Args:
        filename(str): Filename of module being created.
        template(str): Filename of template type.
    Returns:
        None.
    """
    destination_path = os.getcwd()
    os.chdir(get_script_directory())
    with open(template, 'r') as template_file:
        raw_text = ''.join(template_file.readlines())
    script = '{filename}.py'.format(filename=filename)
    os.chdir(destination_path)
    with open(script, 'w') as new_script:
        if filename[0].islower():
            filename = filename.title()
        formatted_text = raw_text.format(filename=filename)
        new_script.write(formatted_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generates templated python files.")
    parser.add_argument("filename",
        type=str,
        help="Name of python file to be generated.")
    parser.add_argument("template",
        type=str,
        help="Type of template to generate. Can be one of {}".format(','.join(TEMPLATES.keys())))
    args = parser.parse_args()
    filename = args.filename
    template = args.template
    template = template.lower()
    if template not in TEMPLATES:
        print("template not found, available templates:")
        print(','.join(TEMPLATES.keys()))
        sys.exit()
    if template == "test":
        filename = "{}_test".format(filename)
    create_new_file(filename, TEMPLATES[template])