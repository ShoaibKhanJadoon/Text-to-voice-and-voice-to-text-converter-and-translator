import speech_recognition as sr
import text_to_speech as ts
import webbrowser
import os
from translator import translation





class listen:
    def __init__(self):
        self.r = sr.Recognizer()
        self.query=""
    def voice_to_text_urdu(self):
        with sr.Microphone() as self.source:  # use the default microphone as the audio source
            print("Listening...")
            audio = self.r.listen(self.source)  # listen for the first phrase and extract it into audio data

        try:
            print("Recognizing...")
            self.query=self.r.recognize_google(audio, language="ur")
            print(f"You said {self.query}")  # recognize speech using Google Speech Recognition - ONLINE
            return self.query
            #print("You said " + r.recognize_sphinx(audio,language="ur"))  # recognize speech using CMUsphinx Speech Recognition - OFFLINE
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")

    def voice_to_text_eng(self):
        with sr.Microphone() as self.source:  # use the default microphone as the audio source
            print("Listening...")
            audio = self.r.listen(self.source)  # listen for the first phrase and extract it into audio data

        try:
            print("Recognizing...")
            self.query = self.r.recognize_google(audio,language="en-US")
            print(f"You said {self.query}")  # recognize speech using Google Speech Recognition - ONLINE
            return self.query
            #print("You said " + r.recognize_sphinx(audio,language="ur"))  # recognize speech using CMUsphinx Speech Recognition - OFFLINE
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
    def open_sites(self,query):

        sites = [
            ["YouTube", "https://www.youtube.com"],
            ["Google", "https://www.google.com"],
            ["Facebook", "https://www.facebook.com"],
            ["Twitter", "https://www.twitter.com"],
            ["Instagram", "https://www.instagram.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["Amazon", "https://www.amazon.com"],
            ["LinkedIn", "https://www.linkedin.com"],
            ["Reddit", "https://www.reddit.com"],
            ["Netflix", "https://www.netflix.com"]
        ]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                text.speak_eng(f"opening {site[0]} sir")
                webbrowser.open(site[1])
    def open_music(self, query):
        if f"open music".lower() in query.lower():
            path = "C:/Users/User/Music/output.mp3"
            os.startfile(path)




if __name__ == '__main__':
    text = ts.speak_text()
    text.speak_eng("whats your name")
    name = input("Enter Name: ")
    text.speak_eng(f"welcome {name}")
    text.speak_eng(f"i am listening say what you want")
    i=0
    while   i!=1:
        listening = listen()
        query=listen.voice_to_text_urdu(listening)

        t = translation()
        persion = t.translate_to_persion(query)
        # Example usage:



        text.speak_persian(persion)

        listening.open_sites(query)
        listening.open_music(query)
        i=int(input('Enter 1 to exit'))






