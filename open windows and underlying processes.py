import pyautogui
from time import sleep
print(pyautogui.getAllWindows())
#print(dir(pyautogui.getAllWindows()[0]))
for i in pyautogui.getAllWindows():
    print(i.title, i.visible, i.isActive, i.size)
    #print(i.title +" "+  str(i.isMaximized) +" "+ str(i.isMinimized) +" "+ str(i.topleft))






import psutil
from datetime import datetime

#date.fromtimestamp()

#parentsset =set()

for proc in psutil.process_iter():
    #print((proc.as_dict()["create_time"]))
    #print(datetime.fromtimestamp((proc.as_dict()["create_time"])))
   #print(proc.started())
   pass
    #print(proc.as_dict())
    #print(proc.name())
    #print(proc.children())
   #parentsset.add(proc.parent())
    #print(proc.cwd())
    #print(proc.environ())
   #print(proc.exe())
   #print(proc.nice())
   



