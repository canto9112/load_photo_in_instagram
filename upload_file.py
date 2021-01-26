import os
from instabot import Bot
import time


def upload_images_instagram(folder):
    password_inst = os.getenv('ISTAGRAM_PASSWORD')
    login_inst = os.getenv('INSTAGRAM_LOGIN')
    filenames = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for filename in filenames:
        bot.upload_photo(f'{folder}/{filename}')
        time.sleep(60)
