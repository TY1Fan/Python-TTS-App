import tkinter as tk
import os
import sys
import subprocess

from frontend.components.label import Label
from frontend.components.button import Button
from frontend.components.textentry import TextEntry
from frontend.components.entry import Entry

class Main_Panel:
    def __init__(self, user, voice, output_file_name):
        self.user = user
        self.voice = voice
        self.output_file_name = output_file_name
        self.label = Label()
        self.button = Button()
        self.entry = Entry()
        self.text_entry = TextEntry()
    
    # Claude Sonnet 3.7 used to generate line 22 to 28 for routing the app back to entry point
    def restart_app(self):
        """Restart the application to return to the initial selection screen."""
        python = sys.executable
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'app.py')
        
        # Start the app again in a new process
        subprocess.Popen([python, script_path])

    def display_card(self, parent, char_id, root):
        def generate_command(): 
            message = self.voice.generate_audio_from_text(
                text = text_entry.get("1.0", tk.END).strip(), 
                voice_id = char_id(),
                output_file = self.output_file_name,
                model_id = "eleven_multilingual_v2",
                settings = self.voice.get_voice_settings(character_id=char_id())
            )
            status_label.delete(0, tk.END)
            status_label.insert(0, "Status: " + message)
            usage_label.config(text=self.user.get_usage())

        def change_tts():
            root.destroy()
            self.restart_app()
            
        self.label.create_label(parent, text="ThinkAloud", pady=(10, 2), font=("Helvetica", 20, "bold"))
        self.label.create_label(parent, text="Generate your thoughts out loud", pady=(0, 15), font=("Helvetica", 12, "italic"))
        self.button.create_button(parent, text="Change TTS", command=change_tts, pady=10)
        usage_label = self.label.create_label(parent=parent, text=self.user.get_usage(), pady=10)
        status_label = self.entry.create_entry(parent=parent, pady=10, width=30)
        status_label.insert(0, "Status: OK")
        text_entry = self.text_entry.create_text_entry(parent=parent, height=10, width=50, pady=10)

        button_frame = tk.Frame(parent)
        button_frame.pack(pady=10)

        self.button.create_button(button_frame, text="Generate Audio", command=generate_command, pady=10).pack(side="left", padx=5)
        self.button.create_button(button_frame, text="Play", command=lambda: self.voice.play_audio(self.output_file_name), pady=10).pack(side="left", padx=5)
        self.button.create_button(button_frame, text="Stop", command=lambda: self.voice.stop_audio, pady=10).pack(side="left", padx=5)
