import tkinter as tk

class Api_Screen:
    
    def __init__(self, client, function):
        self.client = client
        self.function = function

    def display_screen(self):
        root = tk.Tk()
        root.title("API Key Required")

        label = tk.Label(root, text="Enter Elevenlabs API Key:")
        label.pack(pady=10)

        api_key_entry = tk.Entry(root)
        api_key_entry.pack(pady=10)

        def on_submit():
            api_key = api_key_entry.get()
            self.client.set_api_key(api_key)
            self.client.set_client()
            root.destroy()
            self.function()  # trigger the main window

        submit_button = tk.Button(root, text="Submit", command=on_submit)
        submit_button.pack(pady=10)

        root.mainloop()

        return self.client