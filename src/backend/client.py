import os
import sys
import boto3

from elevenlabs import ElevenLabs
from concurrent.futures import ThreadPoolExecutor, as_completed

class Client:
    
    def __init__(self, client_name):
        self.API_KEY_FILE = "env.txt"
        self.client_name = client_name
        self.credentials = self._load_credentials()
        self.client = self.set_client()
        if client_name == "AWS":
            self.session = self.set_polly_session()

    # Used ChatGPT-4o to generate lines 19 - 76 for better credential management
    def _load_credentials(self):
        if getattr(sys, 'frozen', False):
            # Running in a bundle (PyInstaller)
            base_path = os.path.dirname(sys.executable)
        else:
            # Running as a script
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Path to the .env or credentials file in the same folder as the exe/script
        env_file_path = os.path.join(base_path, self.API_KEY_FILE)

        creds = {}
        if not os.path.isfile(env_file_path):
            return creds
        with open(env_file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                creds[key.strip()] = val.strip().strip('"')
        return creds

    def _write_credentials(self):
        # Get the path to the directory of the executable or script
        if getattr(sys, 'frozen', False):
            # Running in a bundle (PyInstaller)
            base_path = os.path.dirname(sys.executable)
        else:
            # Running as a script
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Path to the .env or credentials file in the same folder as the exe/script
        env_file_path = os.path.join(base_path, self.API_KEY_FILE)

        # Write credentials to file
        lines = []
        for k, v in self.credentials.items():
            safe_val = v if '"' in v else f'"{v}"'
            lines.append(f"{k}={safe_val}")

        with open(env_file_path, "w") as f:
            f.write("\n".join(lines) + "\n")

        self.API_KEY_FILE = env_file_path  # Optional: store path if used elsewhere

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

    def set_client(self, region_name="us-east-1"):
        if self.client_name == "ElevenLabs":
            client = ElevenLabs(api_key=self.credentials.get("ELEVENLABS_API_KEY"))
            self.client = client
            return client

        elif self.client_name == "AWS":
            polly_client = boto3.client(
                'polly',
                aws_access_key_id=self.credentials.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=self.credentials.get("AWS_SECRET_ACCESS_KEY"),
                region_name=region_name
            )
            self.client = polly_client
            return polly_client
    
    def set_polly_session(self):
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
    
    def is_valid_aws_key(self, access_key, secret_key):
        try:
            client = boto3.client(
                'polly',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name="us-east-1"
            )
            client.describe_voices()
            return True
        except Exception as e:
            print(f"Invalid AWS credentials: {e}")
            return False
        
    ##### For AWS Users #####
    def set_region(self, region_name):
        self.set_client(region_name=region_name)
    
    def get_region(self):
        available_regions = []
        all_regions = self.session.get_available_regions('polly')

        # ChatGPT-4o used to generate lines 110 - 130 for faster region checking
        def check_region(region):
            try:
                temp_client = boto3.client(
                    'polly',
                    aws_access_key_id=self.credentials.get("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=self.credentials.get("AWS_SECRET_ACCESS_KEY"),
                    region_name=region
                )
                temp_client.describe_voices()
                return region
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(check_region, region): region for region in all_regions}
            for future in as_completed(futures):
                region = future.result()
                if region:
                    available_regions.append(region)

        return available_regions
    
    def get_engines(self, region_name):
        all_engines = ["Standard", "Neural", "Long-form", "Generative"]
        available_engines = []

        self.set_region(region_name)

        # ChatGPT-4o used to generate lines 139 - 154 for faster region checking
        def check_engine(engine):
            try:
                response = self.client.describe_voices(Engine=engine.lower())
                if response['Voices']:
                    return engine
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(check_engine, engine): engine for engine in all_engines}
            for future in as_completed(futures):
                engine = future.result()
                if engine:
                    available_engines.append(engine)

        return available_engines