from pathlib import Path
from PIL import Image
import os
from instabot import Bot
import time
import shutil


def adjust_and_save_images(images_folder, upload_folder):
    content = os.listdir(path=images_folder)
    for file in content:
        file_extansion = file[-4:]
        file_name = file.replace(file_extansion, '')
        image = Image.open(str(images_folder + f"/{file}"))
        image.thumbnail((1080, 1080))
        Path(upload_folder).mkdir(parents=True, exist_ok=True)
        path = Path.cwd() / upload_folder / file_name
        if image.mode != 'RGB':
            ycbcr_image = image.convert('YCbCr')
            ycbcr_image.save(f'{path}.jpg', 'JPEG')
        else:
            image.save(f'{path}.jpg', 'JPEG')


def delete_folder(folder):
    folder_path = Path(folder)
    shutil.rmtree(folder_path)


def upload_images(folder):
    password_inst = os.getenv('ISTAGRAM_PASSWORD')
    login_inst = os.getenv('INSTAGRAM_LOGIN')
    content = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file in content:
        bot.upload_photo(f'{folder}/{file}')
        time.sleep(60)


def start_uploading_images():
    images_folder = "images"
    instagram_images_folder = 'images_to_download'
    adjust_and_save_images(images_folder, instagram_images_folder)
    delete_folder(images_folder)
    upload_images(instagram_images_folder)
