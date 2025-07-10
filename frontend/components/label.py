import tkinter as tk

class Label:
    def __init__(self):
        None
    
    def create_label(self, parent, text, pady):
        label = tk.Label(parent, text=text)
        label.pack(pady=pady)
        return label
