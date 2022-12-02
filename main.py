import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone () as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
    try:
        print("Wait For Few Moments...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Just Said:{query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me again...")
        query="none"

    return query            

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print("Good Morning Bro")
        speak("Good Morning Bro")
    elif hour >=12 and hour <17:
        print("Good Afternoon Bro")
        speak("Good Afternoon Bro")    
    elif hour >=17 and hour <21:
        print("Good Evening Bro")
        speak("Good Evening Bro")
    else:
        print("Good Night Bro") 
        speak("Good Night Bro")   


if __name__ =="__main__":
    wishings()
    while True:
        query = commands().lower() 
        if 'time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak("Bro, the time is:"+strTime)
            print(strTime)

        elif 'open chrome' in query:
            speak("Opening Chrome Bro")
            os.startfile("C:\\Users\\baska\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'wikipedia' in query:
            speak("Searching in wikipedia...")
            try:
                query =query.replace("wikipedia", '')
                results = wikipedia.summary(query, sentances=1)
                speak("According To Wikipedia...")
                print(results)
                speak(results)
            except:
                print("No Results Found...") 
                speak("no results found") 
        elif 'play' in query:
            query=query.replace('play','')
            speak("Playing...." + query)
            pywhatkit.playonyt(query)

        elif 'type' in query:
            speak("Please tell me what should i write")
            while True:
                typeQuery = commands()
                if typeQuery == "exit typing":
                    speak("Done Sir")
                    break
                else:
                    pyautogui.write(typeQuery)
                    



