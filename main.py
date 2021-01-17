import fetch_spacex
import fetch_hubble
import upload_file


if __name__ == "__main__":
    fetch_spacex.start()
    fetch_hubble.start()
    upload_file.start()
