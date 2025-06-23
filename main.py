import os
import csv

from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

##### Code to check the voices available #####
def get_available_voices():
    response = client.voices.get_all()
    voices = response.voices  # List of Voice objects

    fieldnames = ["name", "voice_id", "available_for_tiers", "labels", "preview_url"]  # Relevant fields

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
def generate_audio_from_text(model_id, voice_id, text, output_file):
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        output_format="mp3_44100_128",
        text=text,
        model_id=model_id,
    )

    with open(output_file, "wb") as f:
        for chunk in audio:
            f.write(chunk)

##### Function to check usage for the month #####
def get_usage():
    subscription = client.user.subscription.get()
    remainder = subscription.character_limit - subscription.character_count
    print(f"Character remaining: {remainder} characters")
