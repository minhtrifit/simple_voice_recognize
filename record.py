import speech_recognition as sr

MIC_INDEX = 1
robot_ear = sr.Recognizer()

with sr.Microphone(device_index=MIC_INDEX) as mic:
    print("Say something please...")

    robot_ear.adjust_for_ambient_noise(mic)
    audio = robot_ear.listen(mic)
    
    print("Audio captured successfully!!!")

# Save the audio to a file to check if it captured correctly
with open("audio_record.mp3", "wb") as f:
    f.write(audio.get_wav_data())

you = robot_ear.recognize_google(audio)
print("You said: " + you)