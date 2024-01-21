# import pyttsx3 
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import time
import os
import pyjokes
import winsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        # speak("Say that again please...")
        return "None"

    return query

def timer():
    frequency = 2500
    duration = 200

    speak("How much time should i set")

    num = takecommand()
    speak('setting timer for' + num + 'seconds')
    print('setting timer for' + num + 'seconds')

    for i in range(int(num),0,-1):
        print(i)
        winsound.Beep(frequency, duration)

        if i == 1:
            duration = 1500
            winsound.Beep(frequency, duration)

        time.sleep(1)

def readtask():
    with open('myfile.txt','r') as a:
        query = a.read()


    if 'jarvis' in query or 'hello' in query:
        speak('yes sir what can i do for you')

        while True:

            tasks = takecommand().lower()

            if 'nothing' in tasks or 'kuch Nahin' in tasks or 'bye' in tasks:
                speak('ok sir i am going to sleep')
                print("i am going to sleep")
                break

            elif 'open instagram' in tasks:
                speak('opening instagram')
                webbrowser.open('instagram.com')

            elif 'open youtube' in tasks:
                speak('opening youtube')
                webbrowser.open('youtube.com')

            elif 'open google' in tasks:
                speak("what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f'{cm}')

            elif 'open command prompt' in tasks:
                speak('opening command prompt')
                os.system('start cmd')

            elif 'close command prompt' in tasks or 'close cmd' in tasks:
                speak('closing command prompt')
                os.system('taskkill /f /im cmd.exe')
    
            elif 'timer' in tasks:
                try:
                    timer()    

                except Exception as e:
                    print(e)    

            speak("Sir what should i do for you")
            print("Sir what should i do for you")

def jarvis():
    while True:
        query = takecommand().lower()

        with open('myfile.txt','w') as f:
            f.write(query)

        readtask()

jarvis()
