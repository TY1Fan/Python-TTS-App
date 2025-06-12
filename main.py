import os

from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

audio = client.text_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    text="Testing",
    model_id="eleven_multilingual_v2",
)

with open("audio.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

