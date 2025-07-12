import threading
import pyttsx3
import random
import os
import webbrowser
from flask import Flask, request, jsonify, render_template
import datetime
import ollama


app = Flask(__name__)
conversation_history = ['your name is daisy and i have implemented you for my desktop assistant project so be with the name daisy for the entire conversation', "Hello there! *bloom* I'm Daisy, delighted to be your virtual companion for this desktop assistant project! I'll do my best to assist you with any questions or tasks you may have. What's on your mind today? Do you need help with something specific or would you like to chat about a particular topic?",'keep the sentences short until and unless i tell you to speak in detail', "I'll keep my responses brief until further notice. Go ahead and ask your questions or provide context for me to elaborate on. I'm ready when you are!"]

# Text-to-Speech setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to handle speaking in a separate thread
def speak_thread(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    t = threading.Thread(target=speak_thread, args=(text,))
    t.start()

def generate_response(prompt):
    # query = str(input("Enter query: "))
    conversation_history.append(query)
    full_query = "\n".join(conversation_history)
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': full_query,
        },
    ])

    actual_response = response['message']['content']
    conversation_history.append(actual_response)
    print(f"D.A.I.S.Y.: {actual_response}")
    speak(actual_response)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    command = request.json.get("command", "").lower()
    response = ""

    if "time" in command:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The time is {strTime}."
        speak(response)
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube."
        speak(response)
    elif "play music" in command:
        music_dir = "path_to_music_directory"
        if os.path.exists(music_dir):
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
            response = "Playing music."
        else:
            response = "Music directory not found."
        speak(response)
    else:
        conversation_history.append(command)
        full_query = "\n".join(conversation_history)
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': full_query,
            },
        ])

        actual_response = response['message']['content']
        conversation_history.append(actual_response)
        print(f"D.A.I.S.Y.: {actual_response}")
        speak(actual_response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
