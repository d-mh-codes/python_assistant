# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:18:17 2021

@author: fcoda
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M%p")
    speak("It's ")
    speak(time)


def date():
    date = datetime.datetime.now().strftime("%d/%m")
    speak("today is ")
    speak(date)

def today():
    date = datetime.datetime.now().strftime("%d/%m")
    speak("today is")
    speak(date)
    
def wishme():
    speak("Welcome back, ")
    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    
    except Exception as e:
        print(e)
        speak("Please repeat the command...")
    
        return "None"
        
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('user@gmail.com', 'password')
    server.sendmail('username@gmail.com', to, content)
    server.close()
    


if __name__ == "__main__":
    
    wishme()
    wikipedia.set_lang("en")
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "what time" in query:
            time()
        elif "date" in query:
            date()
        elif "today" in query:
            today()
        elif "offline" in query:
            quit()
        elif "search" in query:
            speak("Searching...")
            query = query.replace("search", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "email" in query:
            try:
                speak("Give me the message")
                content = takeCommand()
                speak("Who will receive the message? ")
                reciever = input("email:  ")
                to = reciever
                sendEmail(to, content)
                speak(content)
                speak('email sent')
            except Exception as e:
                print(e)
                speak("the email cannot be sended")

