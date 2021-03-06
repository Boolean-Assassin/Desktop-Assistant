# importing the dependencies
import pyttsx3
import pyautogui
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('This is anthony sir! I am your personal assistant.')
speak('How may I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        query = r.recognize_google(audio, language='en-in')
        

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif query + 'in google' in query:
            speak('okay i got that! ')
            webbrowser.open('www.' +query+ '.com')  

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
        

