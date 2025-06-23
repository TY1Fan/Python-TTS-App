import os
import csv
import requests
import zipfile

from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

##### Function to check the voices available #####
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

##### Function to generate audio file from text #####
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

##### Function to get history of audio files generated #####
def download_history_audio(output_dir="history_audio"):

    os.makedirs(output_dir, exist_ok=True)

    history_response = client.history.list()
    history_items = history_response.history

    if not history_items:
        print("No history items found.")
        return

    history_ids = [item.history_item_id for item in history_items]

    url = "https://api.elevenlabs.io/v1/history/download"
    payload = {"history_item_ids": history_ids}
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Used ChatGPT to generate the code for downloading and extracting the zip file
    zip_path = os.path.join(output_dir, "history_audio.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    os.remove(zip_path)

download_history_audio()