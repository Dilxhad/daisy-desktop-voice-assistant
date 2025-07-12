
import webbrowser  
import pyttsx3      
import datetime   
import speech_recognition as sr
import os
import random
import wikipedia
import ollama

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id) 

def speak(audio):

    engine.say(audio)
    engine.runAndWait() 

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Sir, Im Daisy, Your virtual assistant, how may I help you?")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon Sir, Im Daisy, Your virtual assistant, how may I help you?")
    else:
        speak("Good evening Sir, Im Daisy, Your virtual assistant, how may I help you?")

def takeCommand():
    r = sr.Recognizer()                 # Create a recognizer object
    with sr.Microphone() as source:     # Access the user's microphone
        print("Listening...")
        r.energy_threshold = 500        # Minimum audio energy required to trigger recognition
        r.pause_threshold = 1         # Minimum silence length to consider speech complete
        audio = r.listen(source)        # Listen for audio input
    try:
        print("Analyzing...")
        query = r.recognize_google(audio, language='en-in')      # Recognize speech using Google STT
        print(f'User said : {query}\n')                          # Print the recognized text for debugging
        return query
    except Exception as e:
        print(e)
        speak("Please repeat once again...")
        return "None"

def site_list():
    """This is list of predefined websites
        [
             ["youtube", "https://www.youtube.com"],
             ["google", "https://www.google.com"],
             ["chat gpt", "https://chat.openai.com/"],
             ["wikipedia", "https://www.wikipedia.com"],
             ["telegram", "https://web.telegram.org/k/"],
             ["spotify", "https://open.spotify.com/"],
             ["instagram", "https://www.instagram.com/"],
             ["amazon", "https://www.amazon.in/"],
             ["flipkart", "https://www.flipkart.com/"],
             ["email", "https://www.mail.google.com"]
         ]"""
def app_lists():
    """
    Following variable stores application path for their execution
    If code is used in other pc, user may change file path accordingly
    User may personalise this list based on their preferences and day-to-day usage
    appPaths = [
        ["vs code", "C:\\Users\\Dilshad Ansari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
        ["blender", "C:\\Program Files\\Blender Foundation\\Blender 4.0\\blender-launcher.exe"],
    ]
    :return:
    """

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


