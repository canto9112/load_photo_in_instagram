import fetch_spacex
import fetch_hubble
import utils
import upload_file
from dotenv import load_dotenv
from pathlib import Path
import shutil
import os


if __name__ == "__main__":
    load_dotenv()
    images_saving_folder = "images"
    instagram_images_folder = 'images_to_download'
    password_instagram = os.getenv('ISTAGRAM_PASSWORD')
    login_instagram = os.getenv('INSTAGRAM_LOGIN')
    habble_collection_name = os.getenv('HABBLE_COLLECTION_NAME')
    Path(images_saving_folder).mkdir(parents=True, exist_ok=True)
    Path(instagram_images_folder).mkdir(parents=True, exist_ok=True)
    try:
        fetch_spacex.fetch_spacex_images(images_saving_folder)
        fetch_hubble.fetch_images_habble(images_saving_folder, habble_collection_name)
    except IndexError:
        fetch_hubble.fetch_images_habble(images_saving_folder, habble_collection_name)
    finally:
        utils.adjust_and_save_images(images_saving_folder, instagram_images_folder)
        upload_file.upload_images_instagram(instagram_images_folder, login_instagram, password_instagram)
        shutil.rmtree(images_saving_folder)
        shutil.rmtree(instagram_images_folder)

