import speech_recognition as sr
import pyttsx3

def transcribe_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for your query...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Speech recognition service is down."

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

