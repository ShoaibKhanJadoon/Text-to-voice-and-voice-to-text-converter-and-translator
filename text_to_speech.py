import win32com.client
from gtts import gTTS
import pygame



class speak_text:
    def __init__(self):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
    def speak_eng(self, text):
        self.speaker.Speak(text)

    def speak_urdu(self, text):
        tts = gTTS(text=text, lang='ur', slow=False)

        # Save the converted audio to a file
        tts.save("Audio/output.mp3")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load and play the converted file
        pygame.mixer.music.load("Audio/outputurdu.mp3")
        pygame.mixer.music.play()

        # Keep the script running until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pass

    # def speak_persian(self, text):
    #     # Convert the text to Persian speech
    #     tts = gTTS(text=text, lang='en', slow=False)
    #
    #     # Save the converted audio to a file
    #     tts.save("Audio/output.mp3")
    #
    #     # Initialize pygame mixer
    #     pygame.mixer.init()
    #
    #     # Load and play the converted file
    #     pygame.mixer.music.load("Audio/outputpersion.mp3")
    #     pygame.mixer.music.play()
    #
    #     # Keep the script running until the audio finishes playing
    #     while pygame.mixer.music.get_busy():
    #         pass

if __name__ == '__main__':
    s=speak_text()
    # text=input("Enter Text to Speak: ")
    # #s.speak_eng(text)
    # s.speak_urdu(text)

    s.speak_persian("سلام، چطوری؟")
