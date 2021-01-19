import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import utils


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


def get_images_habble():
    load_dotenv()
    folder_saving_images = "images"
    habble_collection_name = os.getenv('HABBLE_COLLECTION_NAME')
    url_habble_collections_api = 'http://hubblesite.org/api/v3/images'
    id_images_habble = get_id_images_habble(url_habble_collections_api, habble_collection_name)
    for link_number, link in enumerate(id_images_habble):
        url_habble_api = 'http://hubblesite.org/api/v3/image/{}'.format(link)
        link_last_image = get_link_last_image(url_habble_api)
        file_extension_image_habbble = get_file_extension(link_last_image)
        habble_image_name = (f'habble-{link_number}{file_extension_image_habbble}')
        utils.save_image(link_last_image, habble_image_name, folder_saving_images)
