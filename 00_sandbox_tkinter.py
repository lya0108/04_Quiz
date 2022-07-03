import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randint
#import time

def frame_raise(frame):
    frame.tkraise(aboveThis=None)

def question(frame):
    global answer

    number1 = randint(1, 25)
    number2 = randint(1, 50)
    q = ("Add {} and {}".format(number1, number2))
    answer = number1+number2
    frame.grid(row=0, column=0)
    jbhhd = Label(frame, text=q, width=len(q))
    jbhhd.place(anchor="c", relx=0.5, y=95)
    frame_raise(frame)
    return answer

#counter = 60
#time.sleep(1)
#counter-=1
#points = counter*difficulty_scaling

# window title and dimensions
root = tk.Tk()
root.title("Math Quiz")
root.geometry("512x512")

easy = Frame(root)
easylabel = Label(easy)
easylabel["text"] = "Easy wrhajgbauduwS"

Heading = Label(root, text="Welcome To Andy's Math Quiz", justify=CENTER).place(anchor="c", relx=0.5, y=75)
diff = Label(root, text="Please Select a Difficulty Or Instructions For Instructions", justify=CENTER).place(anchor="c", relx=0.5, y=95)

n = tk.StringVar()
combo = ttk.Combobox(root,state="readonly", width=27, textvariable=n)

combo["values"] = ("Easy", "Normal", "Hard", "Instructions")
combo.place(anchor="c", relx=0.5, y=120)
combo.current(0)

submit = Button(root, text="Submit", command=frame_raise(easy), justify=CENTER).place(anchor="c", relx=0.5, y=145)
root.mainloop()