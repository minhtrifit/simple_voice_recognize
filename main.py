import speech_recognition as sr
import pyttsx3
import subprocess

MIC_INDEX = 1
engine = pyttsx3.init()
robot_ear = sr.Recognizer()

def HandleRequest(request):
   if "bye" in request:
      return "my pleasure sir"
   if(request == "hello"):
      return "alway service sir"
   if(request == "good morning"):
      return "good morning sir, all services are ready"
   if "time" in request:
      return "you should go to speed sir"
   if "terminal" in request:
       subprocess.Popen(['wt'])
       return "of course sir, terminal is opened"
   if "google chrome" in request:
       # Replace with the path to your Chrome executable
       chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

       # This will open Google Chrome
       subprocess.Popen([chrome_path])
       return "of course sir, google chrome is opened"
   else:
      return "sorry sir i can't recognize your request"

while True:
    try:
        with sr.Microphone(device_index = MIC_INDEX) as mic:
            print("Say something please...")
            engine.say("let me know your request sir")
            engine.runAndWait()

            robot_ear.adjust_for_ambient_noise(mic)
            audio = robot_ear.listen(mic)

        request = robot_ear.recognize_google(audio).lower()
        print("Your request: " + request)

        robot_brain = HandleRequest(request)

        engine.say(robot_brain)
        engine.runAndWait()

        if(robot_brain == "my pleasure sir"):
            break

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        engine.say("sorry sir i can't recognize your request")
        engine.runAndWait()
        
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        engine.say("sorry sir i can't find any audio")
        engine.runAndWait()