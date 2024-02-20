# import pyautogui as p
# import time

# for i in range(1,50):
#     if i == 1:
#         time.sleep(5)
#     p.typewrite(f'Hello this is test message {i}')
#     p.press('enter')

# import pyautogui

# pyautogui.alert('This is an alert box.')

# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])

# pyautogui.prompt('What is your name?')

# pyautogui.password('Enter password (text will be hidden)')

# img1 = pyautogui.screenshot('screenshot.png')
# img1.save('C:\\Users\\TALHA PC\\OneDrive\\Desktop\\screenshots\\screenshot.png')
# import pyttsx3
# import speech_recognition as sr
# from tkinter import messagebox
# import googletrans
# from googletrans import *

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 0.5
#         audio = r.listen(source,phrase_time_limit=5)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         query = query.lower()
#         print(f"user said: {query}")

#     except Exception as e:
#         print(e)
#         # speak("Say that again please...")
#         return "None"

#     return query

# while True:
#     query = takecommand()
#     if 'hello' in query:
#         messagebox.showinfo('hello', 'hello sir')
#         # time.sleep(2)
#         # p.hotkey('alt', 'f4')
#         speak('hello sir')
#     elif 'translate this':
#         query = query.replace('translate this', '')
#         translator = googletrans.Translator()

#         speak('in which language')
#         lang = takecommand()

#         translate = translator.translate(query, dest=lang)
#         speak(translate.text)

# import winsound

# frequency = 3200
# duration = 150

# while True:
#     winsound.Beep(frequency, duration)
#     winsound.Beep(frequency, duration)
#     time.sleep(0.9)

# import time
# import pyautogui

# # for i in range(1, 50):
# #     if i == 1:
# #         time.sleep(20)
# #     pyautogui.typewrite(f'Lag attempt {i}')
# #     pyautogui.press('enter')
# time.sleep(3)
# # pyautogui.click(x=200, y=200)
# pyautogui.mouseUp(y=500)
# pyautogui.click()
# # time.sleep(1)
# pyautogui.mouseDown(y=800)
# import time
# import winsound
# import threading

# def timer():
#     frequency = 2500
#     duration = 150

#     for i in range(1, 50):
#         if i == 1:
#             time.sleep(5)
#         winsound.Beep(frequency, duration)
#         winsound.Beep(frequency, duration)
#         time.sleep(0.9)

# def countdown():
#     for i in range(1, 50):
#         if i == 1:
#             time.sleep(5)
#         print(i)
#         time.sleep(1)

# a = threading.Thread(target=timer)
# a.start()

# b = threading.Thread(target=countdown)
# b.start()


# import pyttsx3
# import speech_recognition as sr
# import time
# import threading

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# # creating an speak function that will speak
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # creating a function that will take command and turn it to text
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 0.5
#         audio = r.listen(source, phrase_time_limit=8)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         query = query.lower()
#         print(f"user said: {query}")

#     except Exception as e:
#         print(e)
#         # speak("Say that again please...")
#         return "None"

#     return query

# def timer():
#     frequency = 2500
#     duration = 15

#     speak("How much time should i set")

#     # it will take secondes from user
#     num = takecommand()
#     num = num.replace('seconds','')
#     speak('setting timer for' + num + 'seconds')
#     print('setting timer for' + num + 'seconds')

#     for i in range(int(num),0,-1):
#         print(i)
#         speak(i)
#         winsound.Beep(frequency, duration)

#         if i == 1:
#             duration = 1500
#             winsound.Beep(frequency, duration)

#         time.sleep(1)
# def tasks():
#     try :
#         while True:
#             query = takecommand()
#             if 'set timer' in query:
#                 a = threading.Thread(target=timer)
#                 a.start()

#             speak("next command sir")
#             print("next command sir")

#     except Exception as e:
#         print(e)

# b = threading.Thread(target=tasks)
# b.start()
# print(threading.active_count())

#!/usr/bin/env python3
# task = []

# def task_saver():
#     global task

#     a = input("Enter task: ")
#     task.append(a)

# def task_reveiwer():
#     global task

#     for i in task:
#         print(i)

# task_saver()
# task_reveiwer()
# import time
# import winsound

# frequency = 3200
# duration = 100
# while True:
#     winsound.Beep(frequency, duration)
#     time.sleep(0.2)
#     winsound.Beep(frequency, duration)
#     time.sleep(1.5)
# user_time = input('Enter time in 24 hours format: ')
# user_time = user_time.replace('for', '')
# user_time = user_time.replace('.', '')
# print(user_time)
# print(len(user_time))
# user_time = user_time[0:2] + ':' + user_time[2:]
# print(user_time)
 
