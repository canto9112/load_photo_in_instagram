import os
from instabot import Bot
import time


def upload_images_instagram(folder, login, password):
    filenames = os.listdir(path=folder)
    bot = Bot()
    bot.login(username=login, password=password)
    for filename in filenames:
        bot.upload_photo(f'{folder}/{filename}')
        time.sleep(60)
