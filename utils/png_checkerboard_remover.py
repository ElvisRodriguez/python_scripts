import os
import sys

from rembg import remove
from PIL import Image


def remove_checker_background(file_path):
    """Removes the white and gray checkerboard background in a .png.
    Args:
        file_path(str): Path to the image.
    Returns:
        None
    """
    name, extension = os.path.splitext(file_path)
    new_file_path = f"{name}_transparent{extension}"
    input_image = Image.open(file_path)
    output_image = remove(input_image)
    output_image.save(new_file_path)
    print(f"{file_path} had it's background removed! Saved in {new_file_path}")


if __name__ == "__main__":
    file_path = sys.argv[1]
    if ".png" not in file_path:
        print("Argument is not a .png file")
        sys.exit()
    remove_checker_background(file_path)