import os

from elevenlabs import ElevenLabs
from dotenv import load_dotenv

class Client:

    api_key: str
    client: object

    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.client = ElevenLabs(api_key=self.api_key)

    def set_api_key(self, token: str):
        with open(".env", "w") as f:
            f.write(f'ELEVENLABS_API_KEY="{token}"\n')
        print(f"API key saved")

        load_dotenv(override=True)
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        print(self.api_key)
    
    def set_client(self):
        load_dotenv(override=True)
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    

