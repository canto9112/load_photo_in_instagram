import requests
import utils


def fetch_spacex_launch(url, flight_number):
    params = {'flight_number': flight_number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_images = response.json()[0]['links']['flickr_images']
    return links_images


def fetch_spacex_images(folder_name, spacex_flight_number='220'):
    url_spacex_api = 'https://api.spacexdata.com/v3/launches'
    spacex_template_file_name = 'spacex-{}.jpg'
    spacex_last_launch_url = fetch_spacex_launch(url_spacex_api, spacex_flight_number)
    for link_number, link in enumerate(spacex_last_launch_url):
        spacex_image_name = spacex_template_file_name.format(link_number)
        utils.save_image(link, spacex_image_name, folder_name)
