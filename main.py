import fetch_spacex
import fetch_hubble
import upload_file


if __name__ == "__main__":
    fetch_spacex.get_images_spacex()
    fetch_hubble.get_images_habble()
    upload_file.start_uploading_images()
