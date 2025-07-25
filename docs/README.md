# ThinkAloud User Guide

![Screenshot of UI](./images/UI.png)

## Quick start
1. Sign up for a free Elevenlabs account [here](https://elevenlabs.io/app/sign-up).
1. Follow this [video](https://www.youtube.com/watch?v=BqJyiNFE9pA) to generate a API token. Copy the API token into a notepad as you will need it later.
1. Download the .exe file [here](https://github.com/TY1Fan/Python-TTS-App/releases). Read the release guide to download the correct file.\
![alt text](<./images/mac_issue.png>)
1. For MacOS, on first launch of the app, you will likely face this error `Apple could not verify “app” is free of malware that may harm your Mac or compromise your privacy.`
1. To resolve this, press `done`. Then open System Settings > Privacy & Security. Scroll to the bottom and click `Open Anyway`.
1. Double click on the .exe file to run it. First launch will take some time.\
![Insert your API key here](./images/api.png)
1. On first launch, you will be prompted to insert your API token.
1. After hitting the submit button, the API token window will close. ThinkAloud will show.

## Features:

### Character Usage Count
![Character Count](./images/char_count.png)

Displays the remaining character tokens available based on your subscription tier.

### Audio Generation
![alt text](./images/text_entry.png)

To generate an audio file:
- Enter your thoughts into the text entry box. The text can be in `SSML` format for more life-like speech synthesis.
- Press the `Generate Audio` button to generate an audio file for the text entry.
- Press `Play` to play the audio file generated and `Stop` to stop the audio playback.

**Note:** Pressing `Play` after `Stop` will replay the audio file from the start. I.e. `Stop` is not a pause button.

### Status Bar
![alt text](./images/status.png)

After generating an audio, the status bar will show the status of operation executed.\
The remaining character count display will also update automatically.

### Character Selection
![alt text](./images/char.png)

Select a character from the list of preset characters provided by ElevenLabs.\
On selecting a character, the latest settings configuration of the character will be displayed.

### Settings Configuration
![alt text](./images/config.png)

These are the settings available for configuration:
- Stability: Ranges from 0 (more variation) to 1 (more stable).
- Similarity Boost: Ranges from 0 (low similarity to original voice) to 1 (high similarity to original voice).
- Style: Ranges from 0 (no exaggeration) to 1 (exaggerated style).
- Speed: Ranges from 0.7 (slower) to 1.2 (faster), in comparison to default speed of 1.
- Use Speaker Boost: Boosts the similarity to the original speaker. 

After altering the settings, press on the `Save Settings` button to save the new settings configuration for the selected character.

**Note:** There will be no updates shown on the `status bar`.

### Play Previously Generated Audio
![alt text](./images/history.png)

To play previously generated audio files:
- Select a character. Only character which you had used to generate audio file will be displayed.
- Select an audio file from the character.
- Press on the `Play` button to listen to the audio file.
- Press on the `Stop` button to stop the playback.

**Note:** This panel does not refresh automatically. Hence, press the `Refresh History` button to refresh this panel.

## Known Issues:

1. Feature Flaw: `env.txt` and `history_audio` storage is not in the same directory as the app.\
Description: After you key in your api key when prompted, the `env.txt` file and `history_audio` folder is not saved in the same directory as your app.\
Solution: The `env.txt` and `history_audio` is stored in your system root directory. Hence, if you would like to delete the app, please remember to search and delete the `env.txt` file and `history_audio` in your system.

1. Comestic Bug: `Similarity_boost`\
Description: Currently the similarity boost configurations is labelled as `Similarity_boost`. The underscore is unintended.\
Solution: Currently trying to find a way to remove the underscore without affecting the functionality of the settings panel. Since this bug does not affect the functionality of app, I have decided to backlog for future iterations.

1. Cosmetic Bug: Console launches while using the app.\
Description: When I use the `.exe` file for MacOS, my console launches although I used the flag `--noconsole` while building.\
Solution: Currently trying to find a way to hide the console while my app launches. Since this bug does not affect the functionality of app, I have decided to backlog for future iterations.

## Sources:
```
The audio in this application was generated using ElevenLabs.
Learn more at https://www.elevenlabs.io
``` 