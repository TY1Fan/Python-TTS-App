import time

from backend.client import Client

class Voice(Client):

    def __init__(self):
        super().__init__()

    def get_voice_names(self):
        response = self.client.voices.get_all()
        voices = response.voices  # List of Voice objects

        voice_dicts = []

        for voice in voices:
            voice_dicts.append({
                voice.name
            })

        print(voice_dicts)
        return voice_dicts

    def generate_audio_from_text(self, model_id, voice_id, text, output_file, settings):

        start = time.time()

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
    