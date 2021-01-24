from pathlib import Path
from PIL import Image
import os
from instabot import Bot
import time
import shutil


def adjust_and_save_images(images_folder, upload_folder):
    filepath = os.listdir(path=images_folder)
    for filename in filepath:
        name, extension = os.path.splitext(filename)
        image = Image.open(f'{images_folder}/{filename}')
        image.thumbnail((1080, 1080))
        Path(upload_folder).mkdir(parents=True, exist_ok=True)
        path = Path.cwd() / upload_folder / name
        if image.mode != 'RGB':
            ycbcr_image = image.convert('YCbCr')
            ycbcr_image.save(f'{path}.jpg', 'JPEG')
        else:
            image.save(f'{path}.jpg', 'JPEG')


def delete_folder(folder):
    folder_path = Path(folder)
    shutil.rmtree(folder_path)


def upload_images_instagram(folder):
    password_inst = os.getenv('ISTAGRAM_PASSWORD')
    login_inst = os.getenv('INSTAGRAM_LOGIN')
    filepath = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file_name in filepath:
        bot.upload_photo(f'{folder}/{file_name}')
        time.sleep(60)


def uploading_images(name_folder_save, name_folder_download):
    adjust_and_save_images(name_folder_save, name_folder_download)
    delete_folder(name_folder_save)
    upload_images_instagram(name_folder_download)
