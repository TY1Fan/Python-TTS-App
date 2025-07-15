import tkinter as tk

class Entry:
    def __init__(self):
        None

    def create_entry(self, parent, pady, width=20):
        entry = tk.Entry(parent, width=width)
        entry.pack(pady=pady)
        return entry
    
