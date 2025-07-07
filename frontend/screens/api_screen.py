import tkinter as tk

def api_screen(client):
    root = tk.Tk()
    root.title("API Key Required")

    label = tk.Label(root, text="Enter Elevenlabs API Key:")
    label.pack(pady=10)

    api_key_entry = tk.Entry(root)
    api_key_entry.pack(pady=10)

    def on_submit():
        api_key = api_key_entry.get()
        client.set_api_key(api_key)
        client.set_client()
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()