import tkinter as tk

from frontend.components.label import Label
from frontend.components.button import Button
from frontend.components.dropdown import Dropdown
from frontend.components.slider import Slider
from frontend.components.checkbutton import Checkbutton

class Settings_Panel:

    def __init__(self, client, voice, character):
        self.client = client
        self.character = character
        self.voice = voice
        self.label = Label()
        self.button = Button()
        self.dropdown = Dropdown()
        self.slider = Slider()
        self.checkbutton = Checkbutton()

    def display_card(self, parent):

        char_names = self.character.get_char_names()
        self.selected_char_name = tk.StringVar()
        
        self.dropdown.create_dropdown(parent=parent, values=char_names, textvariable=self.selected_char_name, pady=10)
        settings = self.voice.get_voice_settings(character_id=self.get_char_id())

        settings_config = {
            "stability": (0.0, 1.0, settings.stability),
            "similarity_boost": (0.0, 1.0, settings.similarity_boost),
            "style": (0.0, 1.0, settings.style),
            "speed": (0.7, 1.2, settings.speed)
        }

        self.slider_values = {}

        for name, (min_val, max_val, initial_val) in settings_config.items():
            var = self.slider.create_slider(
                parent=parent,
                name=name,
                from_=min_val,
                to=max_val,
                initial=initial_val,
                resolution=0.01,
            )
            self.slider_values[name] = var

        self.use_boost_var = tk.BooleanVar(value=settings.use_speaker_boost)
        self.checkbutton.create_checkbox(parent, text="Use Speaker Boost", var=self.use_boost_var, pady=5)

        self.button.create_button(
            parent,
            text="Save Settings",
            command=lambda: self.voice.update_voice_settings(
                self.get_char_id(),
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

    def get_char_id(self):
        print(self.selected_char_name.get())
        return self.character.get_char_id(self.selected_char_name.get())
