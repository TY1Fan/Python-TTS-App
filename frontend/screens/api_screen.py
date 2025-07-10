import tkinter as tk

from frontend.components.label import Label
from frontend.components.entry import Entry
from frontend.components.button import Button

class Api_Screen:

    def __init__(self, client, main_screen):
        self.client = client
        self.main_screen = main_screen
        self.label = Label()
        self.entry = Entry()
        self.button = Button()

    def on_submit(self, root, api_key_entry):
        api_key = api_key_entry.get()
        self.client.set_api_key(api_key)
        self.client.set_client()
        root.destroy()
        self.main_screen()

    def display_screen(self):
        root = tk.Tk()
        root.title("API Key Required")

        self.label.create_label(parent=root, text="Enter Elevenlabs API Key:", pady=10)
        api_key_entry = self.entry.create_entry(parent=root, pady=10)

        self.button.create_button(parent=root, text="Submit", command=lambda: self.on_submit(root, api_key_entry), pady=10)

        root.mainloop()
        return self.client
