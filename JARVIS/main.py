import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
newsapi = "news api key" #from newsapi.org


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
    engine.say(text)   #pyttsx3 module documentation
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="your openai api key",
    )

    completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[
        {"role":"system", "content" : "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google cloud.Give short response."},
        {"role": "user", "content":command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    print(f"user:{c}")
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif 'open chat gpt' in c.lower():
        speak("Opening Chat GPT")
        webbrowser.open("https://chat.openai.com")
    elif 'open spotify' in c.lower():
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com/")
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        link = musicLibrary.music[song]
        speak(f"Playing {song}")
        webbrowser.open(link)
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if response.status_code == 200:
            #Parse the JSON response
            data = response.json()

            #extraxt the articles
            articles = data.get("articles",[])
            

            #speak the headlines
            for article in articles:
                speak(article["title"])
    else:
        #let OpenAI handle the request
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing JARVIS...")
    while True:
        #Listne for the wake word "JERVIS"
        #obtain audio from the microphone
        r = sr.Recognizer()
        
        
        print('Recognizing...')
        #recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() in ["jarvis","nova","elias","hey jarvis","hey nova","hey elias"]):
                speak("Yah, How can I help you?")
                #listne for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
            elif word.lower() in ["exit",'quit',"stop" ,"bye","thanks"]:
                speak("Goodbye! Shutting down Nova.")
                break  # exit the loop safely

        except sr.UnknownValueError:
            print("Doesn't Understand audio...")
        except sr.RequestError as e:
            print(f"Google Error: {e}")

