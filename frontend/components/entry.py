import tkinter as tk

class Entry:
    def __init__(self):
        None

    def create_entry(self, parent, pady):
        entry = tk.Entry(parent)
        entry.pack(pady=pady)
        return entry
    
