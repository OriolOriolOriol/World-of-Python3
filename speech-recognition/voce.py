import speech_recognition as sr 
import os
recognizer_instance = sr.Recognizer()
os.chdir("C:\\Users\\claud\\Desktop")
wav=sr.AudioFile("audio.wav")
with wav as source:
    #recognizer_instance.adjust_for_ambient_noise(source)
    recognizer_instance.pause_threshold=10.0
    print("Sono in ascolto...parla pure!!")
    audio= recognizer_instance.listen(source)
    print("OK! Messaggio ricevuto, attendere l'elaborazione")

try:
    text= recognizer_instance.recognize_google(audio,language="it-IT")
    with open("file.txt","w") as f:
        f.write(text)
    #print("Ho capito: \n", text)
    print("Ho finito di trascrivere sul file...\n")
    time.sleep(1)
except Exception as e:
    print(e)