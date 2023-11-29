import requests
import concurrent.futures

# Function to download a file given its URL
def download_file(url):
    filename = url.split("/")[-1]  # Extract filename from URL
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return f"Downloaded {filename}"

# List of URLs to download (replace these with your URLs)
urls = [
    'https://humix.com/video/SARt_QiIqaf/file1.ogv',
    'https://humix.com/video/SARt_QiIqaf/file1.jpg',
    'https://example.com/file2.pdf',
    'https://example.com/file3.txt',
    # Add more URLs as needed
]

# Download files in parallel using a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_file, urls)

# Print results
for result in results:
    print(result)
