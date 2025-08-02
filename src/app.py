import os
import tkinter as tk

from backend.client import Client
from backend.user import User
from backend.voice import Voice
from backend.character import Character
from frontend.screens.api_screen import Api_Screen
from frontend.screens.aws_api_screen import AWS_Api_Screen
from frontend.screens.main_screen import Main_Screen
from frontend.screens.aws_screen import AWS_Screen

def launch_home_screen(client_name):
    client = Client(client_name=client_name)
    user = User(client_name=client_name)
    voice = Voice(client_name=client_name)
    character = Character(client_name=client_name)
    if client_name == "ElevenLabs":
        home_screen = Main_Screen(client, user, voice, character)
        home_screen.display_screen()
    elif client_name == "AWS":
        aws_screen = AWS_Screen(client, user, voice, character)
        aws_screen.display_screen()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Choose TTS Service")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=20, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="ThinkAloud", font=("Helvetica", 20, "bold")).pack()
    tk.Label(frame, text="Generate your thoughts out loud", font=("Helvetica", 12, "italic")).pack()
    tk.Label(frame, text="Select a TTS service to use:", font=("Helvetica", 14, "bold")).pack(pady=(15, 5))

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10, fill="x", padx=20)

    def on_elevenlabs():
        root.destroy()
        client = Client(client_name="ElevenLabs")
        if not os.path.isfile("env.txt"):
            api_screen = Api_Screen(client, lambda:launch_home_screen("ElevenLabs"))
            api_screen.display_screen()
        else:
            if client.is_valid_key(client.credentials.get("ELEVENLABS_API_KEY")):
                launch_home_screen("ElevenLabs")
            else:
                api_screen = Api_Screen(client, lambda:launch_home_screen("ElevenLabs"))
                api_screen.display_screen()

    def on_aws():
        root.destroy()
        client = Client(client_name="AWS")
        if not os.path.isfile("env.txt"):
            api_screen = AWS_Api_Screen(client, lambda:launch_home_screen("AWS"))
            api_screen.display_screen()
        else:
            if client.is_valid_aws_key(client.credentials.get("AWS_ACCESS_KEY_ID"), client.credentials.get("AWS_SECRET_ACCESS_KEY")):
                launch_home_screen("AWS")
            else:
                api_screen = AWS_Api_Screen(client, lambda:launch_home_screen("AWS"))
                api_screen.display_screen()

    tk.Button(btn_frame, text="ElevenLabs", width=15, command=on_elevenlabs).pack(pady=5)
    tk.Button(btn_frame, text="Amazon Polly", width=15, command=on_aws).pack(pady=5)

    root.mainloop()

