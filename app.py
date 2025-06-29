import backend
import os
import pygame
import tkinter as tk

from tkinter import ttk

# Check for api key
if not os.path.isfile(".env"):
    root = tk.Tk()
    root.title("API Key Required")

    # Prompt user to enter the API key
    label = tk.Label(root, text="Enter Elevenlabs API Key:")
    label.pack(pady=10)

    api_key_entry = tk.Entry(root)
    api_key_entry.pack(pady=10)

    def on_submit():
        api_key = api_key_entry.get()
        # if api_key:
        backend.save_api_key(api_key)
        backend.client = backend.get_client()
        root.destroy()
        # else:
            # tk.messagebox.showerror("Error", "API Key cannot be empty.")

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

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
        backend.generate_audio_from_text(
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
label = ttk.Label(window, text=backend.get_usage())
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