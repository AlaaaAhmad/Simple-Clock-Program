from datetime import datetime
from tkinter import *


def update():
    now = datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    timee = now.strftime("%H:%M:%S")
    dayLabel.config(text=day)
    dateLabel.config(text=date)
    timeLabel.config(text=timee)
    root.after(1000, update)


root = Tk()
root.config(bg="Black")
dayLabel = Label(root, bg="Black", fg="White", font=("Georgia", 50))
timeLabel = Label(root, bg="Black", fg="Red", font=("Georgia", 50))
dateLabel = Label(root, bg="Black", fg="White", font=("Georgia", 50))
dayLabel.pack()
timeLabel.pack()
dateLabel.pack()


update()

root.mainloop()
