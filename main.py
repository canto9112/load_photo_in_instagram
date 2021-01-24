import fetch_spacex
import fetch_hubble
import upload_file
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    folder_saving_images = "images"
    instagram_images_folder = 'images_to_download'

    fetch_spacex.fetch_spacex_images(folder_saving_images)
    fetch_hubble.fetch_images_habble(folder_saving_images)
    upload_file.uploading_images(folder_saving_images, instagram_images_folder)
