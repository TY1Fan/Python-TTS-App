from tkinter import ttk

class Dropdown:
    def __init__(self):
        self.widget = None

    def create_dropdown(self, parent, values, pady):
        self.widget = ttk.Combobox(parent, values=values)
        self.widget.pack(pady=pady)
        self.widget.current(0)
        return self.widget


