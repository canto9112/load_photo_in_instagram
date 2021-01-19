from pathlib import Path
from PIL import Image
import os
from instabot import Bot
import time
import shutil


def adjust_and_save_images(folder_images, folder_upload):
    content = os.listdir(path=folder_images)
    for file in content:
        file_extansion = file[-4:]
        file_name = file.replace(file_extansion, '')
        image = Image.open(str(folder_images + f"/{file}"))
        image.thumbnail((1080, 1080))
        Path(folder_upload).mkdir(parents=True, exist_ok=True)
        path = Path.cwd() / folder_upload / file_name
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
    folder_contents = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file in folder_contents:
        bot.upload_photo(f'{folder}/{file}')
        time.sleep(60)


def start_uploading_images():
    folder_images = "images"
    folder_uploading_instagram = 'images_to_download'
    adjust_and_save_images(folder_images, folder_uploading_instagram)
    delete_folder(folder_images)
    upload_images(folder_uploading_instagram)
