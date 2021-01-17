import requests
from pathlib import Path
from PIL import Image
import os
from dotenv import load_dotenv
from instabot import Bot
import time
import shutil


def fetch_spacex_last_launch(url, flight_number):
    params = {'flight_number': flight_number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_images = response.json()[0]['links']['flickr_images']
    return links_images


def get_link_last_image(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image_files = response.json()['image_files']
    for image in image_files:
        link_last_image = ('http:'+image['file_url'])
    return link_last_image


def get_id_images_habble(url, collection_name):
    params = {'page': 'all',
              'collection_name': collection_name}
    response = requests.get(url, params=params)
    response.raise_for_status()
    collection_contents = response.json()
    id_images = []
    for id in collection_contents:
        id_images.append(id['id'])
    return id_images


def get_file_extension(url):
    file_extension = ('.' + url.split('.')[-1])
    return file_extension


def save_image(url, image_name, folder_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    path = Path.cwd() / folder_name / image_name
    content = response.content
    with open(path, 'wb') as file:
        file.write(content)


def adjust_and_save_image(name_folder, upload_folder):
    content = os.listdir(path=name_folder)
    for file in content:
        file_extansion = file[-4:]
        file_name = file.replace(file_extansion, '')
        image = Image.open("images/{}".format(file))
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
    password_inst = os.getenv('password_inst')
    login_inst = os.getenv('login_inst')
    folder_contents = os.listdir(path=name_folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for file in folder_contents:
        bot.upload_photo(str(name_folder) + f'/{file}')
        time.sleep(60)


if __name__ == "__main__":
    load_dotenv()
    folder_saving_images = "images"
    folder_uploading_instsgram = 'uploads_images'
    url_spacex_api = 'https://api.spacexdata.com/v3/launches'
    spacex_flight_number = '108'
    spacex_template_file_name = 'spacex-{}.jpg'

    url_spacex_last_launch = fetch_spacex_last_launch(url_spacex_api, spacex_flight_number)
    for link_number, link in enumerate(url_spacex_last_launch):
        spacex_image_name = spacex_template_file_name.format(link_number)
        save_image(link, spacex_image_name, folder_saving_images)

    habble_collection_name = 'spacecraft'
    url_habble_collections_api = 'http://hubblesite.org/api/v3/images'
    id_images_habble = get_id_images_habble(url_habble_collections_api, habble_collection_name)
    habble_template_file_name = 'habble-{}.jpg'

    for link_number, link in enumerate(id_images_habble):
        url_habble_api = 'http://hubblesite.org/api/v3/image/{}'.format(link)
        link_last_image = get_link_last_image(url_habble_api)
        file_extension_image_habbble = get_file_extension(link_last_image)
        habble_image_name = (f'habble-{link_number}{file_extension_image_habbble}')
        save_image(link_last_image, habble_image_name, folder_saving_images)

    adjust_and_save_image(folder_saving_images, folder_uploading_instsgram)
    delete_folder(folder_saving_images)
    upload_file(folder_uploading_instsgram)
