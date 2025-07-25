import os

from backend.client import Client
from backend.user import User
from backend.voice import Voice
from backend.character import Character
from frontend.screens.api_screen import Api_Screen
from frontend.screens.main_screen import Main_Screen

def launch_home_screen():
    client = Client()
    user = User()
    voice = Voice()
    character = Character()
    home_screen = Main_Screen(client, user, voice, character)
    home_screen.display_screen()
    
if __name__ == "__main__":
    if not os.path.isfile("env.txt"):
        client = Client()
        api_screen = Api_Screen(client, launch_home_screen)
        api_screen.display_screen()
    else:
        launch_home_screen()
