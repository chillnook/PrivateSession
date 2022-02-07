import psutil
import os
import time

process = filter(lambda p: p.name() == "GTA5.exe", psutil.process_iter())
for i in process:
  p = psutil.Process(i.pid)
  p.suspend()
  time.sleep(11)
  p.resume()