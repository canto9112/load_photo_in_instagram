import requests
from pathlib import Path
from pprint import pprint


# def save_image(url, path):
#     response = requests.get(url)
#     response.raise_for_status()
#     with open(path, 'wb') as file:
#         file.write(response.content)


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


if __name__ == "__main__":
    url = 'https://api.spacexdata.com/v3/launches'
    flight_number = '108'
    name_folder = "images"
    template_file_name = 'spacex-{}.jpg'

    fetch_spacex_last_launch(url, flight_number, name_folder, template_file_name)