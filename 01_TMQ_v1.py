import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randint

def show_frame(frame):
    frame.tkraise()

def correct_show(num):
    if num == 1:
        correct.config(text="Correct")
    elif num == 2:
        correct.config(text="Incorrect")
    elif num == 3:
        correct.config(text="Please Enter A Number")

def easy_question(frame):
    global answer

    number1 = randint(1, 25)
    number2 = randint(1, 50)
    q = ("Add {} and {}".format(number1, number2))
    answer = number1 + number2
    question_label = Label(frame, text=q, width=len(q))
    question_label.grid(padx=10, pady=10)
    return answer

def normal_question(frame):
    global answer

    number1 = randint(1, 25)
    number2 = randint(1, 50)
    q = ("Add {} and {}".format(number1, number2))
    answer = number1 + number2
    question_label = Label(frame, text=q, width=len(q))
    question_label.grid(padx=10, pady=10)
    return answer

def hard_question(frame):
    global answer

    number1 = randint(1, 25)
    number2 = randint(1, 50)
    q = ("Add {} and {}".format(number1, number2))
    answer = number1 + number2
    question_label = Label(frame, text=q, width=len(q))
    question_label.grid(padx=10, pady=10)
    return answer

def answer_check(entry):
    global answer
    global correct

    try:
        entry = int(entry.get())
        
        if entry == answer:
            correct_show(1)
        else:
            correct_show(2)

    except ValueError:
        correct_show(3)

# window, title, and size
root = tk.Tk()
root.title("Math Quiz")
root.geometry("280x400")

# frames
mainpage = tk.Frame(root)
instructions = tk.Frame(root)
easy = tk.Frame(root)
normal = tk.Frame(root)
hard = tk.Frame(root)

# puts frames in
for frame in (mainpage, instructions, easy, normal, hard):
    frame.grid(row=0, column=0, sticky='nsew')

# mainpage labels
mainpage_title1 = tk.Label(mainpage, text="Welcome To Andy's Math Quiz")
mainpage_title1.grid(padx=10, pady=0)
mainpage_title2 = tk.Label(mainpage, text="Please Select A Difficulty Or Instructions For Help")
mainpage_title2.grid(padx=10, pady=0)

# adds buttons in mainpage and switches frames when clicked
mainpage_easy_btn = tk.Button(mainpage, text="Easy", command=lambda:show_frame(easy))
mainpage_easy_btn.grid(padx=10, pady=10)
mainpage_normal_btn = tk.Button(mainpage, text="Normal", command=lambda:show_frame(normal))
mainpage_normal_btn.grid(padx=10, pady=10)
mainpage_hard_btn = tk.Button(mainpage, text="Hard", command=lambda:show_frame(hard))
mainpage_hard_btn.grid(padx=10, pady=10)
mainpage_instructions_btn = tk.Button(mainpage, text="Instructions", command=lambda:show_frame(instructions))
mainpage_instructions_btn.grid(padx=10, pady=10)

# easy frame
easy_title = tk.Label(easy, text="You Chose Easy Mode")
easy_title.grid(padx=10, pady=10)
easy_question(easy)
ans = (tk.Entry(easy))
ans.grid(padx=10, pady=10)
easy_btn = tk.Button(easy, text="Submit", command=lambda:answer_check(ans))
easy_btn.grid(padx=10, pady=10)
easy_mainpage = tk.Button(easy, text="Back To Main Menu", command=lambda:show_frame(mainpage))
easy_mainpage.grid(column=1, padx=10, pady=10)
correct = tk.Label(easy, text="")
correct.grid(row=5, column=0, padx=10, pady=10)



# instructions frame
instructions_title = tk.Label(instructions, text="Instructions")
instructions_title.grid(padx=10, pady=10)
instructions_btn = tk.Button(instructions, text="Back To Main Menu", command=lambda:show_frame(mainpage))
instructions_btn.grid(padx=10, pady=10)

show_frame(mainpage)

root.mainloop()