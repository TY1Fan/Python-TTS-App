import tkinter as tk

class Checkbutton:
    def __init__(self):
        None

    def create_checkbox(self, parent, text, var, pady):
        tk.Checkbutton(
            parent,
            text=text,
            variable=var
        ).pack(pady=pady)