import psutil
import os
import time

import pyttsx3
engine = pyttsx3.init()

process = filter(lambda p: p.name() == "GTA5.exe", psutil.process_iter())
for i in process:
  p = psutil.Process(i.pid)
  p.suspend()
  time.sleep(11)
  p.resume()
  engine.say("Session resumed")
  engine.runAndWait()