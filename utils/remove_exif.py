import os
from PIL import Image

VALID_IMAGE_EXTENSIONS = frozenset(
        ["bmp","gif","jpeg","jpg","png","ppm","tiff"]
        )

def remove_exif_data(image_file_path):
    """Removes exif data from an image by creating a new PIL.Image object.
    Args:
        image_file_path: File path to image.
    Retuns:
        None
    """
    _, image_extension = image_file_path.split('.')
    if image_extension in VALID_IMAGE_EXTENSIONS:
        image = Image.open(image_file_path)
        image_data = list(image.getdata())
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(image_data)
        clean_image.save(image_file_path)
    else:
        print("{} is not a supported file".format(image_file_path))


if __name__ == "__main__":
    pass
