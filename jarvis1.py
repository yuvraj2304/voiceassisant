import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
      speak("Good Afternoon ")

    else:
        speak("Good Evening ")

    speak("Sir I am Jarvis. Please tell me how may i help you i will be greatful to help you")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")   
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please..")  
        return "None"
    return query  

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com, 587')
    server.ehlo()
    server.starttls()
    server.login('yuviicr7@gmail.com', 'password') 
    server.sendmail('yourgmail@gmail.com', to, content)
    server.close()

wishMe()
query = takeCommand().lower()

# Logic for executing tasks based on query
if 'wikipedia' in query:
    speak ("Searching Wikipedia... ")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

elif 'open youtube' in query:
    webbrowser.open("youtube.com")

elif 'open google' in query:
    webbrowser.open("google.com") 

elif 'play music' in query:
    music_dir = 'D:\\Music\\musicc'
    songs = os.listdir(music_dir)    
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

elif 'the time' in query:
   strTime = datetime.datetime.now().strftime("%H:%M:%S")
   speak(f"Sir,The time is {strTime} ")
   
elif 'open code' in query:
    codePath = "C:\\Users\\yuvii\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
     
elif 'email to yuvraj'in query:    
    try:
        speak("what should i say")
        content = takeCommand()
        to = "yuvrajyourEmail@gmail.com"
        sendemail(to, content)
        speak("Email has been sent")
    except Exception as e:
        print(e)   
        speak("Sorry Yuvi bhai, i m not able to send this mail") 

