import tkinter as tk

class Label:
    def __init__(self):
        None
    
    def create_label(self, parent, text, pady, font=None):
        label = tk.Label(parent, text=text, font=font)
        label.pack(pady=pady)
        return label
