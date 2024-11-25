import time
from thread import ImageDownloader


def get_image_url(count):
    if count <= 0:
        print("Invalid count")
        return

    urls = []
    for i in range(count):
        url = input(f"Enter URL {i + 1}: ")
        if url:
            urls.append(url)
        else:
            print("Empty URL, skipping.")
    return urls


if __name__ == "__main__":
    start = time.time_ns()
    urls = list(get_image_url(3))
    num_threads = 10

    url_list = [urls[i:i + num_threads] for i in range(0, len(urls), num_threads)]
    threads = []


    for i, url_group in enumerate(url_list):
        th = ImageDownloader(i, f"Thread-{i}", url_group)
        th.start()
        threads.append(th)


    for th in threads:
        th.join()


    diff = time.time_ns() - start
    print("Duration is ", diff / 1_000_000, "ms")
