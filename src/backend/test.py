from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs(
  api_key='YOUR_API_KEY',
).usage.get(
    start_unix=1,
    end_unix=1,
)
print(elevenlabs)