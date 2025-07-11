import pygame
import tkinter as tk

from frontend.components.label import Label
from frontend.components.entry import Entry
from frontend.components.button import Button
from frontend.components.textentry import TextEntry

class Main_Screen:

    def __init__(self, client, user, voice):
        self.client = client
        self.user = user
        self.voice = voice
        self.label = Label()
        self.entry = Entry()
        self.button = Button()
        self.text_entry = TextEntry()

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
        root = tk.Tk()

        root.title("Python TTS App")

        self.label.create_label(parent=root, text=self.user.get_usage(), pady=10)

        command = lambda: self.generate_audio(text_entry.get("1.0", tk.END).strip())
        
        self.button.create_button(root, text="Generate Audio", command=command, pady=10)
        self.button.create_button(root, text="Play", command=self.play_audio, pady=10)    
        self.button.create_button(root, text="Stop", command=self.stop_audio, pady=10)
        text_entry = self.text_entry.create_text_entry(parent=root, height=5, width=50, pady=10)

        pygame.mixer.init()

        root.mainloop()