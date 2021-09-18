# This is a sample Python script.

import threading
import time
import tkinter
from pprint import pprint
import datetime
renderTextRegion = None
IsStartWorker = False
IGNORE_FILE_NAME = ['desktop.ini']
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
    sourceDirPath = r"C:\Users\s8704\Dropbox\Camera Uploads"
    dstDirPath = r"D:\Dropbox照片備份"
    Allfiles = os.listdir(sourceDirPath)
    if len(Allfiles) -1 > 0:
        renderText(f"Find {len(Allfiles)} files")
    time.sleep(10)

    for files in Allfiles:
        if files in IGNORE_FILE_NAME:
            continue
        source = os.path.join(sourceDirPath, files)
        destination = os.path.join(dstDirPath, files)
        shutil.move(source, destination)
        renderText(f"Move file {source} to {destination}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startMoveFile()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
