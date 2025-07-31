import pyttsx3
import csv

engine = pyttsx3.init()

###### For testing speech synthesis ######
def speech_synthesis(text, rate, volume):
    engine.setProperty('rate', rate) # Integer speech rate in words per minute.
    engine.setProperty('volume', volume) # 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

###### For testing saving to file ######
def save_to_file(text, filename):
    engine.save_to_file(text, filename)
    engine.runAndWait()

###### For testing different voices ######
def get_available_voices():
    voices = engine.getProperty('voices')

    fieldnames = ["name", "voice_id", "languages", "gender", "age"]  # Relevant fields

    voice_dicts = []

    for voice in voices:
        voice_dicts.append({
            "name": voice.name,
            "voice_id": voice.id,
            "languages": voice.languages,
            "gender": voice.gender,
            "age": voice.age
        })

    with open("voices_avail.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(voice_dicts)
