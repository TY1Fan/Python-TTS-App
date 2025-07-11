import tkinter as tk

class TextEntry:
    def __init__(self):
        None

    def create_text_entry(self, parent, height, width, pady):
        text = tk.Text(parent, height=height, width=width)
        text.pack(pady=pady)
        return text