import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser


openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'Keshav: {question}\n AMA: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Keshav'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello my name is AMA how can i help you ? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("Keshav Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'bye' in query:
            break
        else:
            ans=Reply(query)
            print(ans) 
            speak(ans)

