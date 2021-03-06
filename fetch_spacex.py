import requests
import utils


def fetch_spacex_launch_urls(url, flight_number):
    params = {'flight_number': flight_number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_images = response.json()[0]['links']['flickr_images']
    return links_images


def fetch_spacex_images(folder_name, spacex_flight_number='220'):
    url_spacex_api = 'https://api.spacexdata.com/v3/launches'
    filename_template = 'spacex-{}.jpg'
    spacex_launch_urls = fetch_spacex_launch_urls(url_spacex_api, spacex_flight_number)
    for link_number, link in enumerate(spacex_launch_urls):
        spacex_image_name = filename_template.format(link_number)
        utils.save_image(link, spacex_image_name, folder_name)
