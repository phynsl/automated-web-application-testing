import requests
import time
import os

def test_file_download():
    url = "https://example.com"
    local_path = "downloaded.txt"

    start = time.time()
    response = requests.get(url, stream=True)
    with open(local_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    end = time.time()

    assert response.status_code == 200
    assert os.path.exists(local_path)
    assert os.path.getsize(local_path) > 0
    print(f"Downloaded in {end - start:.2f} seconds")

if __name__ == "__main__":
    test_file_download()
