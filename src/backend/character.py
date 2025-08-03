from backend.client import Client

class Character(Client):

    def __init__(self, client_name):
        super().__init__(client_name=client_name)

    def get_char_names(self, engine='standard', language_code=""):
        if self.client_name == "ElevenLabs":
            response = self.client.voices.get_all()
            characters = response.voices

            char_names = [char.name for char in characters]

            print(char_names)
            return char_names
        elif self.client_name == "AWS":
            response = self.client.describe_voices(
                Engine=engine,
                # LanguageCode=language_code,
            )
            characters = response['Voices']
            char_names = [char['Name'] for char in characters]

            print(char_names)
            return char_names
    
    def get_char_name_id_map(self):
        if self.client_name == "ElevenLabs":
            response = self.client.voices.get_all()
            characters = response.voices
            return {char.name: char.voice_id for char in characters}
        elif self.client_name == "AWS":
            response = self.client.describe_voices(
                Engine='standard',
            )
            characters = response['Voices']
            return {char['Name']: char['Id'] for char in characters}

    def get_char_id(self, char_name):
        char_map = self.get_char_name_id_map()
        return char_map.get(char_name)
