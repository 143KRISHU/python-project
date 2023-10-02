import os
import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import datetime

SITES = [["youtube", "http://www.youtube.com", "youtube"], ["wikipedia", "http://www.wikipedia.com", "wikipedia"],
         ["google", "http://www.google.com", "google"], ["facebook", "http://www.facebook.com", "facebook"],
         ["twitter", "http://www.twitter.com", "twitter"], ["instagram", "http://www.instagram.com", "instagram"],
         ["yahoo", "http://www.yahoo.com", "yahoo"], ["amazon", "http://www.amazon.com", "amazon"],
         ["flipkart", "http://www.flipkart.com", "flipkart"]]

APP = [["word", "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE", "word"],
       ["vs code", "E:\\INSTALLED\\Microsoft VS Code\\Code.exe", "vscode"],
       ["notepad", "C:\\Program Files\\Notepad++\\notepad++.exe", "notepad"],
       ["excel", "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE", "excel"],
       ["vlc", "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", "vlc"]]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices)


def say(s):
    engine.say(s)
    engine.runAndWait()


def takecommand():
    print("Listening......")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing........")
            que = r.recognize_google(audio, language="en-in")
            print(f"User said: {que}")
            return que
        except Exception:
            return "Some Error Occured. Sorry From Friday"


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        say("good morning sir, I am ADAM, how may i help you")
    elif 12 < hour <= 16:
        say("good after noon sir, I am ADAM, how may i help you")
    elif 16 < hour <= 20:
        say("good evening sir, I am ADAM, how may i help you")
    else:
        say("good night sir, I am ADAM, how may i help you")


if __name__ == '__main__':
    greeting()
    while 1:
        query = takecommand()

        # opening sites
        for site in SITES:
            if f"Open {site[0]}".lower() in query.lower():
                wb.open(site[1])
                say(f"OPENING {site[2]}")
        # Music play control
        if "play music".lower() in query.lower():
            music_dir = "C:\\Users\\1712r\\Music\\songs"
            songs = os.listdir(music_dir)
            index = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[index]))
        # Time
        if "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")
        # Day
        if "today".lower() in query.lower():
            date = datetime.date.today().strftime("%B %d, %Y")
            say(f"the date today is {date}")

        # todo: add more application in list app
        for app in APP:
            if f"Open {app[0]}".lower() in query.lower():
                os.startfile(app[1])
                say(f"OPENING {app[2]}")

        # about someone or something
        if 'wikipedia'.lower() in query.lower():
            say("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            say("according to wikipedia")
            print(results)
            say(results)

        # shutdown
        if "KILL YOURSELF".lower() in query.lower():
            say("you want me to shut down myself")
            q = takecommand()
            if "yes".lower() or "shutdown".lower() in q.lower():
                say("LOGGING OFF !!!! Have a nice day Sir")
                exit()
