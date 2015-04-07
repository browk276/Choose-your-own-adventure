# Choose.py
# by [YourNameHere]
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()


################ Ken's Functions #####################


################ AJ's Functions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You must make a decision for you and your unit.  Now you must choose mystery 1 or mystery 2?")
    if (choice == 1):
        messagebox.showinfo("Move on the President",
                            "You choose to carry out your mission to kill the president no matter what happens. You Win. THE END")

    elif (choice == 2):
        messagebox.showinfo("Total Chaos",
                            "You choose to cause as much destruction as you possilby can before... You Die. THE END")
    else:
        choice1()

def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You must make a decision for you and your unit.  Now you must choose tomb 1 or tomb 2.")
    if (choice == 1):
        messagebox.showinfo("Run Away",
                            "You think the situation is hopeless and you tell your unit to RUN!!! You ALL Die. THE END")

    elif (choice == 2):
        messagebox.showinfo("Split Up",
                            "You tell your unit to split up into muitiple groups in a last min effort to" + \
                            " become unpredicable. YOU Live. THE END")
    else:
        choice2()

################ Quinn's Functions #####################
        

################ Main #####################
intro()

root.destroy()
