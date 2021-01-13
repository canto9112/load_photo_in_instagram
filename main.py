import requests
from pathlib import Path
from pprint import pprint


def save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, flight_number, name_folder, template_file_name):
    params = {'flight_number': flight_number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_image = response.json()[0]['links']['flickr_images']
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    for link_number, link in enumerate(links_image):
        filename = template_file_name.format(link_number)
        path = Path.cwd() / name_folder / filename
        response = requests.get(link)
        response.raise_for_status()
        content = response.content
        with open(path, 'wb') as file:
            file.write(content)


def get_images_habble(url):
    response = requests.get(url)
    response.raise_for_status()
    image_files = response.json()['image_files']
    for image in image_files:
        last_image_url = ('http:'+image['file_url'])
    return last_image_url


def get_file_extension(url):
    extension = ('.' + url.split('.')[-1])
    return extension


def safe_image_hubble(url, name_folder, template_file_name, extension):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    if extension != '.tif':
        Path(name_folder).mkdir(parents=True, exist_ok=True)
        print('template_file_name -', template_file_name)
        print('extension -', extension)
        filename = str(template_file_name) + extension
        path = Path.cwd() / name_folder / filename
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        Path('tif').mkdir(parents=True, exist_ok=True)
        filename = str(template_file_name) + extension
        path = Path.cwd() / 'tif' / filename
        with open(path, 'wb') as file:
            file.write(response.content)
        print(extension, '= .tif')


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


if __name__ == "__main__":
    # url_spacex_api = 'https://api.spacexdata.com/v3/launches'
    # spacex_flight_number = '108'
    name_folder = "images"
    # spacex_template_file_name = 'spacex-{}.jpg'
    # fetch_spacex_last_launch(url_spacex_api, spacex_flight_number, name_folder, spacex_template_file_name)

    url_habble_collections_api = 'http://hubblesite.org/api/v3/images'

    habble_id_image = get_images_id_habble(url_habble_collections_api)
    for id in habble_id_image:
        url_habble_api = 'http://hubblesite.org/api/v3/image/{}'.format(id)
        url_image_habble = get_images_habble(url_habble_api)
        file_extension_habbble_image = get_file_extension(url_image_habble)
        safe_image_hubble(url_image_habble, name_folder, id, file_extension_habbble_image)
        print(id, 'safe')
