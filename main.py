# This is a sample Python script.

import threading
import time
import tkinter
from pprint import pprint
import datetime
renderTextRegion = None
IsStartWorker = False

def renderText(text):
    if renderTextRegion:
        curTime = datetime.datetime.now().strftime("%H:%M:%S:")
        renderTextRegion.insert(tkinter.END, f"{curTime}: {text}"+"\n")
        renderTextRegion.see("end")
    print(text)

def startMoveFile():
    global IsStartWorker
    if IsStartWorker:
        return

    IsStartWorker = True
    t = threading.Thread(target=TaskWorker)
    t.start()
    renderText("StartMoveFile")

def stopMoveFile():
    global IsStartWorker
    IsStartWorker = False
    renderText("StopMoveFile")

def TaskWorker():
    while IsStartWorker:
        MoveFileTask()
        time.sleep(5)

def MoveFileTask():
    import shutil
    import os
    pprint(os.listdir("/Users/ee303/Dropbox/Camera Uploads/"))
    for files in os.listdir("/Users/ee303/Dropbox/Camera Uploads/"):
        source = r'/Users/ee303/Dropbox/Camera Uploads/{}'.format(files)
        destination = r'/Users/ee303/Downloads/照片備份/{}'.format(files)
        shutil.move(source, destination)
        renderText(f"Move file {source} to {destination}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startMoveFile()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
