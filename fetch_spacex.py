import requests
from pathlib import Path


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    links_images = response.json()[0]['links']['flickr_images']
    return links_images


def save_image(url, image_name, folder_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    path = Path.cwd() / folder_name / image_name
    content = response.content
    with open(path, 'wb') as file:
        file.write(content)


def start():
    folder_saving_images = "images"
    url_latests_launch_api = 'https://api.spacexdata.com/v3/launches/latest'
    spacex_template_file_name = 'spacex-{}.jpg'
    url_spacex_last_launch = fetch_spacex_last_launch(url_latests_launch_api)
    for link_number, link in enumerate(url_spacex_last_launch):
        spacex_image_name = spacex_template_file_name.format(link_number)
        save_image(link, spacex_image_name, folder_saving_images)


