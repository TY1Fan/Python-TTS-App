import os

from backend.client import Client
from backend.user import User
from backend.voice import Voice
from backend.character import Character
from frontend.screens.api_screen import Api_Screen
from frontend.screens.main_screen import Main_Screen

client = Client()
user = User()
character = Character()
voice = Voice()
home_screen = Main_Screen(client, user, voice, character)
api_screen = Api_Screen(client, home_screen.display_screen)

if not os.path.isfile(".env"):
    client = api_screen.display_screen()
else:
    home_screen.display_screen()
