import fetch_spacex
import fetch_hubble
import upload_file
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    fetch_spacex.fetch_spacex_images()
    fetch_hubble.fetch_images_habble()
    upload_file.uploading_images()
