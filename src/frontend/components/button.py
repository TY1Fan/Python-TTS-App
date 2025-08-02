import tkinter as tk

class Button:
    def __init__(self):
        None

    def create_button(self, parent, text, command, pady):
        button = tk.Button(parent, text=text, command=command)
        button.pack(pady=pady)
        return button
