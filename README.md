# File Reader with Text-to-Speech

This Python project is a command-line tool that reads text files and converts the content into speech using the Google Text-to-Speech (gTTS) library and Pygame for audio playback. It supports multiple languages (currently Arabic and English).

## Features

- Reads text from a file provided by the user.
- Converts the text into speech using the `gTTS` library.
- Plays the generated speech audio using `pygame`.
- Supports multilingual text-to-speech (e.g., Arabic and English).
- Handles temporary audio file generation and cleanup automatically.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `gTTS`
  - `pygame`

Install the required libraries using pip:

```bash
pip install gtts pygame
