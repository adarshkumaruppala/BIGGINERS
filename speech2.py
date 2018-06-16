import speech_recognition as sr
import socket
socket.getaddrinfo('localhost', 8080)
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
with open("microphone-results.wav","wb")as f:
    f.write(audio.get_wav_data())

try:
    
    text=r.recognize_google(audio)
    with open("output.txt","w") as fo:
        text=fo.write(text)
        import os
        os.system("start notepad.exe output.txt")
        
        
        fo.close()
    

    print(" done listening")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e)) 

