import fetch_spacex
import fetch_hubble
import upload_file
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    fetch_spacex.get_spacex_images()
    fetch_hubble.get_images_habble()
    upload_file.start_uploading_images()
