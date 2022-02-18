import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import sys
import play_music 
import face_classifier
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12:
        speak("Good morning !")
    elif hour >=12 and hour < 18:
        speak('Good Afternoon !')
    else:
        speak('Good Evening !')

    speak("I am Friday . verification start")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said :- {query}\n')

    except Exception as e:
        # print(e)
        print("say that again...\n")
        # return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        # speak("Face verification")
        name = face_classifier.face_classifier()
        if "yash" == name:
            speak('Face verification complete')
            while True:
                command = takecommand().lower()
                if 'wikipedia' in command:
                    command = command.replace('wikipedia','')
                    result = wikipedia.summary(command, sentences=2)
                    print(result)
                    speak(result)

                elif 'open youtube' in command:
                    webbrowser.open('youtube.com')

                elif 'open stackoverflow' in command:
                    webbrowser.open('stackoverflow.com')

                elif 'open google' in command:
                    webbrowser.open('google.com')

                elif 'play music' in command:
                    play_music.play_audio_songs()

                elif 'play video' in command:
                    play_music.play_video_songs()

                elif 'the time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f'The time is {strTime}')

                elif 'exit' in command:
                    sys.exit()
                
        else:
            speak("Face recognition fail, re-try verification")
 