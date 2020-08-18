import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
#comment added
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Sir. I'm jarvis.Please tell me how May I help you")

def takeCommand():
    #it takes voice command from microphone and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','yourpassword#')
    server.sendmail('toemail@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower()
        #logic for executing various tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\oprakash8\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'open outlook' in query:
            outlookPath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(outlookPath)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to="worstguymanu@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print(e)
                speak("email is not sent, some error ocurred")
        elif 'quit' in query:
            exit()     
    
