import argparse
import collections
import os
from PIL import Image

VALID_IMAGE_EXTENSIONS = frozenset(
    ["bmp","gif","jpeg","jpg","png","ppm","tiff"])

def find_valid_images(images):
    """Filters out images that are not supported by PIL.Image objects.
    Args:
        images(list: str): absolute paths to image files.
    Returns:
        valid_images(list: str): absolute paths to image files supported by PIL.
    """
    valid_images = []
    for image in images:
        _, image_extension = image.split('.')
        if image_extension in VALID_IMAGE_EXTENSIONS:
            valid_images.append(image)
    return valid_images

def find_all_images(source_path, recursive=False):
    """Finds all images in given directory.
    Args:
        source_path(str): Absolute path to a directory containing images.
        recursive(bool): (optional)
        - True: Find all images within all directories using source_path as the root.
        - False: Find all images only within source_path, ignoring any sub directories.
    Returns:
        images(list: str): List of all images with valid extensions.
    """
    source_files = os.listdir(source_path)
    full_path_files = list(
        map(lambda file: os.path.join(source_path, file), source_files))
    if not recursive:
        full_path_files = [file for file in full_path_files if os.path.isfile(file)]
    all_images = []
    file_queue = collections.deque(full_path_files)
    while file_queue:
        file = file_queue.popleft()
        if os.path.isfile(file):
            all_images.append(file)
        else:
            directory_path = file
            directory_contents = os.listdir(directory_path)
            file_queue.extend(list(map(
                lambda file: os.path.join(directory_path, file), directory_contents)))
    valid_images = find_valid_images(all_images)
    return valid_images
    

def remove_exif_data(image_file_path):
    """Removes exif data from an image by creating a new PIL.Image object.
    Args:
        image_file_path: Path to image file.
    Retuns:
        None
    """
    print("Scrubbing {image}...".format(image=image_file_path))
    image = Image.open(image_file_path)
    image_data = list(image.getdata())
    clean_image = Image.new(image.mode, image.size)
    clean_image.putdata(image_data)
    clean_image.save(image_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrub EXIF data from all images in directory.")
    parser.add_argument("directory",
        type=str,
        help="Path to directory containing images that need their EXIF data scrubbed.")
    parser.add_argument('-r', "--recursive",
        action="store_true",
        default=False,
        required=False,
        help="Also scrub images in all sub directories within directory given")
    args = parser.parse_args()
    print("Finding all images...")
    images = find_all_images(args.directory, recursive=args.recursive)
    for image in images:
        remove_exif_data(image)
    print("Done!")
