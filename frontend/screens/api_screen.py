import tkinter as tk

class Api_Screen:
    
    def __init__(self, client):
        self.client = client

    def on_submit(self):
        api_key = self.api_key_entry.get()
        self.client.set_api_key(api_key)

    def display_screen(self):
        self.root = tk.Tk()
        self.root.title("API Key Required")

        self.label = tk.Label(self.root, text="Enter Elevenlabs API Key:")
        self.label.pack(pady=10)

        self.api_key_entry = tk.Entry(self.root)
        self.api_key_entry.pack(pady=10)

        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)
