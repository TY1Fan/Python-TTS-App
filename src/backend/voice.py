import sys
import pygame
import os
import datetime
import shutil

from backend.character import Character
from elevenlabs import VoiceSettings

class Voice(Character):

    def __init__(self, client_name):
        super().__init__(client_name=client_name)

    def generate_audio_from_text(self, model_id, voice_id, text, output_file, settings=None, text_type="text", lang=None):
        try:
            if self.client_name == "ElevenLabs":
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
            elif self.client_name == "AWS":
                audio = self.client.synthesize_speech(
                    Engine=model_id,
                    LanguageCode=lang,
                    OutputFormat='mp3',
                    Text=text,
                    TextType=text_type,
                    VoiceId=voice_id,
                )
                with open(output_file, "wb") as f:
                    for chunk in audio["AudioStream"]:
                        f.write(chunk)

                self.save_to_aws(output_file, voice_id)

            return "Audio generated successfully"           
        except Exception as e:
            print(f"Error generating audio: {e}")
            return "Error generating audio"

    def save_to_aws(self, output_file, voice_id):

        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            current_file = os.path.abspath(__file__)
            base_dir = os.path.dirname(os.path.dirname(current_file))

        audio_folder = os.path.join(base_dir, "aws_audio")
        voice_name = voice_id.lower()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%S")
        
        # Create the directory structure if it doesn't exist
        history_dir = os.path.join(audio_folder, voice_name)
        os.makedirs(history_dir, exist_ok=True)
        
        # Create the history filename with timestamp
        history_filename = f"{timestamp}_{voice_name}.mp3"
        history_path = os.path.join(history_dir, history_filename)
        
        # Copy the generated audio file to the history folder
        shutil.copy2(output_file, history_path)
        print(f"Audio saved to history: {history_path}")

    def get_voice_settings(self, character_id):
        if self.client_name == "ElevenLabs":
            settings = self.client.voices.settings.get(voice_id=character_id)
            print(settings)
            return settings
        elif self.client_name == "AWS":
            print("AWS does not support voice settings retrieval in this implementation.")

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
    


