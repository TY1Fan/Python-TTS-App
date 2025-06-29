# Python-TTS-App

## Acknowledgement
The audio in this application was generated using ElevenLabs.\
Learn more at https://www.elevenlabs.io

Frontend inspired by this youtube tutorial: https://www.youtube.com/watch?v=aiC8K90MhgA&t=417s

## User Guide:
1. Sign up for a free Elevenlabs account [here](https://elevenlabs.io/app/sign-up)
1. Follow this [video](https://www.youtube.com/watch?v=BqJyiNFE9pA) to generate a API token. Copy the API token into a notepad as you will need it later
1. Download the .exe file [here](https://github.com/TY1Fan/Python-TTS-App/releases). Read the release guide to download the correct file.
1. For MacOS, on first launch of the app, you will likely face this error `Apple could not verify “app” is free of malware that may harm your Mac or compromise your privacy.`
1. To resolve this, press `done`. Then open System Settings > Privacy & Security. Scroll to the bottom and click `Open Anyway`.
1. Double click on the .exe file to run it. First launch will take some time.
1. On first launch, you will be prompted to insert your API token.
1. After hitting the submit button, the API token window will close. The TTS App will show.
1. Within the app, you should be able to see remaining character display at the top of the window.
1. There is a text box to input text.
1. Generate audio button to generate MP3 audio file.
1. Play button to play the audio file.
1. Stop button to stop the audio file.

## For Developers:

### Environment:
- Python version used: Python 3.12.1
- TTS Service used: ElevenLabs

### Steps to reproduce:
1. Create a virtual environment by running `python -m venv venv`
1. Activate the virtual environment by running `source venv/bin/activate`
1. Install the requirements by running `pip install -r requirements.txt`
1. Paste your ELEVENLABS_API_KEY in the `.env` file.
1. Run the `main` script to generate an audio by running `python main.py`

### ElevenLabs API:
To generate API key from ElevenLabs, please refer to this [video](https://www.youtube.com/watch?v=BqJyiNFE9pA).

### Important Notes:
- No billing information (i.e. credit card) is required for ElevenLabs if you choose the free tier.
- 10,000 tokens issued per month for free tier.

### Resources:
- API Documentation: https://elevenlabs.io/docs/api-reference/introduction
- YouTube: https://www.youtube.com/watch?v=ECBmgtxd_Zk&t=774s