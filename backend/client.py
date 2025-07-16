import os
from elevenlabs import ElevenLabs

class Client:
    
    def __init__(self):
        self.API_KEY_FILE = "env.txt"
        self.api_key = self.get_api_key()
        self.client = ElevenLabs(api_key=self.api_key)

    def get_api_key(self):
        if not os.path.isfile(self.API_KEY_FILE):
            return None
        with open(self.API_KEY_FILE, "r") as f:
            return f.read().strip()

    def set_api_key(self, token: str):
        with open(self.API_KEY_FILE, "w") as f:
            f.write(token.strip())
        print("API key saved.")

        self.api_key = token.strip()
        self.set_client()

    def set_client(self):
        self.client = ElevenLabs(api_key=self.api_key)

    def is_valid_key(self, token):
        try:
            client = ElevenLabs(api_key=token)
            client.user.get()
            return True
        except Exception as e:
            print(f"Invalid API key: {e}")
            return False
