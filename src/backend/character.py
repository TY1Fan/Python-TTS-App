from backend.client import Client

class Character(Client):

    def __init__(self, client_name):
        super().__init__(client_name=client_name)

    def get_char_names(self, engine=None, language_code=None):
        if self.client_name == "ElevenLabs":
            response = self.client.voices.get_all()
            characters = response.voices

            char_names = [char.name for char in characters]

            print(char_names)
            return char_names
        elif self.client_name == "AWS":
            response = self.client.describe_voices(
                Engine=engine,
                LanguageCode=language_code,
            )
            characters = response['Voices']
            char_names = [char['Name'] for char in characters]

            print(char_names)
            return char_names
    
    def get_char_name_id_map(self, engine=None, lang_code=None):
        if self.client_name == "ElevenLabs":
            response = self.client.voices.get_all()
            characters = response.voices
            return {char.name: char.voice_id for char in characters}
        elif self.client_name == "AWS":
            response = self.client.describe_voices(
                Engine=engine,
                LanguageCode=lang_code
            )
            characters = response['Voices']
            return {char['Name']: char['Id'] for char in characters}

    def get_char_id(self, char_name=None, engine=None, lang_code=None):
        if self.client_name == "ElevenLabs":
            char_map = self.get_char_name_id_map()
            return char_map.get(char_name)
        if self.client_name == "AWS":
            char_map = self.get_char_name_id_map(engine=engine, lang_code=lang_code)
            return char_map.get(char_name)
    
    def get_lang_name(self, region, engine):
        self.set_region(region)

        response = self.client.describe_voices(Engine=engine)
        lang_names = []
        for voice in response['Voices']:
            lang_name = voice['LanguageName']
            lang_names.append(lang_name)

        return sorted(lang_names)  
    
    def get_lang_name_id_map(self, region, engine):
        self.set_region(region)
        response = self.client.describe_voices(
            Engine=engine,
        )
        languages = response['Voices']
        return {lang['LanguageName']: lang['LanguageCode'] for lang in languages}
    
    def get_lang_code(self, region, engine, lang_name):
        lang_map = self.get_lang_name_id_map(region, engine)
        return lang_map.get(lang_name)
