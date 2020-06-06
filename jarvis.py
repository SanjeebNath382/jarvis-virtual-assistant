import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import webbrowser
import smtplib
# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('path/to/installed firefox binary')
# browser = webdriver.Firefox(firefox_binary=binary)
import os
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if  hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening")
    speak("Hello sir I am Jarvis!, Please tell me how I can help you")
def takeCommand():
    '''It takes speech input from user  '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..............")
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            print("Recognising......................")
            query= r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            speak("Sorry did not catch that, Please say that again")
            print("Say that again...............")
            return "none"
        return query
# remove comment and add your user id and password here 
# def sendEmail(to,body):
#     server= smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('your-email','your-password')
#     server.sendmail('your-email',to,body)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searchin in wikipedia....")
            query= query.replace('wikipedia','')
            results= wikipedia.summary(query,sentences=3)
            try:
                
                speak("According to Wikipedia..")
                speak(results)
                print(results)
            except wikipedia.DisambiguationError as e:
                speak("there is some disambiguity!!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
           
        elif 'open google' in query:
            
            webbrowser.open("google.com")
        elif  'open stackoverflow' in query:
            
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'E:\\songs'
            songs= os.listdir(music_dir)
            x= random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[x]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir the thime is {strTime}")
        elif 'open code' in query:
            code_path="C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'send mail' in query:
            speak("Whome do you wanna mail sir?")
            email= takeCommand().lower()
            try:
                speak("What should i say?")
                body= takeCommand()
                to=email
                speak("E-Mail has been sent")
                sendEmail(to,body)
            except Exception as e:
                print(e)
                speak("Sorry there was an error sending your mail")
        elif 'help' in query:
            speak("I can help you with the following")
            speak("To serach something on wikipedia say i wanna search this on wikipedia")
            speak("To open a website say i wanna open this website")
            speak("to play music say jarvis play music")
            speak("To send mail say jarvis send mail")



        

                
                


   

