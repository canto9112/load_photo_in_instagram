from pathlib import Path
from PIL import Image
import os
from dotenv import load_dotenv
from instabot import Bot
import time
import shutil


def adjust_and_save_image(name_folder, upload_folder):
    content = os.listdir(path=name_folder)
    for file in content:
        file_extansion = file[-4:]
        file_name = file.replace(file_extansion, '')
        image = Image.open(str(name_folder + f"/{file}"))
        image.thumbnail((1080, 1080))
        Path(upload_folder).mkdir(parents=True, exist_ok=True)
        path = Path.cwd() / upload_folder / file_name
        if image.mode != 'RGB':
            ycbcr_image = image.convert('YCbCr')
            ycbcr_image.save(f'{path}.jpg', 'JPEG')
        else:
            image.save(f'{path}.jpg', 'JPEG')


def delete_folder(name_folder):
    folder_path = Path(name_folder)
    shutil.rmtree(folder_path)


def upload_file(name_folder):
    password_inst = os.getenv('PASSWORD_INST')
    login_inst = os.getenv('LOGIN_INST')
    folder_contents = os.listdir(path=name_folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file in folder_contents:
        bot.upload_photo(str(name_folder) + f'/{file}')
        time.sleep(60)


def start():
    load_dotenv()
    folder_saving_images = "images"
    folder_uploading_instsgram = 'images_to_download'

    adjust_and_save_image(folder_saving_images, folder_uploading_instsgram)
    delete_folder(folder_saving_images)
    upload_file(folder_uploading_instsgram)
