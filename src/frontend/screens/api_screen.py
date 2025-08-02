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
        if self.client.is_valid_key(api_key_entry.get()):
            api_key = api_key_entry.get()
            self.client.set_api_key(api_key)
            self.client.set_client()
            root.destroy()
            self.main_screen()
        else:
            api_key_entry.delete(0, tk.END)
            api_key_entry.insert(0, "Invalid API Key.")

    def display_screen(self):
        root = tk.Tk()
        root.resizable(False, False)
        root.title("API Key Required")

        frame = tk.Frame(root, padx=20, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        self.label.create_label(frame, text="ThinkAloud", pady=(10, 2), font=("Helvetica", 20, "bold"))
        self.label.create_label(frame, text="Generate your thoughts out loud", pady=(0, 15), font=("Helvetica", 12, "italic"))
        self.label.create_label(frame, text="Enter Elevenlabs API Key:", pady=10)
        api_key_entry = self.entry.create_entry(frame, pady=10)

        self.button.create_button(frame, text="Submit", command=lambda: self.on_submit(root, api_key_entry), pady=10)

        root.mainloop()
