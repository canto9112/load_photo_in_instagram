import requests
from pathlib import Path
import os
from PIL import Image


def save_image(url, image_name, folder_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    path = Path.cwd() / folder_name / image_name
    content = response.content
    with open(path, 'wb') as file:
        file.write(content)


def get_file_extension(url):
    name, extension = os.path.splitext(url)
    return extension


def adjust_and_save_images(images_folder, upload_folder):
    filenames = os.listdir(path=images_folder)
    MAX_SIZE = 1080, 1080
    for filename in filenames:
        name, extension = os.path.splitext(filename)
        image = Image.open(f'{images_folder}/{filename}')
        image.thumbnail(MAX_SIZE)
        path = Path.cwd() / upload_folder / name
        if image.mode != 'RGB':
            ycbcr_image = image.convert('YCbCr')
            ycbcr_image.save(f'{path}.jpg', 'JPEG')
        else:
            image.save(f'{path}.jpg', 'JPEG')