import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else: 
        speak("Good Evening!")
    speak("Hii I am jarvis!! How can i help you")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1  
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")        
        
    except Exception as e:
        print("Say that again please...")
        return "None" 
    return query         

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nikhil@gmail.com','14nkrt')
    server.sendmail('nikhil@gmail.com',to,content)
    server.close()    
if __name__=="__main__":
    wishMe()
    while True:
       query=takeCommand().lower()
       
       if 'wikipedia' in query:
           speak('Searching wikipedia...') 
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentence=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
           
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
           
       elif 'open google' in query:
           webbrowser.open("google.com")   
           
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com") 
           
       elif 'play music' in query:
           music_dir='C:\\Users\\DELL\\Music' 
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))         
           
       elif 'open pictures' in query:
           pic_dir='F:\\Pictures' 
           img=os.listdir(pic_dir)
           print(img)
           os.startfile(os.path.join(pic_dir,img[0]))             
           
       elif 'the time' in query:
              strTime=datetime.datetime.now().strftime("%H:%M:%S")
              print(strTime)
              speak(f"Sir, The Time is {strTime}")
              
       elif 'open code' in query:
           codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"      
           os.startfile(codePath) 
           
       elif 'email to nikhil' in query:
           try:
              speak("What should I say?")
              content=takeCommand()
              to="nikhil@gmail.com"
              sendEmail(to,content)
              speak("Email has been sent!")
              
           except Exception as e:
               print(e)
               speak("Sorry this mail can't be sent")        
       elif 'quit' in query:
           exit()   
