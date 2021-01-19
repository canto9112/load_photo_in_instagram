import requests
import os
import utils


def get_image_last_link(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image_files = response.json()['image_files']
    for image in image_files:
        image_last_link = ('http:'+image['file_url'])
    return image_last_link


def get_habble_image_ids(url, collection_name):
    params = {'page': 'all',
              'collection_name': collection_name}
    response = requests.get(url, params=params)
    response.raise_for_status()
    collection_contents = response.json()
    image_ids = []
    for image_id in collection_contents:
        image_ids.append(image_id['id'])
    return image_ids


def get_images_habble():
    images_folser = "images"
    habble_collection_name = os.getenv('HABBLE_COLLECTION_NAME')
    habble_collections_api_url = 'http://hubblesite.org/api/v3/images'
    habble_image_ids = get_habble_image_ids(habble_collections_api_url, habble_collection_name)
    for link_number, link in enumerate(habble_image_ids):
        habble_api_url = 'http://hubblesite.org/api/v3/image/{}'.format(link)
        image_last_link = get_image_last_link(habble_api_url)
        file_extension = utils.get_file_extension(image_last_link)
        habble_image_name = (f'habble-{link_number}{file_extension}')
        utils.create_folder_save_images(images_folser)
        utils.save_image(image_last_link, habble_image_name, images_folser)
