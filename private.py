import psutil
import os
import time

import pyttsx3
engine = pyttsx3.init()
import keyboard

def mainmenu():

    while(True):
        a = keyboard.read_key()

        if a == 'page up':
            process = filter(lambda p: p.name() == "GTA5.exe", psutil.process_iter())
            for i in process:
             p = psutil.Process(i.pid)
             p.suspend()
             engine.say("Session suspended")
             engine.runAndWait()
             time.sleep(11)
             p.resume()
             engine.say("Session resumed")
             engine.runAndWait()

        time.sleep(0.3)

mainmenu()