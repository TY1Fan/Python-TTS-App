import tkinter as tk

class Listbox:
    def __init__(self):
        None
    
    def create_listbox(self, parent, padx, pady, height, exportselection=False):
        listbox = tk.Listbox(parent, height=height, exportselection=exportselection)
        listbox.pack(padx=padx, pady=pady)
        return listbox
    
    def insert_items(self, listbox, items):
        for item in items:
            listbox.insert(tk.END, item)