import os
import shutil
from pathlib import Path

def delete_all_files_and_folders(username):
    # Define the target directory using Path
    directory = Path(__file__).parent / "hiii" / f"{username}"
    
    # Check if the directory exists
    if directory.exists() and directory.is_dir():
        # Loop through everything in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            try:
                if os.path.isdir(file_path):
                    # If it's a directory, delete it and its contents
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file_path}")
                elif os.path.isfile(file_path):
                    # If it's a file, delete it
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        print(f"The directory {directory} does not exist.")

# Call the function
# delete_all_files_and_folders()
