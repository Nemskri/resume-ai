import os
import shutil
import requests



def download_file(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, "wb") as f:
        f.write(response.content)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def deleteFolder(folder_path):
    try:
        print("Deleting Folder", folder_path)
        shutil.rmtree(folder_path)
        print(f"Folder {folder_path} deleted successfully.")
    except:
        print("An exception occurred while Deleting")