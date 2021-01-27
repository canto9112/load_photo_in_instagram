import fetch_spacex
import fetch_hubble
import utils
import upload_file
from dotenv import load_dotenv
from pathlib import Path
import shutil
import os


def main():
    load_dotenv()

    ISTAGRAM_PASSWORD = os.getenv('ISTAGRAM_PASSWORD')
    INSTAGRAM_LOGIN = os.getenv('INSTAGRAM_LOGIN')
    HABBLE_COLLECTION_NAME = os.getenv('HABBLE_COLLECTION_NAME')

    images_saving_folder = "images"
    instagram_images_folder = 'images_to_download'

    Path(images_saving_folder).mkdir(parents=True, exist_ok=True)
    Path(instagram_images_folder).mkdir(parents=True, exist_ok=True)

    try:
        fetch_spacex.fetch_spacex_images(images_saving_folder)
        fetch_hubble.fetch_images_habble(images_saving_folder, HABBLE_COLLECTION_NAME)
        utils.adjust_and_save_images(images_saving_folder, instagram_images_folder)
        upload_file.upload_images_instagram(instagram_images_folder, INSTAGRAM_LOGIN, ISTAGRAM_PASSWORD)
    except IndexError:
        fetch_hubble.fetch_images_habble(images_saving_folder, HABBLE_COLLECTION_NAME)
    finally:
        shutil.rmtree(images_saving_folder)
        shutil.rmtree(instagram_images_folder)


if __name__ == "__main__":
    main()
