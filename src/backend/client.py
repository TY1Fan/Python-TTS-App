import os
from elevenlabs import ElevenLabs
import boto3

class Client:
    
    def __init__(self, client_name):
        self.API_KEY_FILE = "env.txt"
        self.client_name = client_name
        self.credentials = self._load_credentials()
        self.client = self.set_client()
        if client_name == "AWS":
            self.session = self.set_session()

    def _load_credentials(self):
        creds = {}
        if not os.path.isfile(self.API_KEY_FILE):
            return creds
        with open(self.API_KEY_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                creds[key.strip()] = val.strip().strip('"')
        return creds

    def _write_credentials(self):
        lines = []
        for k, v in self.credentials.items():
            # wrap in quotes if contains spaces or special chars
            safe_val = v if '"' in v else f'"{v}"'
            lines.append(f"{k}={safe_val}")
        with open(self.API_KEY_FILE, "w") as f:
            f.write("\n".join(lines) + "\n")

    def set_credential(self, key: str, value: str):
        self.credentials[key] = value.strip()
        self._write_credentials()

        # Keep cached attrs up to date if relevant
        if key == "ELEVENLABS_API_KEY":
            self.elevenlabs_key = self.credentials[key]
            # refresh ElevenLabs client here if you have one
        elif key == "AWS_ACCESS_KEY_ID":
            self.aws_key = self.credentials[key]
        elif key == "AWS_SECRET_ACCESS_KEY":
            self.aws_secret = self.credentials[key]

    def set_client(self):
        if self.client_name == "ElevenLabs":
            client = ElevenLabs(api_key=self.credentials.get("ELEVENLABS_API_KEY"))
            self.client = client
            return client

        elif self.client_name == "AWS":
            polly_client = boto3.client(
                'polly',
                aws_access_key_id=self.credentials.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=self.credentials.get("AWS_SECRET_ACCESS_KEY"),
                region_name="us-east-1"
            )
            self.client = polly_client
            return polly_client
    
    def set_session(self):
        if self.client_name == "AWS":
            return boto3.Session(
                aws_access_key_id=self.credentials.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=self.credentials.get("AWS_SECRET_ACCESS_KEY"),
            )
        return None

    def is_valid_key(self, token):
        print(f"Validating API key: {token}")
        try:
            client = ElevenLabs(api_key=token)
            client.user.get()
            return True
        except Exception as e:
            print(f"Invalid API key: {e}")
            return False
    