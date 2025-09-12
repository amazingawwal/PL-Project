import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url, fetched_hashes):
    try:
        # Fetch the image with a timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad HTTP codes

        # Check Content-Type header to confirm it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (Not an image): {url}")
            return

        # Extract filename from URL or assign default
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Create save path
        filepath = os.path.join("Fetched_Images", filename)

        # Check for duplicates using hash
        file_hash = hashlib.md5(response.content).hexdigest()
        if file_hash in fetched_hashes:
            print(f"✗ Duplicate skipped: {filename}")
            return
        fetched_hashes.add(file_hash)

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ensure Fetched_Images directory exists
    os.makedirs("Fetched_Images", exist_ok=True)

    # Allow multiple URLs
    urls = input("Please enter image URL(s), separated by spaces:\n").split()

    fetched_hashes = set()

    for url in urls:
        fetch_image(url.strip(), fetched_hashes)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
