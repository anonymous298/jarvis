# import pyttsx3 
# All modules are imported
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit as kit
import time
import os
import pyjokes
import winsound

# creating an engine that will speak
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# creating an speak function that will speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating a function that will take command and turn it to text
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

# creating a timer function that will set a timer
def timer():
    frequency = 2500
    duration = 50

    speak("How much time should i set")

    # it will take secondes from user
    num = takecommand()
    speak('setting timer for' + num + 'seconds')
    print('setting timer for' + num + 'seconds')

    for i in range(int(num),0,-1):
        print(i)
        speak(i)
        winsound.Beep(frequency, duration)

        if i == 1:
            duration = 1500
            winsound.Beep(frequency, duration)

        time.sleep(1)

# this function read tasks from myfile.txt and execute them
def readtask():

    # opens the file
    with open('myfile.txt','r') as a:
        query = a.read()

    # executes the tasks
    # if user calls jarvis then it will execute the if statement
    if 'jarvis' in query or 'hello' in query:
        speak('yes sir what can i do for you')

        # it will take command from user
        while True:
            # exception handling is important
            try:
                
                # it will take command from user
                tasks = takecommand().lower()

                # the commands that user gives will be match here

                # if user says 'nothing' or 'kuch Nahin' or 'bye' then it will exit
                if 'nothing' in tasks or 'kuch Nahin' in tasks or 'bye' in tasks:
                    speak('ok sir i am going to sleep')
                    print("i am going to sleep")
                    break

                elif 'who made you' in tasks or 'who created you' in tasks:
                    speak("I have, been created by, Sir Talha, the greates of all time ")
                    speak("I am a virtual assistant")
                    speak("And my name is Jarvis")

                # it will open instagram
                elif 'open instagram' in tasks:
                    speak('opening instagram')
                    webbrowser.open('https://www.instagram.com/')

                # it will open youtube
                elif 'open youtube' in tasks:
                    speak('opening youtube')
                    webbrowser.open('https://www.youtube.com/')

                elif 'play video' in tasks:
                    speak('what should i play on youtube')
                    myvideo = takecommand().lower()

                    speak('playing' + myvideo)
                    kit.playonyt(myvideo)
                
                # it will open google
                elif 'open google' in tasks:
                    speak('what should i search on google')
                    mysearch = takecommand().lower()

                    speak('opening google')
                    webbrowser.open(f'https://www.google.com/search?q={mysearch}')

                # it will close google
                elif 'close google' in tasks:
                    speak('closing google')
                    os.system('taskkill /f /im chrome.exe')

                # it will open whatsapp
                elif 'open whatsapp' in tasks:
                    speak('opening whatsapp')
                    webbrowser.open('https://web.whatsapp.com/')

                # it will open command prompt
                elif 'open command prompt' in tasks:
                    speak('opening command prompt')
                    os.system('start cmd')

                # it will close command prompt
                elif 'close command prompt' in tasks or 'close cmd' in tasks:
                    speak('closing command prompt')
                    os.system('taskkill /f /im cmd.exe')

                # it will open notepad
                elif 'open notepad' in tasks:
                    speak('opening notepad')
                    os.system('start notepad')

                # it will close notepad
                elif 'close notepad' in tasks:
                    speak('closing notepad')
                    os.system('taskkill /f /im notepad.exe')

                # it will set the timer 
                elif 'timer' in tasks:
                    try:
                        timer()    

                    except Exception as e:
                        print(e)    

                # it will open github
                elif 'open github' in tasks or 'github' in tasks:
                    speak('opening github')
                    webbrowser.open('https://github.com/')

                # it will open stackoverflow
                elif 'open stackoverflow' in tasks or 'stackoverflow' in tasks:
                    speak('opening stackoverflow')
                    webbrowser.open('https://stackoverflow.com/')

                elif 'open vs code' in tasks:
                    speak('opening vscode')
                    os.system('start vscode')
                
                # when the user if else statement works then it will execute this
                # or when the user says anything else then it will execute this
                speak("Sir what should i do for you")
                print("Sir what should i do for you")

            # in case of any error
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to do this task")

def jarvis():
    while True:
        query = takecommand().lower()

        with open('myfile.txt','w') as f:
            f.write(query)

        readtask()

jarvis()