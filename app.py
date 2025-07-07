import os
import pygame
import tkinter as tk

from tkinter import ttk
from backend.client import Client
from backend.user import User
from backend.voice import Voice
from frontend.screens.api_screen import api_screen

##### Initialize backend modules #####
client = Client()
user = User()
voice = Voice()

##### Frontend GUI setup #####
# Check for api key
if not os.path.isfile("backend/.env"):
    api_screen(client)

def play_audio():
    if output_file_name:
        pygame.mixer.music.load(output_file_name)
        pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def generate_audio():
    global output_file_name
    text = recognized_text_entry.get("1.0", tk.END).strip()
    if text:
        model_id = "eleven_multilingual_v1"
        voice_id = "onwK4e9ZLuTAKqWW03F9"
        settings = None
        output_file_name = "output.mp3"
        voice.generate_audio_from_text(
            model_id=model_id,
            voice_id=voice_id,
            text=text,
            output_file=output_file_name,
            settings=settings
        )
        print(f"Audio generated and saved to {output_file_name}")
    else:
        print("No text provided for audio generation.")

# Initialize the main window
window = tk.Tk()

# Set title of GUI
window.title("Python TTS App")

# Label to display character usage
label = ttk.Label(window, text=user.get_usage())
label.pack(pady=10)

generate_button = tk.Button(
    window, text="Generate Audio", command=generate_audio)
generate_button.pack(pady=10)

play_button = tk.Button(window, text="Play", command=play_audio)
play_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop", command=stop_audio)
stop_button.pack(pady=10)

recognized_text_entry = tk.Text(window, height=5, width=50)
recognized_text_entry.pack(pady=10)

pygame.mixer.init()

window.mainloop()