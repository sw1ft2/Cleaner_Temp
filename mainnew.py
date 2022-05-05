from tkinter import *
import tkinter.ttk as ttk
import shutil
import os
import glob
import time
files = glob.glob(f'C:/Users/{os.environ.get( "USERNAME" )}/AppData/Local/Temp/*')
cnt = str(len(files))
count = 0
result = 0
def clicked():
    for f in files:
        try:
            global count
            global result
            count += os.path.getsize(f)
            score = count / (1024 ** 2)
            result = round(score, 3)
            shutil.rmtree(f, ignore_errors=True)
            os.remove(f)
        except (FileNotFoundError,PermissionError):
            pass


def step():
    for i in range(5):
        window.update_idletasks()
        progress_bar['value'] += 25
        time.sleep(0.05)

def final():
    lbl1.configure(text=f"Было отчищено - {cnt} файла(ов)")
    lbl2.configure(text=f"Объем отчистки - {result} МБ")


window = Tk()
window.title("ClearTemp")
window.geometry("400x250+800+350")

lbl = Label(window, text=f"Отчистка ТЕМР-файлов", font=("Arial Bold", 16))
lbl.place(x=65, y=20)

lbl1 = Label(window, text="", font=("Arial Bold", 16))
lbl1.place(x=35, y=180)
lbl2 = Label(window, text="", font=("Arial Bold", 16))
lbl2.place(x=50, y=210)

btn = Button(window,text='Кнопка',height=2,width=6,command= lambda:[clicked(),step(),final()])
btn.place(x=165, y=130)


progress_bar = ttk.Progressbar(window,orient= "horizontal",mode="determinate",maximum=100,value=0)
progress_bar.pack(expand = True)
progress_bar.place(x = 140,y =90)

window.mainloop()











