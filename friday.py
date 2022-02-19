#Import the library which we need
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import sys
import play_music 
import face_classifier
import time

#some global variable 
todo_list = []

#set some global property
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    '''
        This is our speak function 
    '''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''
    This is our greeting function, it greet according to the time
    '''

    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12:
        speak("Good morning !")
    elif hour >=12 and hour < 18:
        speak('Good Afternoon !')
    else:
        speak('Good Evening !')
    speak("I am Friday . verification start")

def create_note():
    '''
    Creating the notes function as a reminder or save the some important function
    '''
    speak("what do you want to write in note?")

    done = False

    while not done:
        try:
            note = takecommand().lower()
            speak("Choose a filename")
            filename = takecommand().lower()            
            with open(f'{filename}.txt', 'w') as f:
                f.write(note)
                done = True
                speak(f"I Successfully save a note in {filename}")
        except sr.UnknownValueError:
            speak("I did not understand you ! please try again.")

def add_todo():
    '''
    This is a list where we place all the reminder of the day
    '''
    speak("What to do do want to add?")
    
    done = False
    while not done:
        item = takecommand().lower()
        todo_list.append(item)
        done = True
        speak(f"I successfully added {item} in to do list!")

def show_todo():
    '''
    This is a function to show all the items in the todo list
    '''
    speak("The item on your to do list are following")
    for item in todo_list:
        speak(item)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said :- {query}\n')
    except Exception as e:
        # print(e)
        print("say that again...\n")
        return "None"
    
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
                    sys.exit(0)

                else:
                    speak("Command is not in my database")
                
        else:
            speak("Face recognition fail, re-try verification")
