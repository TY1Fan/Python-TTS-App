import os
import sys
import requests
import zipfile

from backend.client import Client

class User(Client):

    def __init__(self, client_name):
        super().__init__(client_name=client_name)
    
    ##### For ElevenLabs Users #####
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

        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        audio_folder = os.path.join(base_dir, output_dir)
        os.makedirs(audio_folder, exist_ok=True)

        history_response = self.client.history.list(page_size=20)
        history_items = history_response.history

        if not history_items:
            print("No history items found.")
            return

        history_ids = [item.history_item_id for item in history_items]

        url = "https://api.elevenlabs.io/v1/history/download"
        payload = {"history_item_ids": history_ids}
        headers = {
            "xi-api-key": self.credentials.get("ELEVENLABS_API_KEY"),
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
    
