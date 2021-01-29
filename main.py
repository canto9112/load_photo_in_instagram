import fetch_spacex
import fetch_hubble
import fetch_NASA
import utils
import upload_file
from dotenv import load_dotenv
from pathlib import Path
import shutil
import os


def main():
    load_dotenv()

    instagram_password = os.getenv('ISTAGRAM_PASSWORD')
    instagram_login = os.getenv('INSTAGRAM_LOGIN')
    habble_collection_name = os.getenv('HABBLE_COLLECTION_NAME')

    images_saving_folder = "images"
    instagram_images_folder = 'images_to_download'

    Path(images_saving_folder).mkdir(parents=True, exist_ok=True)
    Path(instagram_images_folder).mkdir(parents=True, exist_ok=True)

    try:
        fetch_NASA.fetch_nasa_images(images_saving_folder)
        fetch_spacex.fetch_spacex_images(images_saving_folder)
        fetch_hubble.fetch_images_habble(images_saving_folder, habble_collection_name)
        utils.adjust_and_save_images(images_saving_folder, instagram_images_folder)
        upload_file.upload_images_instagram(instagram_images_folder, instagram_login, instagram_password)
    except IndexError:
        fetch_hubble.fetch_images_habble(images_saving_folder, habble_collection_name)
    finally:
        shutil.rmtree(images_saving_folder)
        shutil.rmtree(instagram_images_folder)


if __name__ == "__main__":
    main()
