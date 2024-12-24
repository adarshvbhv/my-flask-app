import os
from pathlib import Path

def make_map(username):
    directory = Path(__file__).parent / "hiii" / f"{username}"
    folder_map = {}

    for file in directory.iterdir():  # Use iterdir() instead of os.listdir
        if file.is_file() and file.suffix == '.txt':  # Use Path methods
            folder_map[file.stem + '.mp4'] = file.name  # Use stem to get the filename without extension
    return folder_map