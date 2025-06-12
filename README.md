# Python-TTS-App

## Environment:
- Python version used: Python 3.12.1
- TTS Service used: ElevenLabs

## Steps to reproduce:
1. Create a virtual environment by running `python -m venv venv`
1. Activate the virtual environment by running `source venv/bin/activate`
1. Install the requirements by running `pip install -r requirements.txt`
1. Create a file named `.env` 
1. Create a variable in the `.env` file for ElevenLabs API. Name the variable `ELEVENLABS_API_KEY`.
1. Run the `main` script to generate an audio by running `python main.py`

## ElevenLabs API:
To generate API key from ElevenLabs, please refer to this [video](https://www.youtube.com/watch?v=BqJyiNFE9pA).

## Important Notes:
- No billing information (i.e. credit card) is required for ElevenLabs if you choose the free tier.
- 10,000 tokens issued per month for free tier.

## Resources:
- API Documentation: https://elevenlabs.io/docs/api-reference/introduction
- YouTube: https://www.youtube.com/watch?v=ECBmgtxd_Zk&t=774s