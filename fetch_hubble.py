import requests
import os
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
    for id_image in collection_contents:
        id_images.append(id_image['id'])
    return id_images


def get_images_habble():
    folder_saving_images = "images"
    habble_collection_name = os.getenv('HABBLE_COLLECTION_NAME')
    url_habble_collections_api = 'http://hubblesite.org/api/v3/images'
    id_images_habble = get_id_images_habble(url_habble_collections_api, habble_collection_name)
    for link_number, link in enumerate(id_images_habble):
        url_habble_api = 'http://hubblesite.org/api/v3/image/{}'.format(link)
        link_last_image = get_link_last_image(url_habble_api)
        file_extension_image_habbble = utils.get_file_extension(link_last_image)
        habble_image_name = (f'habble-{link_number}{file_extension_image_habbble}')
        utils.create_folder_save_images(folder_saving_images)
        utils.save_image(link_last_image, habble_image_name, folder_saving_images)
