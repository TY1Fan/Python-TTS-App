import os
import requests
import zipfile

from backend.client import Client

class User(Client):

    def __init__(self):
        super().__init__()
    
    def get_usage(self):
        try:
            subscription = self.client.user.subscription.get()
            remainder = subscription.character_limit - subscription.character_count
            result = f"Character remaining: {remainder} characters"

            print(result)
            return result
        except Exception as e:
            print(f"Error fetching usage: {e}")
            return "Error fetching usage"
    
    def download_history_audio(self, output_dir="history_audio"):

        os.makedirs(output_dir, exist_ok=True)

        history_response = self.client.history.list()
        history_items = history_response.history

        if not history_items:
            print("No history items found.")
            return

        history_ids = [item.history_item_id for item in history_items]

        url = "https://api.elevenlabs.io/v1/history/download"
        payload = {"history_item_ids": history_ids}
        headers = {
            "xi-api-key": self.get_api_key(),
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        # Used ChatGPT-4o to generate the code for downloading and extracting the zip file
        zip_path = os.path.join(output_dir, "history_audio.zip")
        with open(zip_path, "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)

        os.remove(zip_path)

        # Return list of downloaded files
        return [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".mp3")]
