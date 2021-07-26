# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:18:17 2021

@author: fcoda
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hora():
    time = datetime.datetime.now().strftime("%I:%M%p")
    speak("La hora actual es")
    speak(time)


def fecha():
    fecha = datetime.datetime.now().strftime("%d/%m")
    speak("La fecha de hoy es")
    speak(fecha)

def dia():
    dia = datetime.datetime.now().strftime("%d/%m")
    speak("La fecha de hoy es")
    speak(dia)
    
def wishme():
    speak("Bienvenido señor Daniel!")
    speak("Sistema Nayeli a su servicio, cómo puedo ayudarle?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    
    except Exception as e:
        print(e)
        speak("Por favor repita el comando...")
    
        return "None"
        
    return query

if __name__ == "__main__":
    
    wishme()
    wikipedia.set_lang("es")
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "hora" in query:
            hora()
        elif "fecha" in query:
            fecha()
        elif "que dia" in query:
            dia()
        elif "offline" in query:
            quit()
        elif "busca" in query:
            speak("Buscando...")
            query = query.replace("busca", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
