import os
import tkinter as tk

from tkinter import Listbox
from frontend.components.label import Label
from frontend.components.button import Button
from frontend.components.listbox import Listbox

class AWS_History_Panel:
    def __init__(self, user, voice, output_dir="aws_audio"):
        self.user = user
        self.voice = voice
        self.output_dir = output_dir
        self.char_folders = []
        self.audio_files = []
        self.label = Label()
        self.button = Button()
        self.listbox = Listbox()
        self.char_listbox = None
        self.audio_listbox = None

    def refresh(self, parent):
        self.char_folders = [
            d.capitalize() for d in os.listdir(self.output_dir)
            if os.path.isdir(os.path.join(self.output_dir, d))
        ]

        if not self.char_folders:
            print("No audio folders found.")
            return self.char_folders

        if self.char_listbox:
            self.char_listbox.delete(0, tk.END)
            self.listbox.insert_items(self.char_listbox, self.char_folders)
        else:
            self.char_listbox = self.listbox.create_listbox(parent, padx=10, pady=5, height=9)
            self.listbox.insert_items(self.char_listbox, self.char_folders)
            
        if self.audio_listbox:
            self.audio_listbox.delete(0, tk.END)
        else:
            self.audio_listbox = self.listbox.create_listbox(parent, padx=10, pady=5, height=9)
            
        return self.char_folders

    def display_panel(self, parent):
        
        self.label.create_label(parent, text="Select a character:", pady=5)
        self.button.create_button(parent, text="Refresh History", command=lambda: self.refresh(parent), pady=5)
        self.refresh(parent)

        if not self.char_folders:
            self.char_listbox = None 
            return None
        else:
            # ChatGPT-4o used to generate the following code for handling character selection and audio playback:
            def on_voice_select(event):
                selected_index = self.char_listbox.curselection()
                if selected_index:
                    voice_name = self.char_folders[selected_index[0]]
                    folder_path = os.path.join(self.output_dir, voice_name)
                    self.audio_files = [
                        os.path.join(folder_path, f)
                        for f in os.listdir(folder_path)
                    ]
                    self.audio_listbox.delete(0, tk.END)
                    for path in self.audio_files:
                        self.audio_listbox.insert(tk.END, os.path.basename(path))

            self.char_listbox.bind("<<ListboxSelect>>", on_voice_select)

            def on_play():
                selected_index = self.audio_listbox.curselection()
                if selected_index:
                    filepath = self.audio_files[selected_index[0]]
                    self.voice.play_audio(filepath)

            button_frame = tk.Frame(parent)
            button_frame.pack(pady=10)

            self.button.create_button(button_frame, text="Play", command=on_play, pady=5).pack(side="left", padx=5)
            self.button.create_button(button_frame, text="Stop", command=self.voice.stop_audio, pady=5).pack(side="left", padx=5)
            

