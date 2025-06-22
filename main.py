import os
import csv
import calendar
import time

from elevenlabs import ElevenLabs
from dotenv import load_dotenv
from datetime import datetime, UTC

load_dotenv(override=True)

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

##### Code to check the voices available #####

# response = client.voices.get_all()  
# voices = response.voices # List of Voice objects

# fieldnames = ["name", "voice_id", "available_for_tiers", "labels", "preview_url"] # Relevant fields

# voice_dicts = []

# for voice in voices:
#     voice_dicts.append({
#         "name": voice.name,
#         "voice_id": voice.voice_id,
#         "available_for_tiers": voice.available_for_tiers,
#         "labels": str(voice.labels),
#         "preview_url": voice.preview_url
#     })

# with open("voices_avail.csv", mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(voice_dicts)

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

##### Code to check usage for the month #####
# Time configuration
now = datetime.now(UTC)
first = datetime(now.year, now.month, 1, 0, 0, 0) 
last = datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1], 23, 59, 59)

# Convert to Unix timestamp in milliseconds
start = int(first.timestamp() * 1000)
end = int(last.timestamp() * 1000)

usage = client.usage.get(
    start_unix=start,
    end_unix=end
)

sum_of_usage = sum(usage.usage["All"])
remainder = 10000 - sum_of_usage
print(f"Character remaining: {remainder} characters")