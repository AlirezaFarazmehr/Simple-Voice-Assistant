import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import random
import subprocess

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query
        except Exception as e:
            print(e)
            return None


def play_music():
    music_dir = '/path/to/your/music/folder'  # Replace with your music directory
    music_files = os.listdir(music_dir)
    random_music = random.choice(music_files)
    os.startfile(os.path.join(music_dir, random_music))


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")  # Format: 12-hour time with AM/PM
    return current_time


def get_current_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")  # Format: Monday, January 01, 2023
    return current_date


def open_word():
    try:
        subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'])  # Adjust the path as per your Word installation path
        speak("Opening Microsoft Word")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open Microsoft Word")


def open_excel():
    try:
        subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'])  # Adjust the path as per your Excel installation path
        speak("Opening Microsoft Excel")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open Microsoft Excel")


def open_powerpoint():
    try:
        subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'])  # Adjust the path as per your PowerPoint installation path
        speak("Opening Microsoft PowerPoint")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open Microsoft PowerPoint")


def open_file(filename):
    try:
        os.startfile(filename)
        speak(f"Opening {filename}")
    except Exception as e:
        print(e)
        speak(f"Sorry, I couldn't open {filename}")


def main():
    speak("Hello! How can I help you?")
    while True:
        query = listen()
        if query:
            if "what's your name" in query:
                speak("My name is Cortana.")
            elif "who are you" in query:
                speak("I am your virtual assistant.")
            elif "open browser" in query or "Launch browser" in query:
                speak("Opening browser")
                webbrowser.open('http://www.google.com')  # Opens the default web browser to Google's homepage
            elif "search for" in query:
                search_query = query.split("search for", 1)[1].strip()
                speak(f"Searching for {search_query}")
                search_url = f"http://www.google.com/search?q={search_query}"
                webbrowser.open(search_url)
            elif "play music" in query:
                speak("Playing music")
                play_music()
            elif "what's the time" in query or "what time is it" in query:
                current_time = get_current_time()
                speak(f"The current time is {current_time}")
            elif "what's today's date" in query or "what day is it" in query:
                current_date = get_current_date()
                speak(f"Today's date is {current_date}")
            elif "open Word" in query:
                open_word()
            elif "open Excel" in query:
                open_excel()
            elif "open PowerPoint" in query:
                open_powerpoint()
            elif "open file" in query:
                filename = query.split("open file", 1)[1].strip()
                open_file(filename)
            elif "goodbye" in query or "bye bye" in query:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
