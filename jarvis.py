import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import pyjokes
import pywhatkit as kit
import sys
import random
from test import timer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 2
        audio = r.listen(source,10,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except:
        speak("Sorry i did not get it say it again")
        print("Say that again please...")
        return "None"
        
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir talha")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir talha")

    elif hour >= 16 and hour < 20:
        speak("Good Evening sir talha")

    else:
        speak("Good Night sir talha")

    speak("I am Jarvis. How can I help you?")


if __name__ == "__main__":
    wish()

    # while True:
    while True:
        query = takecommand().lower()

        if "open notepad" in query or 'notepad khol do' in query:
            speak("Opening...") 

            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'close notepad' in query or 'notepad band kar do' in query:
            speak("Closing...")

            os.system("taskkill /f /im notepad.exe")

        elif "open minecraft" in query:
            speak("Opening....") 

            npath = "C:\\Users\\TALHA PC\\AppData\\Roaming\\.minecraft"
            os.startfile(npath)

        elif "open command prompt" in query or 'command prompt khol do' in query:
            speak("Opening...") 

            os.system("start cmd")

        elif 'close command prompt' in query or 'command prompt band kar do' in query:
            speak("Closing...")

            os.system("taskkill /f /im cmd.exe")

        elif "open github" in query:
            speak("Opening...")

            os.system('start github')

        elif 'close github' in query:
            speak("Closing...")

            os.system("taskkill /f /im github.exe")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)

            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'play music' in query or 'gana chala do' in query:
            speak("playing music")
            music_dir = 'C:\\Users\\TALHA PC\\OneDrive\\Desktop\\music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "open youtube" in query or 'youtube khol do' in query:
            speak("Opening...") 

            webbrowser.open("youtube.com")


        elif "open instagram" in query or 'instagram khol do' in query:
            speak("Opening...")

            webbrowser.open("instagram.com")

        elif 'open whatsapp' in query or 'whatsapp khol do' in query:
            speak("Opening...")

            webbrowser.open("web.whatsapp.com")

        elif "open google" in query or 'google khol do' in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            javeria = "+923378415773"
            farhan = "+923433071974"

            speak("which person do you want to send message")

            person = takecommand().lower()

            if 'javeria' in person:
                num = javeria
                speak("what message should i send")
                print("listening...")

                msg = takecommand().lower()
                kit.sendwhatmsg_instantly(num, msg, 10, tab_close=True)

            elif 'farhan' in person:
                num = farhan
                speak("what message should i send")
                print("listening...")

                msg = takecommand().lower()
                kit.sendwhatmsg_instantly(num, msg, 10, tab_close=True)

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "restart the system" in query:
            speak("Restarting in")

            for i in range(5,1,-1):
                speak(i)

            os.system('shutdown /r /t 10')

        elif "shutdown the system" in query or 'computer band kar do' in query:
            speak("Shutting down in")

            for i in range(5,1,-1):
                speak(i)

            os.system('shutdown /s /t 10')

        elif "calculator" in query:
            speak("Calculator has been started")
            speak("what operation did you want to start")

            query = takecommand().lower()

            if "addition" in query:
                speak("Enter your first number")
                num1 = takecommand()

                speak("Enter your second number")
                num2 = takecommand()

                sum = num1 + num2
                speak(f"The sum of {num1} and {num2} is {sum}")

            elif "subtraction" in query:
                speak("Enter your first number")
                num1 = takecommand()

                speak("Enter your second number")
                num2 = takecommand()

                sum = num1 - num2
                speak(f"The sum of {num1} and {num2} is {sum}")

            elif "multiplication" in query:
                speak("Enter your first number")
                num1 = takecommand()

                speak("Enter your second number")
                num2 = takecommand()

                sum = num1 * num2
                speak(f"The sum of {num1} and {num2} is {sum}")

            elif "division" in query:
                speak("Enter your first number")
                num1 = takecommand()

                speak("Enter your second number")
                num2 = takecommand()

                sum = num1 / num2
                speak(f"The sum of {num1} and {num2} is {sum}")

        elif 'play video' in query or 'video chala do' in query:
            speak("What video should you want to play")
            print('listening...')
            
            query = takecommand().lower()

            speak('playing...')

            kit.playonyt(query)

        elif "timer" in query:
            speak("Starting...")
            print("Starting...")
            timer()

        elif "bye" in query or 'nothing' in query or 'no thanks' in query:
            speak("Bye sir talha. Have a good day")
            sys.exit()

        speak("Sir, do you have any other work")