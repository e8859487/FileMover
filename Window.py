import tkinter as tk

from main import startMoveFile, stopMoveFile
import main

root = tk.Tk()
root.title('湯湯專用移動 DropBox 照片工具')
root.geometry('600x400')
labelVar = tk.StringVar()
labelVar.set("停止")
lbl_1 = tk.Label(root, textvariable=labelVar, bg='yellow', fg='#263238', font=('Arial', 12))
lbl_1.grid(column=0, row=2)
tex = tk.Text(master=root)

def onBtnStart():
    global labelVar
    labelVar.set("運作中...")
    startMoveFile()

def onBtnStop():
    global labelVar
    labelVar.set("停止")
    stopMoveFile()

btnStart = tk.Button(root, height=1, width=10, text="開始移動檔案",
                     command=onBtnStart)
btnStart.grid(row=1, column=0)

btnStop = tk.Button(root, height=1, width=10, text="停止移動檔案",
                    command=onBtnStop)
btnStop.grid(row=1, column=1)

scr = tk.Scrollbar(root, orient=tk.VERTICAL, command=tex.yview)
scr.grid(row=2, column=2, rowspan=15, columnspan=1, sticky=tk.NS)
tex.grid(row=2, column=1, sticky=tk.W)
tex.config(yscrollcommand=scr.set, font=('Arial', 12, 'bold', 'italic'))
main.renderTextRegion = tex
root.mainloop()