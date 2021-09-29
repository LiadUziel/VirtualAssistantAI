import speech_recognition as sr
import pyttsx3  # Computer voice
import pywhatkit  # Search in youtube
import wikipedia  # Search in wikipedia
import pyjokes
import datetime

import sys
import webbrowser

chrome_path = "C:/Program  Files (x86)/Google/Chrome/Application/chrome.exe %s"

playing = True

engine = pyttsx3.init()  # Initial text to speech

# Initial Voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # 0 - male, 1 - female


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening for you...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("User said: " + command + '\n')

            if "alexa" in command:  # Output just if say "alexa"
                command = command.replace("alexa", "")  # Remove 'Alexa' from command
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return command


def run_assistant():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", '')
        print(song)
        talk("playing" + song)
        pywhatkit.playonyt(song)  # open youtube

    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M')  # ('%I:%M %p) for AM
        print(time)
        talk("Current time is " + time)

    elif "wikipedia" in command:  # 'who the heck' 'wiki' 'info'
        value_wiki = command.replace("wikipedia", '')
        info = wikipedia.summary(value_wiki, 1)  # 1 is number of lines
        print(info)
        talk(info)

    elif "date" in command:
        print("I don't want you")
        talk("I don't want you")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "open google" in command:
        print("Opening google")
        talk("Opening google")
        webbrowser.get(chrome_path).open("google.com")

    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        talk("User asked to Locate" + location)
        map_string = ' '.join(sys.argv[1:])
        print(map_string)
        webbrowser.get(chrome_path).open('https://www.google.com/maps/place/' + map_string)
        # webbrowser.get(chrome_path).open("https://www.google.nl / maps / place/" + location + "")

    elif "logout" in command or "exit" in command:
        print("Good bye")
        talk("Good bye")
        exit(1)

    else:
        print("Please say the command again")
        talk("Please say the command again")


def start():
    while True:
        run_assistant()


if __name__ == "__main__":
    start()
