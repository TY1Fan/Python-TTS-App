import tkinter as tk

from frontend.components.label import Label
from frontend.components.entry import Entry
from frontend.components.button import Button
from frontend.components.textentry import TextEntry
from frontend.components.dropdown import Dropdown
from frontend.components.slider import Slider
from frontend.components.checkbutton import Checkbutton

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
        self.dropdown = Dropdown()
        self.slider = Slider()
        self.checkbutton = Checkbutton()

    def display_screen(self):
        root = tk.Tk()
        root.title("Python TTS App")

        char_names = self.character.get_char_names()
        char_id = lambda: self.character.get_char_id(self.dropdown.widget.get())
        generate_command = lambda: self.voice.generate_audio_from_text(
            text = text_entry.get("1.0", tk.END).strip(), 
            voice_id = char_id(),
            output_file = self.output_file_name,
            model_id = "eleven_multilingual_v2",
            settings = self.voice.get_voice_settings(character_id=char_id())
        )
        
        self.label.create_label(parent=root, text=self.user.get_usage(), pady=10)
        self.button.create_button(root, text="Generate Audio", command=generate_command, pady=10)
        self.dropdown.create_dropdown(parent=root, values=char_names, pady=10)
        settings = self.voice.get_voice_settings(character_id=char_id())

        settings_config = {
            "stability": (0.0, 1.0, settings.stability),
            "similarity_boost": (0.0, 1.0, settings.similarity_boost),
            "style": (0.0, 1.0, settings.style),
            "speed": (0.7, 1.2, settings.speed)
        }

        self.slider_values = {}

        for name, (min_val, max_val, initial_val) in settings_config.items():
            var = self.slider.create_slider(
                parent=root,
                name=name,
                from_=min_val,
                to=max_val,
                initial=initial_val,
                resolution=0.01,
            )
            self.slider_values[name] = var

        self.use_boost_var = tk.BooleanVar(value=settings.use_speaker_boost)
        self.checkbutton.create_checkbox(root, text="Use Speaker Boost", var=self.use_boost_var, pady=5)

        self.button.create_button(
            root,
            text="Save Settings",
            command=lambda: self.voice.update_voice_settings(
                char_id(),
                {
                    "stability": self.slider_values["stability"].get(),
                    "similarity_boost": self.slider_values["similarity_boost"].get(),
                    "style": self.slider_values["style"].get(),
                    "speed": self.slider_values["speed"].get(),
                    "use_speaker_boost": self.use_boost_var.get()
                }
            ),
            pady=10
        )

        self.button.create_button(root, text="Play", command=lambda: self.voice.play_audio(self.output_file_name), pady=10)    
        self.button.create_button(root, text="Stop", command=lambda: self.voice.stop_audio(), pady=10)
        text_entry = self.text_entry.create_text_entry(parent=root, height=5, width=50, pady=10)

        root.mainloop()