import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import sys
import os
import random
import pygame
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from termcolor import colored
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

console = Console()
def speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic_source:
        print("Ready to listen... 🎤\n")
        try:
            recognizer.adjust_for_ambient_noise(mic_source, duration=0.5)
            audio_input = recognizer.listen(mic_source, timeout=2)  # Set the timeout value (in seconds)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.\n")
            return

    try:
        user_command = recognizer.recognize_google(audio_input)
        user_command = user_command.lower()
        user_prefix = f'{name.upper()} : '
        user_print = user_prefix+user_command

        # Choose the colors you want for the text
        user_prefix_colored = colored(user_prefix, 'white','on_blue')
        user_command_colored = colored(user_command, 'white','on_blue',['bold'])
        user_print_colored = colored(user_print, 'white','on_blue',['bold'])
        # Combine the colored components back into the formatted text
        formatted_text_colored = f"{user_print_colored}".rjust(130)

        print(formatted_text_colored,"\n")
        command_processing(user_command)

    except sr.UnknownValueError:
        print("\nApologies, I couldn't comprehend that. 🤔\n")
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")

def play_random_music(music_dir):
    pygame.mixer.init()
    
    # Get a list of music files in the directory
    songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav'))]

    if not songs:
        speak("No music files found in the directory.")
        return

    # Select a random music file
    random_song = os.path.join(music_dir, random.choice(songs))

    speak(f"Now playing")
    
    # Load and play the selected music file
    pygame.mixer.music.load(random_song)
    pygame.mixer.music.play()
    speak("Say 'stop music' to stop the music.")


def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")

def command_processing(user_command):
    query = user_command.lower()
    
    if 'hello' in user_command:
        text = "Hi ," + name + ". I am Chitti the robot. Speed 1 terahertz, memory 1 zigabyte."
        speak(text)
    
    elif 'how are you' in user_command:
        speak("I don't feel anything as I am a robot. But I am fine. Thank you for asking.")
    
    elif 'what time is it' in user_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It is " + time)
    
    elif 'date' in user_command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today is " + date)
    
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        speak(results)
    
    elif 'play music' in query or 'play song' in query:
        speak("Here you go with music")
        music_dir = r"C:\Users\indhu\OneDrive\Documents\oasis\music"
        play_random_music(music_dir)
    
    elif 'stop music' in query:
        stop_music()
    
    elif 'quit' in user_command:
        quit_text = "See you later " + name + "! Exiting now."
        speak(quit_text)
        sys.exit()
    
    elif 'command list' in user_command:
        speak("This how you can interact with me.")
        print("1. Hello")
        print("2. How are you?")
        print("3. What time is it?")
        print("4. What is today's date?")
        print("5. Search Wikipedia for [query]")
        print("6. Play music")
        print("7. Stop music")
        print("8. Quit")
        
    else:
        engine.say("Sorry, I couldn't understand that.")
        print("Sorry, I couldn't understand that.")
        engine.runAndWait()


def speak(text):
    chitti_text = f'CHITTI: {text}\n'
    

    styled_chitti_text = Text(chitti_text, style="bold white on #0d0056")
    

    console.print(styled_chitti_text)
    
    engine.say(text)
    engine.runAndWait()



print("\n")
print("                      ▒█▀▀█ ▒█░▒█ ▀█▀ ▀▀█▀▀ ▀▀█▀▀ ▀█▀ 　 ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀")
time.sleep(0.8)
print("                      ▒█░░░ ▒█▀▀█ ▒█░ ░▒█░░ ░▒█░░ ▒█░ 　 ░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█▄▄▀ ▒█░░▒█ ▒█▀▀▄ ▒█░░▒█ ░▒█░░")
time.sleep(0.8)
print("                      ▒█▄▄█ ▒█░▒█ ▄█▄ ░▒█░░ ░▒█░░ ▄█▄ 　 ░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░")
print("\n")
heading_text = "Speed 1 terahertz, memory 1 zigabyte."
heading_panel = Panel(Text(heading_text, style="bold blue", justify="center"), width=150)
console.print(heading_panel)


name = input("What is your name? \n")
while True:
    speech_recognition()