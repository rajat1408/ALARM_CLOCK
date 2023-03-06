from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep
from threading import Thread


#color
bg_color = "#2C3E50" #blue
color1 = "#808B96" #grey



# windows
window = Tk()
window.title("")
window.geometry('450x250')
window.configure(bg=bg_color)

#frames up

frames_line = Frame(window, width=4, height=5, bg=color1)
frames_line.grid(row=0, column=4)

frames_body = Frame(window, width=500, height=290, bg=color1)
frames_body.grid(row=1, column=0)

#frame body

img = Image.open('R1.png')
img=img.resize((110, 110))
img = ImageTk.PhotoImage(img)

app_image = Label(frames_body, height=200, image=img, bg=color1)
app_image.place(x=10, y=10)

name = Label(frames_body,text ="ALARM CLOCK", height=1, font=(" STENCIL 35 bold "),bg=color1)
name.place(x=115, y=1)

#HOUR
hour = Label(frames_body, text="hour", height=1, font=("STENCIL 15 bold"),bg=color1)
hour.place(x=115, y=90)

c_hour = Combobox(frames_body,width=2, font=("arial 15"))
c_hour["values"] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=120,y=120)

#minute
minute = Label(frames_body,text ="MIN",height=1,font=("STENCIL 15 bold"),bg=color1)
minute.place(x=200, y=89)

c_minute = Combobox(frames_body,width=2, font=("arial 15"))
c_minute["values"] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_minute.current(0)
c_minute.place(x=200,y=120)

#second
second = Label(frames_body,text ="SEC",height=1,font=("STENCIL 15 bold"),bg=color1)
second.place(x=265, y=89)

c_sec = Combobox(frames_body,width=2, font=("arial 15"))
c_sec["values"] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=265,y=120)

#period
period = Label(frames_body,text ="PERIOD",height=1,font=("STENCIL 15 bold"),bg=color1)
period.place(x=330, y=89)

c_period = Combobox(frames_body,width=3, font=("arial 15"))
c_period["values"] = ("AM","PM")
c_period.current(0)
c_period.place(x=340,y=120)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print("deactivate alarm: ",selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frames_body, font=("arial 14 bold"), value=1, text="ACTIVATE", bg="#396f80", command=activate_alarm, variable=selected)
rad1.place(x = 135,y = 175)

def sound_alarm():
    mixer.music.load("Audio2.mp3")
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frames_body, font=("arial 14 bold"), value=0, text="STOP", bg="#396f80", command=deactivate_alarm  ,variable=selected)
    rad2.place(x=295, y=175)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_min = c_minute.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        curr = datetime.now()

        hour = curr.strftime("%I")
        minute = curr.strftime("%M")
        second = curr.strftime("%S")
        period = curr.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_min == minute:
                        if alarm_sec == second:
                            print("break time")
                            sound_alarm()
        sleep(1)

mixer.init()

window.mainloop()