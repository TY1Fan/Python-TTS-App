import pygame
import tkinter as tk

from tkinter import ttk

class Main_Screen:

    def __init__(self, client, user, voice):
        self.client = client
        self.user = user
        self.voice = voice

    def play_audio(self):
        if output_file_name:
            pygame.mixer.music.load(output_file_name)
            pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()

    def generate_audio(self, text):
        global output_file_name
        if text:
            model_id = "eleven_multilingual_v1"
            voice_id = "onwK4e9ZLuTAKqWW03F9"
            settings = None
            output_file_name = "output.mp3"
            self.voice.generate_audio_from_text(
                model_id=model_id,
                voice_id=voice_id,
                text=text,
                output_file=output_file_name,
                settings=settings
            )
            print(f"Audio generated and saved to {output_file_name}")
        else:
            print("No text provided for audio generation.")

    def display_screen(self):
        # Initialize the main window
        window = tk.Tk()

        # Set title of GUI
        window.title("Python TTS App")

        # Label to display character usage
        label = ttk.Label(window, text=self.user.get_usage())
        label.pack(pady=10)

        generate_button = tk.Button(
            window, text="Generate Audio", command=lambda: self.generate_audio(recognized_text_entry.get("1.0", tk.END).strip()))
        generate_button.pack(pady=10)

        play_button = tk.Button(window, text="Play", command=self.play_audio)
        play_button.pack(pady=10)

        stop_button = tk.Button(window, text="Stop", command=self.stop_audio)
        stop_button.pack(pady=10)

        recognized_text_entry = tk.Text(window, height=5, width=50)
        recognized_text_entry.pack(pady=10)

        pygame.mixer.init()

        window.mainloop()