import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "turn on the music" in query:
            speak("Sure, playing music!")  # Textual response
            # (Optional: Add code to open your music player application here)
        elif "call my boss" in query:
            speak("I can't directly make calls yet, but here's your boss's number:")  # Textual response
            # (Optional: Access contact list and display boss's number here)
        elif "shortest route" in query:
            speak("Sure, I can help you find the shortest route. Please specify your destination on a map or search engine.")  # Textual response with guidance
        elif "nearby restaurant" in query:
            speak("Finding nearby restaurants! Would you like Italian, Chinese, or something else?")
