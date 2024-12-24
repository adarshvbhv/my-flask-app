import instaloader
import os
from pathlib import Path

def download_instagram_reel(reel_url, i, username):
    loader = instaloader.Instaloader()

    try:
        
        # Define the target path for the downloaded post
         # This will be 'hiii/username'

        target = Path('hiii')/f"{username}"
        shortcode = reel_url.split('/')[-2]
        loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target=target)

        files = os.listdir(target)
        
        for file in files:
            if file.endswith("UTC.mp4"):
                old_file_path = os.path.join(target, file)
                new_file_path = os.path.join(target, f"{i}.mp4")
                os.rename(old_file_path, new_file_path)
                print(f"Downloaded and renamed to {new_file_path}")

            if file.endswith("UTC.txt"):
                old_file_path = os.path.join(target, file)
                new_file_path = os.path.join(target, f"{i}.txt")
                os.rename(old_file_path, new_file_path)
                print(f"Downloaded and renamed to {new_file_path}")
                break

    except Exception as e:
        print(f'An error occurred: {e}')

def run_downloader(urls, username):
    n = len(urls)
    for i in range(n):
        download_instagram_reel(urls[i], i, username)