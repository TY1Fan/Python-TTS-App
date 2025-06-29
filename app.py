import backend
import os
import pygame
import tkinter as tk

from tkinter import ttk

# Check for api key
if not os.path.isfile(".env"):
    root = tk.Tk()
    root.title("API Key Required")

    # Prompt user to enter the API key
    label = tk.Label(root, text="Enter Elevenlabs API Key:")
    label.pack(pady=10)

    api_key_entry = tk.Entry(root)
    api_key_entry.pack(pady=10)

    def on_submit():
        api_key = api_key_entry.get()
        # if api_key:
        backend.save_api_key(api_key)
        backend.client = backend.get_client()
        root.destroy()
        # else:
            # tk.messagebox.showerror("Error", "API Key cannot be empty.")

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

# Initialize the main window
window = tk.Tk()

# Set title of GUI
window.title("Python TTS App")

# Label to display character usage
label = ttk.Label(window, text=backend.get_usage())
label.pack(pady=10)

window.mainloop()