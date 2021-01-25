import os
from instabot import Bot
import time


def upload_images_instagram(folder):
    password_inst = os.getenv('ISTAGRAM_PASSWORD')
    login_inst = os.getenv('INSTAGRAM_LOGIN')
    filepath = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file_name in filepath:
        bot.upload_photo(f'{folder}/{file_name}')
        time.sleep(60)
