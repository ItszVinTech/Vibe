import speech_recognition as sr
import json
import pyttsx3
import random
import pywhatkit
import pyjokes
import pyautogui
import datetime
import time as tm
import wikipedia
import os
import requests
import webbrowser
from pydub import AudioSegment
from pydub.playback import play

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)


RUNNING = True
master = ' ,(yournamehere)'
assistant = 'computer'

def kelvinToCelsius(kelvin):
    return kelvin - 273.15

def weather():
    api_key = "your weathermap api key"
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "dublin"
    url = f"{root_url}appid={api_key}&q={city_name}"
    r = requests.get(url)
    data = r.json()
    if data['cod'] == 200:
        temp = data['main']['temp']
        kelvin = temp
        celsius = kelvinToCelsius(kelvin)
        celsius = round(celsius, 1)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        descr = data['weather'][0]['description']
        wind = data['wind']['speed']
        print(f"City Name : {city_name}")
        print(f"The Weather Condition is {descr}")
        print(f"The temperature is {celsius} Celsius")
        print(f"The humidity is {humidity}%")
        print(f"The speed of wind is {wind} meters per second")
        talk(f"City Name : {city_name}")
        talk(f"The Weather Condition is {descr}")
        talk(f"The temperature is {celsius} Celsius")
        talk(f"The humidity is {humidity}%")
        talk(f"The speed of wind is {wind}meters per second")
    else:
        print("Something Went Wrong")

def talk(text):
    engine.say(text)
    engine.runAndWait()        

def take_cmd():
    song = AudioSegment.from_wav("listening.wav")
    play(song)

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','' )
                print(command)
    except:
        pass     
    return command

def axela():
    command = take_cmd()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        print('Playing ' + song + master)    
        talk('playing ' + song + master)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time is " + time + master)
        talk("Current time is " + time + master)
    
    elif 'who' in command:
        person = command.replace('who is', '')
        lines = random.randint(1,3)
        info = wikipedia.summary(person, lines)
        print(info)
        talk(info)
    
    elif 'what is' in command:
        person = command.replace('what is', '')
        lines = random.randint(1,3)
        info = wikipedia.summary(person, lines)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    
    elif 'fortnite' in command or 'rocket league' in command or 'fall guys' in command:
        print('Opening Epic Games Launcher...'  + master)
        talk('Opening Epic Games Launcher...'  + master)
        os.startfile('C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe')
    
    elif 'browser' in command or 'brave' in command:
        print('Opening Brave Browser...'  + master)
        talk('Opening Brave Browser...'  + master)
        os.startfile('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
    
    elif 'weather' in command or 'temperature' in command:
        print('Getting Weather...'  + master)
        talk('Getting Weather...'  + master)
        weather()
    
    elif 'whatsapp dad' in command:
        print('Messaging dad..'  + master)
        talk('Messaging dad..'  + master)
        talk('What is the message content? ' + master)
        msg = input('What is the message content? \n')
        webbrowser.open('https://web.whatsapp.com')
        tm.sleep(4)
        pyautogui.click(561,199)
        pyautogui.write('your dads name')
        tm.sleep(1)
        pyautogui.click(637,261)
        tm.sleep(0.5)
        pyautogui.write(msg)
        pyautogui.click(1100,1352)
        pyautogui.click(2038,1345)
        tm.sleep(3)
        pyautogui.click(1320, 442)
        pyautogui.hotkey('ctrl', 'w')

    elif 'whatsapp mom' in command:
        print('Messaging dad..'  + master)
        talk('Messaging dad..'  + master)
        talk('What is the message content? ' + master)
        msg = input('What is the message content? \n')
        webbrowser.open('https://web.whatsapp.com')
        tm.sleep(4)
        pyautogui.click(561,199)
        pyautogui.write('your moms name')
        tm.sleep(1)
        pyautogui.click(637,261)
        tm.sleep(0.5)
        pyautogui.write(msg)
        pyautogui.click(1100,1352)
        pyautogui.click(2038,1345)
        tm.sleep(3)
        pyautogui.click(1320, 442)
        pyautogui.hotkey('ctrl', 'w')

    else:
        webbrowser.open('https://www.google.com/search?q=' + command)
        song = AudioSegment.from_wav("end.wav")
        play(song)
while RUNNING == True:
    axela()
