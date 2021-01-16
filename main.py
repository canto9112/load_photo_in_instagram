import requests
from pathlib import Path
from PIL import Image
from pprint import pprint
import os
from dotenv import load_dotenv
from instabot import Bot
import time


def save_image(url, image_name, name_folder):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    path = Path.cwd() / name_folder / image_name
    content = response.content
    with open(path, 'wb') as file:
        file.write(content)

# def fetch_spacex_last_launch(url, flight_number, name_folder, template_file_name):
#     params = {'flight_number': flight_number}
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     links_image = response.json()[0]['links']['flickr_images']
#     print('links_image', links_image)
#     Path(name_folder).mkdir(parents=True, exist_ok=True)
#     for link_number, link in enumerate(links_image):
#         filename = template_file_name.format(link_number)
#         path = Path.cwd() / name_folder / filename
#         response = requests.get(link)
#         response.raise_for_status()
#         content = response.content
#         with open(path, 'wb') as file:
#             file.write(content)

def fetch_spacex_last_launch(url, flight_number):
    params = {'flight_number': flight_number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_image = response.json()[0]['links']['flickr_images']
    return links_image


def get_images_habble(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image_files = response.json()['image_files']
    for image in image_files:
        last_image_url = ('http:'+image['file_url'])
    return last_image_url


def get_file_extension(url):
    extension = ('.' + url.split('.')[-1])
    return extension


# def safe_image_hubble(url, name_folder, template_file_name, extension):
#     response = requests.get(url, verify=False)
#     response.raise_for_status()
#     Path(name_folder).mkdir(parents=True, exist_ok=True)
#     filename = str(template_file_name) + extension
#     path = Path.cwd() / name_folder / filename
#     with open(path, 'wb') as file:
#         file.write(response.content)


def get_images_id_habble(url):
    params = {'page': 'all',
              'collection_name': 'spacecraft'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_json = response.json()
    images_id = []
    for id in response_json:
        images_id.append(id['id'])
    return images_id


def crop_save_image(name_folder):
    images = os.listdir(path=name_folder)
    for image in images:
        extansion = image[-4:]
        image_name = image.replace(extansion, '')
        open_image = Image.open("images/{}".format(image))
        open_image.thumbnail((1080, 1080))
        path = Path.cwd() / name_folder / image_name
        if open_image.mode != 'RGB':
            ycbcr_image = open_image.convert('YCbCr')
            ycbcr_image.save(f'{path}.jpg', 'JPEG')
        else:
            open_image.save(f'{path}.jpg', 'JPEG')

def remove_not_jpg(name_folder):
    images = os.listdir(path=name_folder)
    for image in images:
        extansion = image[-4:]
        if extansion != '.jpg':
            file_path = str(name_folder) + f'/{image}'
            os.remove(file_path)


def upload_images(name_folder):
    password_inst = os.getenv('password_inst')
    login_inst = os.getenv('login_inst')
    images = os.listdir(path=name_folder)
    bot = Bot()
    bot.login(username=login_inst, password=password_inst)
    for image in images:
        bot.upload_photo(str(name_folder) + f'/{image}')
        print(image, 'Опубликована')
        time.sleep(60)


if __name__ == "__main__":
    load_dotenv()
    name_folder = "images"
    # save images spaceX
    # url_spacex_api = 'https://api.spacexdata.com/v3/launches'
    # spacex_flight_number = '108'
    # spacex_template_file_name = 'spacex-{}.jpg'
    # url_spacex = fetch_spacex_last_launch(url_spacex_api, spacex_flight_number)
    # for link_number, link in enumerate(url_spacex):
    #     filename = spacex_template_file_name.format(link_number)
    #     save_image(link, filename, name_folder)
    #     print('save', link_number, filename, 'image')
    #
    # # save images HABBLE
    # url_habble_collections_api = 'http://hubblesite.org/api/v3/images'
    # habble_id_image = get_images_id_habble(url_habble_collections_api)
    # # habble_template_file_name = 'habble-{}.jpg'
    # for link_number, link in enumerate(habble_id_image):
    #     url_habble_api = 'http://hubblesite.org/api/v3/image/{}'.format(link)
    #     url_image_habble = get_images_habble(url_habble_api)
    #     file_extension_habbble_image = get_file_extension(url_image_habble)
    #     filename = (f'habble-{link_number}{file_extension_habbble_image}')
    #     save_image(url_image_habble, filename, name_folder)
    #     print('save', link_number, filename, 'image')
    #
    # cropped images
    # crop_save_image(name_folder)
    # # remove image not .jpg
    # remove_not_jpg(name_folder)

    upload_images(name_folder)
