import os
from threading import Thread
import requests

class ImageDownloader(Thread):
    def __init__(self, thread_id, name, urls):
        super(ImageDownloader, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.urls = urls

    def run(self):

        if not os.path.exists("images"):
            os.makedirs("images")

        for i, url in enumerate(self.urls):
            self.download_image(url, f"{self.thread_id}_{i}.jpg")

    def download_image(self, url, file_name):
        try:
            r = requests.get(url, stream=True, timeout=10)
            if r.status_code == 200:
                r.raw.decode_content = True
                file_path = f"images/{file_name}"

                with open(file_path, 'wb') as f:
                    f.write(r.content)
                print(f"{file_path} has been downloaded")
            else:
                print(f"Failed to download {url}. HTTP Status Code: {r.status_code}")
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
