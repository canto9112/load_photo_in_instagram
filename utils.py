import requests
from pathlib import Path
import os


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