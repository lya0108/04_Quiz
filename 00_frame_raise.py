import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randint

def show_frame(frame):
    frame.tkraise()

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

# adds buttons in mainpage and switches frames when clicked
mainpage_easy_btn = tk.Button(mainpage, text="Easy", command=lambda:show_frame(easy))
mainpage_easy_btn.grid(padx=10, pady=10)
mainpage_normal_btn = tk.Button(mainpage, text="Normal", command=lambda:show_frame(normal))
mainpage_normal_btn.grid(padx=10, pady=10)
mainpage_hard_btn = tk.Button(mainpage, text="Hard", command=lambda:show_frame(hard))
mainpage_hard_btn.grid(padx=10, pady=10)
mainpage_instructions_btn = tk.Button(mainpage, text="Instructions", command=lambda:show_frame(instructions))
mainpage_instructions_btn.grid(padx=10, pady=10)

show_frame(mainpage)

root.mainloop()