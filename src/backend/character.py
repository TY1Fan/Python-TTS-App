from backend.client import Client

class Character(Client):

    def __init__(self):
        super().__init__()

    def get_char_names(self):
        response = self.client.voices.get_all()
        characters = response.voices

        char_names = [char.name for char in characters]

        print(char_names)
        return char_names
    
    def get_char_name_id_map(self):
        response = self.client.voices.get_all()
        characters = response.voices
        return {char.name: char.voice_id for char in characters}
    
    def get_char_id(self, char_name):
        char_map = self.get_char_name_id_map()
        return char_map.get(char_name)