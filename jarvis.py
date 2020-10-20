import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyglet

# import PyAudiso

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am jarvis sir,How may i help you?")

def takeCommand():
    # it takes command from microphone inputgnis
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing.....")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please..")
        return "None"
    return query

    


if __name__=="__main__":
    # speak("Arpit is a good boy")
    wishme()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("Acoording to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\arppt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play song' in query:
            music_dir='C:\\Users\\arppt\\Desktop\\arp'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open video' in query:
            vid_dir='D:\\PHOTOS\\arpit\\4thyear'
            vidlist=os.listdir(vid_dir)
            os.startfile(os.path.join(vid_dir,vidlist[0]))


        

        
