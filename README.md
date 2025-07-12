# Daisy-desktop-voice-assistant


**Daisy** is a Python-based desktop voice assistant developed as a final project for CS50x and refined during my second year of university. It acts as a virtual assistant that understands voice commands, performs web searches, opens websites and applications, plays music, provides time and date updates, and supports conversational AI interaction.

---

## Features

- **Voice Recognition & Response:** Listens and responds using `pyttsx3` and `SpeechRecognition`.
- **Website Launcher:** Opens predefined or user-added websites via voice commands.
- **Application Launcher:** Starts user-defined desktop applications.
- **Wikipedia Search:** Fetches summaries from Wikipedia.
- **Music Player:** Plays random music from a user-specified directory.
- **Time & Date:** Announces current time and day.
- **Calculator Launcher:** Opens Windows calculator.
- **Conversational Mode:** AI-powered chat mode via `ollama` API.
- **Dynamic Database:** Add websites and applications dynamically.
- **Custom Greetings:** Time-based greetings.
- **Help & Instructions:** Voice-enabled task summary and usage tips.
- **Exit Command:** Graceful shutdown.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages:

  ```bash
  pip install pyttsx3 SpeechRecognition wikipedia ollama

- Windows OS (uses `sapi5` voice engine and `os.startfile()`).
- Microphone access.

## Setup

1. Clone or download the repository.
2. Ensure these files are in the same directory as the script:
   - `sites.txt` — Website list (name, URL)
   - `appPaths.txt` — Application list (name, path)
   - `musicDir.txt` — Path to music folder
3. Edit these text files to match your system paths and preferences.

## Usage Examples

### Open website
- Say: `"Open YouTube"`, `"Open Google"`
### Start application
- Say: `"Start VS Code"`, `"Start Blender"`
### Add website
- Say: `"Add a website"` and follow prompts.
### Add application
- Say: `"Add an app"` and follow prompts.
### Play music
- Say: `"Play music"`
### Get current time
- Say: `"What is the time?"`
### Get today's day
- Say: `"What is the day today?"`
### Search Wikipedia
- Say: `"Search Wikipedia for Albert Einstein"`
### Switch to conversation mode
- Say: `"Conversation mode"`
### Switch back to command mode
- Say: `"Command mode"`
### Exit assistant
- Say: `"Exit"`


## Project Structure

daisy_assistant/
│
├── daisy_assistant.py
├── sites.txt
├── appPaths.txt
├── musicDir.txt
└── README.md

## Notes

- Keep the Python script and data files in the same folder.
- Modify `sites.txt` and `appPaths.txt` either manually or via voice commands.
- Correct any path or URL issues if apps or sites do not launch.
- Avoid duplicate entries in data files.
- Designed primarily for Windows OS.

## Credits

Developed by **Dilshad Ansari** as part of the CS50x final project.

Uses the following libraries and APIs:

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- [Ollama conversational AI](https://ollama.com/)

## License

This project is for educational purposes. Please give proper credit to the original developer, **Dilshad Ansari**, when using or modifying this code.

