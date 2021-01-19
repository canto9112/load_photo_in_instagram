import requests
from pathlib import Path


def create_folder_save_images(folder_name):
    Path(folder_name).mkdir(parents=True, exist_ok=True)


def save_image(url, image_name, folder_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    path = Path.cwd() / folder_name / image_name
    content = response.content
    with open(path, 'wb') as file:
        file.write(content)