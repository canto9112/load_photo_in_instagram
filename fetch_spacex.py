import requests
import utils


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()[0]['links']['flickr_images']
    return image_links


def get_spacex_images():
    folder_saving_images = "images"
    latests_launch_api_url = 'https://api.spacexdata.com/v3/launches/latest'
    spacex_template_file_name = 'spacex-{}.jpg'
    spacex_last_launch_url = fetch_spacex_last_launch(latests_launch_api_url)
    for link_number, link in enumerate(spacex_last_launch_url):
        spacex_image_name = spacex_template_file_name.format(link_number)
        utils.create_folder_save_images(folder_saving_images)
        utils.save_image(link, spacex_image_name, folder_saving_images)
