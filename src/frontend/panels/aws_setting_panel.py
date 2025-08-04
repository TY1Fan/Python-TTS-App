import tkinter as tk

from frontend.components.label import Label
from frontend.components.button import Button
from frontend.components.dropdown import Dropdown
from frontend.components.slider import Slider
from frontend.components.checkbutton import Checkbutton

class AWS_Settings_Panel:

    def __init__(self, client, voice, character):
        self.client = client
        self.character = character
        self.voice = voice
        self.label = Label()
        self.button = Button()
        self.dropdown = Dropdown()
        self.slider = Slider()
        self.checkbutton = Checkbutton()

    def display_panel(self, parent):

        self.selected_region_name = tk.StringVar()
        self.selected_engine_name = tk.StringVar()
        self.selected_lang_name = tk.StringVar()
        self.selected_char_name = tk.StringVar()

        self.label.create_label(parent, "Select AWS Region:", pady=10)
        self.region_dropdown = self.dropdown.create_dropdown(
            parent, 
            values=self.client.get_region(),
            textvariable=self.selected_region_name, pady=10
        )

        engine = self.client.get_engines(self.selected_region_name.get())
        self.label.create_label(parent, "Select Engine:", pady=10)
        self.engine_dropdown = self.dropdown.create_dropdown(
            parent, 
            values=engine,
            textvariable=self.selected_engine_name, pady=10
        )

        lang_name = self.character.get_lang_name(region=self.selected_region_name.get(), engine=self.selected_engine_name.get().lower())
        self.label.create_label(parent, "Select Language Code:", pady=10)
        self.language_code_dropdown = self.dropdown.create_dropdown(
            parent, 
            values=lang_name,
            textvariable=self.selected_lang_name, pady=10
        )

        lang_code = self.character.get_lang_code(
            self.selected_region_name.get(), 
            self.selected_engine_name.get().lower(),
            self.selected_lang_name.get()
        )
        char_names = self.character.get_char_names(
            engine=self.selected_engine_name.get().lower(),
            language_code=lang_code
        )
        self.label.create_label(parent, "Select Character:", pady=10)
        self.char_dropdown = self.dropdown.create_dropdown(
            parent, 
            values=char_names,
            textvariable=self.selected_char_name, pady=10
        )
    
    def get_char_id(self):
        print(self.selected_char_name.get())
        return self.character.get_char_id(
            self.selected_char_name.get(),
            self.selected_engine_name.get().lower(),
            self.selected_lang_name.get()
        )






        
