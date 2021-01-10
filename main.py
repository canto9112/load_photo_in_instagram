import requests
from pathlib import Path
from pprint import pprint


def get_links_images():
    params = {'flight_number': '108'}
    response = requests.get('https://api.spacexdata.com/v3/launches', params=params)
    response.raise_for_status()
    links_image = response.json()[0]['links']['flickr_images']
    return links_image


def save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    folder = Path("images").mkdir(parents=True, exist_ok=True)
    last_links_images = get_links_images()

    for link_number, link in enumerate(last_links_images):
        filename = 'spacex{}.jpg'.format(link_number)
        path = Path.cwd() / 'images' / filename
        save_image(link, path)
