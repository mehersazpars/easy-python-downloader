import os
import urllib.request
import threading
import time

# === CONFIG ===
DOWNLOAD_DIR = "F:/downloads" #You Can Change it :-D
NUM_THREADS = 8
CHUNK_SIZE = 1024 * 100  # 100 KB

# === Disable system proxy for Python app only ===
proxy_handler = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

def get_file_info(url):
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req) as resp:
        size = int(resp.getheader('Content-Length', '0'))
        filename = url.split('/')[-1].split('?')[0]
        return size, filename

def download_part(url, start, end, part_file, idx):
    req = urllib.request.Request(url)
    req.headers['Range'] = f'bytes={start}-{end}'
    with urllib.request.urlopen(req) as response, open(part_file, 'wb') as out:
        while True:
            chunk = response.read(CHUNK_SIZE)
            if not chunk:
                break
            out.write(chunk)

def merge_parts(part_files, output_file):
    with open(output_file, 'wb') as final_file:
        for part in part_files:
            with open(part, 'rb') as pf:
                final_file.write(pf.read())
            os.remove(part)

def download_file(url):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    file_size, filename = get_file_info(url)
    print(f"Downloading: {filename} ({file_size / 1024 / 1024:.2f} MB)")

    output_path = os.path.join(DOWNLOAD_DIR, filename)
    part_size = file_size // NUM_THREADS
    threads = []
    part_files = []

    start_time = time.time()

    for i in range(NUM_THREADS):
        start_byte = i * part_size
        end_byte = file_size - 1 if i == NUM_THREADS - 1 else (start_byte + part_size - 1)
        part_file = f"{output_path}.part{i}"
        part_files.append(part_file)
        t = threading.Thread(target=download_part, args=(url, start_byte, end_byte, part_file, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    merge_parts(part_files, output_path)

    print(f"\n✅ Download complete: {output_path}")
    print(f"⏱ Time: {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    url = input("Enter file URL: ").strip()
    download_file(url)
