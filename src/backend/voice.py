import time
import pygame

from backend.character import Character
from elevenlabs import VoiceSettings

class Voice(Character):

    def __init__(self, client_name):
        super().__init__(client_name=client_name)

    def generate_audio_from_text(self, model_id, voice_id, text, output_file, settings):
        try:
            start = time.time()
            print(settings)
            audio = self.client.text_to_speech.convert(
                voice_id=voice_id,
                output_format="mp3_44100_128",
                text=text,
                model_id=model_id,
                voice_settings=settings
            )

            with open(output_file, "wb") as f:
                for chunk in audio:
                    f.write(chunk)

            end = time.time()
            print(f"Audio generated in {end - start:.2f} seconds and saved to {output_file}")
            return "Audio generated successfully"
        except Exception as e:
            print(f"Error generating audio: {e}")
            return "Error generating audio"

    def get_voice_settings(self, character_id):
        settings = self.client.voices.settings.get(voice_id=character_id)
        print(settings)
        return settings
    
    def update_voice_settings(self, character_id, updated_settings):
        print(updated_settings)
        self.client.voices.settings.update(
            voice_id=character_id,
            request=VoiceSettings(
                stability=updated_settings.get("stability"),
                use_speaker_boost=updated_settings.get("use_speaker_boost"),
                similarity_boost=updated_settings.get("similarity_boost"),
                style= updated_settings.get("style"),
                speed= updated_settings.get("speed"),
            ),
        )
        print(f"Settings updated for character ID {character_id}")

    def play_audio(self, output_file_name):
        pygame.mixer.init()
        if output_file_name:
            pygame.mixer.music.load(output_file_name)
            pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()
    