if __name__ == '__main__':
    greetings()

    sites_file = "D:\Studies\CS50 Final Project\sites.txt"
    if os.path.exists(sites_file):
        with open(sites_file, "r") as f:
            sites = [line.strip().split(",") for line in f.readlines()]
    # print(site_list.__doc__)

    app_paths = "D:\Studies\CS50 Final Project\\appPaths.txt"
    if os.path.exists(app_paths):
        with open(app_paths, 'r') as a:
            appPaths = [line.strip().split(",") for line in a.readlines()]
    # print(app_lists().__doc__)

    conversation_history = ['your name is daisy and i have implemented you for my desktop assistant project so be with the name daisy for the entire conversation', "Hello there! *bloom* I'm Daisy, delighted to be your virtual companion for this desktop assistant project! I'll do my best to assist you with any questions or tasks you may have. What's on your mind today? Do you need help with something specific or would you like to chat about a particular topic?",'keep the sentences short until and unless i tell you to speak in detail', "I'll keep my responses brief until further notice. Go ahead and ask your questions or provide context for me to elaborate on. I'm ready when you are!"]

    command_mode = True
    conversation_mode = False

    while command_mode:                             # Create a loop to continuously listen for commands
        query = takeCommand().lower()       # Get the user's spoken command and convert it to lowercase

        if "add a website".lower() in query or "add a site".lower() in query or "add website".lower() in query or "add site".lower() in query:
            speak("Please provide name and URL of the website.")
            siteName = str(input("Enter site name: "))
            siteURL = str(input("Enter URL of site: "))
            newSite = [siteName, siteURL]
            sites.append(newSite)
            with open(sites_file, "a") as f:
                f.write(f"\n{siteName},{siteURL}")
            print("D.A.I.S.Y.: New site added:", newSite)
            speak("New site has been added.")

        if "add an app".lower() in query or "add an application" in query or "add application".lower() in query or "add path".lower() in query or "add app location".lower() in query:
            speak("Please provide name and path location of the application.")
            appName = str(input("Enter application name: "))
            appLocation = str(input("Enter path location of application: "))
            newPath = [appName, appLocation]
            appPaths.append(newPath)
            with open(app_paths, "a") as a:
                a.write(f"\n{appName},{appLocation}")
            print("D.A.I.S.Y.: New application added:", newPath)
            speak("New application has been added.")

        if "erase all applications".lower() in query or "erase all path locations".lower() in query:
            with open(app_paths, 'w') as erase:
                erase.truncate(0)
            print("D.A.I.S.Y.: All application path locations have been erased successfully")
            speak("All application path locations have been erased successfully")

        if "open".lower() in query:
            for site in sites:
                if f"Open {site[0]}".lower() in query:  # Check if the user's command includes phrases like "Open youtube"
                    print(f"D.A.I.S.Y.: Opening {site[0]}...")
                    speak(f"Opening {site[0]}")
                    webbrowser.open(site[1])

        if "start".lower() in query:
            for paths in appPaths:
                if f"start {paths[0]}".lower() in query:  # Check if the user's command includes phrases like "start blender"
                    print(f"D.A.I.S.Y.: Running {paths[0]}...")
                    speak(f"Running {paths[0]}...")
                    os.startfile(paths[1])

        if "exit".lower() in query:
            print("D.A.I.S.Y.: Goodbye, take care...")
            speak("Goodbye, take care!...")
            conversation_history.clear()
            sites.clear()
            appPaths.clear()
            exit()

        elif "introduce yourself".lower() in query:
            print("D.A.I.S.Y.: Hello! I'm  Daisy, your personal voice assistant. My name Daisy is an acronym for - \n D - Digital \n A - Artificial \n I - Intelligence \n S - System for \n Y - You.\n I am capable of performing multiple tasks which is handy for day-to-day usage of the user. I can provide the list of commands and features if user says 'task summary' in their sentence, as an input. Im looking forward to helping you! ")
            speak("Hello! I'm  Daisy, your personal voice assistant. My name Daisy is an acronym for 'Digital Artificial Intelligence System for You'. I am capable of performing multiple tasks which is handy for day-to-day usage of the user. I can provide the list of commands and features if user says 'task summary' in their sentence, as an input. Im looking forward to helping you!")

        elif "chipi chipi".lower() in query:
            webbrowser.open("https://www.youtube.com/watch?v=0tOXxuLcaog")

        elif "the time".lower() in query or "current time".lower() in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"D.A.I.S.Y.: The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "the day".lower() in query or "today's day".lower() in query:
            strDay = datetime.datetime.now().strftime("%A")
            strDate = datetime.datetime.now().date()
            print(f'D.A.I.S.Y.: Today, {strDate} is {strDay}')
            speak(f'Today, {strDate} is {strDay}')

        elif "calculator".lower() in query:
            print("D.A.I.S.Y.: Here's your calculator")
            speak("Here's your calculator")
            calculator_path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calculator_path)

        elif "change music path".lower() in query or "change music location".lower() in query or "add music path".lower() in query or "add music location".lower() in query:
            newMusicDir = open("musicDir.txt", 'w')
            speak("Please enter new music directory location.")
            newMusicLocation = str(input("Enter new music directory location: "))
            newMusicDir.write(newMusicLocation)
            print("D.A.I.S.Y.: Music directory location updated successfully.")
            speak("Music directory location updated successfully.")

        elif "play music".lower() in query:
            print("D.A.I.S.Y.: Playing music...")
            speak("Playing music")
            m = open("D:\Studies\CS50 Final Project\musicDir.txt", 'r')
            music_dir = m.read()            # Please enter your music directory path in musicDir.txt before executing this functionality
            songs = os.listdir(music_dir)
            N = random.randint(0, len(songs)-1)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[N]))

        elif "search" in query and "wikipedia".lower() in query:
            print("D.A.I.S.Y.: Searching in wikipedia...")
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("about", "")
            query = query.replace("the meaning of", "")
            query = query.replace("please", "")
            results = wikipedia.summary(query, sentences = 3)
            print("D.A.I.S.Y.: According to wikipedia...")
            speak("According to wikipedia...")
            print(f"D.A.I.S.Y.: {results}")
            speak(results)

        elif "Dilshad".lower() in query or "Ansari".lower() in query:
            print("D.A.I.S.Y.:Dilshad, yes I know him, he is the one who developed me, Daisy.")
            speak("Dilshad, yes I know him, he is the one who developed me, Daisy.")

        elif "Your".lower() in query and "developer".lower() in query:
            print("D.A.I.S.Y.: My developer is Dilshad Ansari, who programmed me for creating an interactive voice assistant for his day-to-day usage.")
            speak("My developer is Dilshad Ansari, who programmed me for creating an interactive voice assistant for his day-to-day usage.")

        elif "read instructions".lower() in query:
            print("D.A.I.S.Y.: # Important instructions\n\n1. Do not change any sequence of functionality.\n2. If any website or app path is not in database but is commanded to open or start respectively, program will continue without any output.\n3. In case site or any app does not open, use 'add site' or 'add path' functionality to add your desired website or application respectively.\n4. Store this python code file, app path location list and site list file in same folder before executing program.\n5. Change path locations which are user pc specific accordingly.\n6.Do not add same file location or site URL twice, in case you do, please delete it from their respective text files to avoid any inconvenience.")
            speak("Important instructions\n\n1. Do not change any sequence of functionality.\n2. If any website or app path is not in database but is commanded to open or start respectively, program will continue without any output.\n3. In case site or any app does not open, use 'add site' or 'add path' functionality to add your desired website or application respectively.\n4. Store this python code file, app path location list and site list file in same folder before executing program.\n5. Change path locations which are user pc specific accordingly.\n6.Do not add same file location or site URL twice, in case you do, please delete it from their respective text files to avoid any inconvenience.")

        elif "task summary".lower() in query or "operation summary".lower() in query:
            print("1. 'Open {site name}'   command executes websites.\n2. 'Start {app name}'   command executes applications.\n3. 'Add website'   command adds and updates site database.\n4. 'Add application'    command adds executable application in database.\n5. 'Erase all applications'    command clears all application location in database.\n6. 'Current time'    command tells time or can ask   {what's the time}   directly.\n7. Asking about   'Today's day'   tells current date and day.\n8. 'Calculator'    command opens calculator.\n9. 'Play music'    command plays music.\n10. 'Change music location'    command changes music directory.\n11. 'Exit'    command terminates the program.\n12. 'Task summary'    command provides list of commands and their functionalities.\n13. 'Search'    command searches query in Wikipedia.\n14. Program is in command mode normally and conversation mode can be activated by using command 'conversation mode' and to switch back, use 'command mode' as voice input. ")

        elif "conversation mode".lower() in query or "interactive mode".lower() in query or "chat mode".lower() in query:
            speak("Initializing conversation mode...")
            command_mode = False
            conversation_mode = True

    while conversation_mode:
        query = takeCommand().lower()

        if "exit".lower() in query:
            print("D.A.I.S.Y.: Goodbye, take care...")
            speak("Goodbye, take care!...")
            conversation_history.clear()
            sites.clear()
            appPaths.clear()
            exit()

        elif "the time".lower() in query or "current time".lower() in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"D.A.I.S.Y.: The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "the day".lower() in query or "today's day".lower() in query:
            strDay = datetime.datetime.now().strftime("%A")
            strDate = datetime.datetime.now().date()
            print(f'D.A.I.S.Y.: Today, {strDate} is {strDay}')
            speak(f'Today, {strDate} is {strDay}')
        
        elif "introduce yourself".lower() in query:
            print("D.A.I.S.Y.: Hello! I'm  Daisy, your personal voice assistant. My name Daisy is an acronym for - \n D - Digital \n A - Artificial \n I - Intelligence \n S - System for \n Y - You.\n I am capable of performing multiple tasks which is handy for day-to-day usage of the user. I can provide the list of commands and features if user says 'task summary' in their sentence, as an input. Im looking forward to helping you! ")
            speak("Hello! I'm  Daisy, your personal voice assistant. My name Daisy is an acronym for 'Digital Artificial Intelligence System for You'. I am capable of performing multiple tasks which is handy for day-to-day usage of the user. I can provide the list of commands and features if user says 'task summary' in their sentence, as an input. Im looking forward to helping you!")

        elif "command mode".lower() in query or "operation mode".lower() in query or "task mode".lower() in query:
            speak("Initializing command mode...")
            command_mode = True
            conversation_mode = False

        else:
            generate_response(query)
