# Voice Assistant

A simple Python-based voice assistant that recognizes voice commands and performs various tasks like opening applications, playing music, and searching the web.

## Features
- Voice recognition using `speech_recognition`.
- Text-to-speech response using `pyttsx3`.
- Opens web browser and performs Google searches.
- Retrieves current time and date.
- Opens Microsoft Word, Excel, and PowerPoint.
- Plays music from a specified directory.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install speechrecognition pyttsx3
```

## Usage
Run the script and speak commands such as:
- "Open browser"
- "Search for Python tutorials"
- "What's the time?"
- "Open Word"
- "Play music"

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd voice-assistant
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python assistant.py
   ```

## Customization
- Update `music_dir` to the correct path for your music folder.
- Modify application paths (Word, Excel, PowerPoint) if necessary.

## License
This project is licensed under the MIT License.

