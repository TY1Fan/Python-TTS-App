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
        self.label.create_label(parent, "Select Language:", pady=10)
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

        self.selected_region_name.trace_add("write", self.on_region_change)
        self.selected_engine_name.trace_add("write", self.on_engine_change)
        self.selected_lang_name.trace_add("write", self.on_language_change)

        self.use_ssml_var = tk.BooleanVar()
        self.checkbutton.create_checkbox(parent, text="Use SSML Syntax", var=self.use_ssml_var, pady=5)

    def on_region_change(self, *args):
        region = self.selected_region_name.get()
        engines = self.client.get_engines(region)
        self.engine_dropdown['values'] = engines
        if engines:
            self.selected_engine_name.set(engines[0])

    def on_engine_change(self, *args):
        region = self.selected_region_name.get()
        engine = self.selected_engine_name.get().lower()
        languages = self.character.get_lang_name(region=region, engine=engine)
        self.language_code_dropdown['values'] = languages
        if languages:
            self.selected_lang_name.set(languages[0])

    def on_language_change(self, *args):
        region = self.selected_region_name.get()
        engine = self.selected_engine_name.get().lower()
        language_name = self.selected_lang_name.get()
        lang_code = self.character.get_lang_code(region, engine, language_name)
        characters = self.character.get_char_names(engine=engine, language_code=lang_code)
        self.char_dropdown['values'] = characters
        if characters:
            self.selected_char_name.set(characters[0])

    
    def get_char_id(self):
        print(self.selected_char_name.get())
        return self.character.get_char_id(
            self.selected_char_name.get(),
            self.selected_engine_name.get().lower(),
            self.get_lang_code()
        )
    
    def get_text_type(self):
        if self.use_ssml_var.get():
            return "ssml"
        else:
            return "text"
        
    def get_engine(self):
        return self.selected_engine_name.get().lower()
    
    def get_lang_code(self):
        code = self.character.get_lang_code(
            self.selected_region_name.get(),
            self.selected_engine_name.get().lower(),
            self.selected_lang_name.get()
        )
        print(code)
        return code






        
