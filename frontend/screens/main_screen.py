import tkinter as tk

from frontend.components.label import Label
from frontend.components.entry import Entry
from frontend.components.button import Button
from frontend.components.textentry import TextEntry
from frontend.panels.settings_panel import Settings_Panel

class Main_Screen:

    output_file_name = "output.mp3"

    def __init__(self, client, user, voice, character):
        self.client = client
        self.user = user
        self.character = character
        self.voice = voice
        self.label = Label()
        self.entry = Entry()
        self.button = Button()
        self.text_entry = TextEntry()
        self.settings_card = Settings_Panel(client, voice, character)

    def display_screen(self):
        root = tk.Tk()
        root.title("Python TTS App")

        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, padx=10, pady=10)
        left_frame.pack(side="left", fill=tk.Y)

        separator = tk.Frame(main_frame, width=2, bg="gray")
        separator.pack(side="left", fill=tk.Y)

        right_frame = tk.Frame(main_frame, padx=20, pady=20)
        right_frame.pack(side="left", fill=tk.BOTH, expand=True)

        self.settings_card.display_card(right_frame)

        char_id = self.settings_card.get_char_id
        generate_command = lambda: self.voice.generate_audio_from_text(
            text = text_entry.get("1.0", tk.END).strip(), 
            voice_id = char_id(),
            output_file = self.output_file_name,
            model_id = "eleven_multilingual_v2",
            settings = self.voice.get_voice_settings(character_id=char_id())
        )
        
        self.label.create_label(parent=left_frame, text=self.user.get_usage(), pady=10)
        self.button.create_button(left_frame, text="Generate Audio", command=generate_command, pady=10)
        self.button.create_button(left_frame, text="Play", command=lambda: self.voice.play_audio(self.output_file_name), pady=10)    
        self.button.create_button(left_frame, text="Stop", command=lambda: self.voice.stop_audio(), pady=10)
        text_entry = self.text_entry.create_text_entry(parent=left_frame, height=5, width=50, pady=10)

        root.mainloop()