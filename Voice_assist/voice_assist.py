import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import datetime
import pyjokes # type: ignore


# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to the user's speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            command = ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            command = ""
        return command

def get_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"what is current time {now}")

def get_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"what is Today's date {today}")


def tell_joke():
    jokes = pyjokes.get_joke()
    speak(f"Tell me Jokes{jokes}")


def main():
    speak("Hello, how can I help you?")
    while True:
        command = listen().lower()
        if "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hello! How are you?")
        elif "your name" in command:
            speak("I am your voice assistant.")
        elif "time" in command:
            get_time()
        elif "date" in command:
            get_date()
        elif "joke" in command:
            tell_joke()
        elif "wikipedia" in command:
            speak("What do you want to search on Wikipedia?")
            query = listen().lower()
            search_wikipedia(query)
        else:
            speak("I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
