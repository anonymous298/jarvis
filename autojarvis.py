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
import random
import pyautogui
import requests
from bs4 import BeautifulSoup

# creating an engine that will speak
engine = pyttsx3.init('sapi5')
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
        audio = r.listen(source,phrase_time_limit=5)

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

def wish():
    hour = int(time.strftime("%H"))

    if hour >= 0 and hour < 12:
        speak("Have a Good Morning sir talha")
        print("Have a Good Morning sir talha")

    elif hour >= 12 and hour < 16:
        speak("Have a Good Afternoon sir talha")
        print("Have a Good Afternoon sir talha")

    elif hour >= 16 and hour < 20:
        speak("Have a Good Evening sir talha") 
        print("Have a Good Evening sir talha")

    else:
        speak("Have a Good Night sir talha")
        print("Have a Good Night sir talha")

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0b7e8e50067048a78a648b70ac2b3977'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")

# this function read tasks from myfile.txt and execute them
def readtask():

    # opens the file
    with open('myfile.txt','r') as a:
        query = a.read()

    # executes the tasks
    # if user calls jarvis then it will execute the if statement
    if 'jarvis' in query or 'hello' in query or 'wake up jarvis' in query:
        speak(f'Welcome, sir talha, its {time.strftime("%I:%M %p")}, how can i help you')
        print(f'Welcome, sir talha, its {time.strftime("%I:%M %p")}, how can i help you')

        # it will take command from user
        while True:
            # exception handling is important
            try:
                
                # it will take command from user
                tasks = takecommand().lower()

                # the commands that user gives will be match here

                # if user says 'nothing' or 'kuch Nahin' or 'bye' then it will exit
                if 'nothing' in tasks or 'kuch Nahin' in tasks or 'bye' in tasks or 'you can sleep now' in tasks:
                    print("i am going to sleep")
                    speak('ok sir i am going to sleep, wake me up when you need me')
                    wish()
                    break

                # it will tell you name of the creator of jarvis
                elif 'who made you' in tasks or 'who created you' in tasks:
                    speak("I have, been created by, Sir Talha, the ,greates,of ,all ,time ")
                    speak("I am a virtual assistant")
                    speak("And my name is Jarvis")

                # it will tell you about yourself
                elif 'how are you' in tasks:
                    speak("I am fine, what about you")
                    user = takecommand()

                    if 'good' in user or 'fine' in user:
                        speak("that's great")
                        print("that's great")
                    
                    elif 'bad' in user or 'sad' in user:
                        speak("that's too bad")
                        print("that's too bad")

                        speak('do you want to listen to some jokes')

                        um = takecommand()

                        if 'yes' in um or 'sure' in um:
                            jokes = pyjokes.get_joke()
                            print(jokes)
                            speak(jokes)

                        elif 'no' in um:
                            speak('ok no problem')

                # it will tell time
                elif 'tell me the time' in tasks or 'time' in tasks:
                    t = time.strftime("%I:%M %p")
                    print(t)
                    speak(f"The time is {t}")

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
                elif 'open github desktop' in tasks:
                    speak('opening github desktop')
                    webbrowser.open('https://github.com/')

                elif 'open github' in tasks:
                    speak('opening github')
                    os.system('start github')

                elif 'close github' in tasks:
                    speak('closing github')
                    os.system('taskkill /f /im github.exe')

                # it will open stackoverflow
                elif 'open stack overflow' in tasks or 'stack overflow' in tasks:
                    speak('opening stackoverflow')
                    webbrowser.open('https://stackoverflow.com/')

                # it will open vs code
                elif 'open vs code' in tasks:
                    speak('opening vscode')
                    os.system('code')

                # it will close vs code
                elif 'close vs code' in tasks:
                    speak('closing vscode')
                    os.system('taskkill /f /im code.exe')

                # it will open file explorer
                elif 'open file explorer' in tasks:
                    speak('opening file explorer')
                    os.system('explorer')
                
                # it will close file explorer
                elif 'close file explorer' in tasks:
                    speak('closing file explorer')
                    os.system('taskkill /f /im explorer.exe')

                # it will restart my computer
                elif 'restart my system' in tasks or 'restart my pc' in tasks:
                    speak('restarting my computer')
                    for i in range(5,0,-1):
                        print(i)
                        speak(i)
                        time.sleep(1)
                    os.system('shutdown /r /t 1')

                # it will shutdown my computer
                elif 'shut down my system' in tasks or 'shut down my pc' in tasks:
                    speak('shutting down my computer')
                    for i in range(5,0,-1):
                        print(i)
                        speak(i)
                        time.sleep(1)
                    os.system('shutdown /s /t 1')
                
                # it will play music
                elif 'play music' in tasks:
                    music_dir = "C:\\Users\\TALHA PC\\OneDrive\\Desktop\\music"
                    songs = os.listdir(music_dir)

                    speak("what music should i play sir")
                    speak("Did you want me to play some random music")
                    speak("Or i will put all the list of the songs")

                    mymusic = takecommand().lower()

                    if 'play random music' in mymusic or 'random' in mymusic:
                        speak("playing random music")
                        rd = random.choice(songs)
                        os.startfile(os.path.join(music_dir, rd))

                    elif 'put list' in mymusic or 'list' in mymusic:
                        speak("putting list of the songs")
                        for song in songs:
                            print(song)
                            speak(song)

                        user_song = takecommand().lower()

                        if user_song in songs:
                            speak("playing " + user_song)
                            os.startfile(os.path.join(music_dir, user_song))

                # it will tell me a joke
                elif 'tell me a joke' in tasks:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)
                
                # it will search on wikipedia
                elif 'wikipedia' in tasks:
                    speak('exploring wikipedia')
                    speak('what should you want to explore')

                    query = takecommand().lower()
                    results = wikipedia.summary(query, sentences=2)

                    print("Searching on wikipedia...")
                    speak("Searching")

                    speak("according to wikipedia")
                    print(results)
                    speak(results)

                # it will send message on whatsapp
                elif 'send message on whatsapp' in tasks:
                    
                    javeria = '+923378415773'
                    farhan = '+923433071974'
                    abid = '+923312617860'
                    adeel = '+923333468247'
                    aani = '+923352641406'


                    speak("Which contact name you want to send message")

                    name = takecommand().lower()

                    if 'javeria' in name:
                        speak("what should i send")
                        print("what should i send")

                        msg = takecommand().lower()
                        kit.sendwhatmsg_instantly(javeria, msg, 10, tab_close=True)

                    elif 'farhan' in name:
                        speak("what should i send")
                        print("what should i send")

                        msg = takecommand().lower()
                        kit.sendwhatmsg_instantly(farhan, msg, 10, tab_close=True)

                    elif 'abid' in name:
                        speak("what should i send")
                        print("what should i send")

                        msg = takecommand().lower()
                        kit.sendwhatmsg_instantly(abid, msg, 10, tab_close=True)

                    elif 'adeel' in name:
                        speak("what should i send")
                        print("what should i send")

                        msg = takecommand().lower()
                        kit.sendwhatmsg_instantly(adeel, msg, 10, tab_close=True)

                    elif 'aani' in name:
                        speak("what should i send")
                        print("what should i send")

                        msg = takecommand().lower()
                        kit.sendwhatmsg_instantly(aani, msg, 10, tab_close=True)

                # it will take a screenshot
                elif "screenshot" in tasks:
                    speak("taking screenshot")
                    img = pyautogui.screenshot(f'screenshot.png')
                    img.save(f'C:\\Users\\TALHA PC\\OneDrive\\Desktop\\screenshots\\screenshot.png')

                # it will switch window
                elif 'switch window' in tasks:
                    speak("switching window")
                    print("switching window")

                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.keyUp('alt')

                # it will minimize all
                elif 'minimize all' in tasks or 'minimise all' in tasks:
                    speak("minimizing all")
                    pyautogui.keyDown('win')
                    pyautogui.press('m')
                    pyautogui.keyUp('win')

                elif 'news' in tasks:
                    speak("please wait sir")
                    speak("fetching the latest news")
                    news()

                elif 'temperature' in tasks:
                    search = "temperature in karachi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    print(f"current {search} is {temp}")
                    speak(f"current {search} is {temp}")


                # when the user if else statement works then it will execute this
                # or when the user says anything else then it will execute this
                speak("Sir how may i help you")
                print("Sir how may i help you")

            # in case of any error
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to do this task")
                speak("say another task")

# this function will continuesly run and append text into myfile.txt
def jarvis():
    while True:
        query = takecommand().lower()

        with open('myfile.txt','w') as f:
            f.write(query)

        readtask()

# calling the function
if __name__ == '__main__':
    jarvis()
