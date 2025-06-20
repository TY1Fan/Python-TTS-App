import os
import csv

from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

##### Code to check the voices available #####

response = client.voices.get_all()  
voices = response.voices # List of Voice objects

fieldnames = ["name", "voice_id", "available_for_tiers", "labels", "preview_url"] # Relevant fields

voice_dicts = []

for voice in voices:
    voice_dicts.append({
        "name": voice.name,
        "voice_id": voice.voice_id,
        "available_for_tiers": voice.available_for_tiers,
        "labels": str(voice.labels),
        "preview_url": voice.preview_url
    })

with open("voices_avail.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(voice_dicts)

##### Code to generate audio file from text #####
# audio = client.text_to_speech.convert(
#     voice_id="JBFqnCBsd6RMkjVDRZzb",
#     output_format="mp3_44100_128",
#     text="Testing",
#     model_id="eleven_multilingual_v2",
# )

# with open("audio.mp3", "wb") as f:
#     for chunk in audio:
#         f.write(chunk)

