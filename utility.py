import os
import shutil
import requests
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("KEY")
client = OpenAI(api_key=key)

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

def chat_with_gpt(system_prompt: str, user_prompt: str, model: str = "gpt-4o-mini", max_tokens: int = None):
    try:
        # Base parameters
        params = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"}
        }
        
        # Add max_tokens only if it's provided (not None)
        if max_tokens is not None:
            params["max_tokens"] = max_tokens

        response = client.chat.completions.create(**params)
        return json.loads(response.choices[0].message.content)
    except Exception as err:
        print("Exception in LLM Call", err)
        return {}
