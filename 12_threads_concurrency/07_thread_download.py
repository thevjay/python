import threading
import requests
import time

def download(url):
    print(f"{threading.current_thread().name}: Starting download from {url}")
    response = requests.get(url)
    print(f"{threading.current_thread().name}: Finished download from {url} with status code {response.status_code} size {len(response.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(f"Total time taken in seconds: {end - start:.2f}")