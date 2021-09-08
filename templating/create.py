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
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        template = sys.argv[2].lower()
        if template not in TEMPLATES:
            print("template not found, available templates:")
            print(",".join(TEMPLATES.keys()))
            sys.exit()
        if template == "test":
            filename = "{}_test".format(filename)
        create_new_file(sys.argv[1], template=TEMPLATES[template])
    elif len(sys.argv) == 2:
        print("Must provide a template type, available templates:")
        print(",".join(TEMPLATES.keys()))
    else:
        print("filename and template must be provided, available templates:")
        print(",".join(TEMPLATES.keys()))