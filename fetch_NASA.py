import requests
import os
from datetime import date, timedelta
import utils


def fetch_nasa_image_url(url, date, api_key):
    params = {
        'api_key': api_key,
        'date': date
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_url = response.json()['url']
    return image_url


def fetch_last_week_links():
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.getenv('NASA_API_KEY')
    date_now = date.today()

    links = []
    for day in range(1, 8):
        last_day_date = date_now - timedelta(days=day)
        link = fetch_nasa_image_url(api_url, last_day_date, api_key)
        links.append(link)
    return links


def fetch_nasa_images(folder_name):
    filename_template = 'nasa-{}.jpg'
    nasa_urls = fetch_last_week_links()
    for link_number, link in enumerate(nasa_urls):
        nasa_image_name = filename_template.format(link_number)
        utils.save_image(link, nasa_image_name, folder_name)
