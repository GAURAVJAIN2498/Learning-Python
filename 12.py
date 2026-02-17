import pyttsx3
def myspeak(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

myspeak("you are awesome")  