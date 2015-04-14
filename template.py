# Choose.py
# by [YourNameHere]
# Description: starter code for the Choose Your
# Own Adventure Project

#Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()
name = simpledialog.askstring("Name?","What's your name?")
################ AJ's Functions #####################

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Recap", "You and your current unit have trained for 6 months." + \
                        "In the middle of the battle, the stealth team reports that the plan has failed.")
    choice = simpledialog.askinteger("Pick a number",
                                   "You have a choice to make: (Win-Win) choice 1 or (No Hope) choice 2?")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()
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
                            "become unpredicable. YOU Live. THE END")
        
    else:
        choice2()
################ Ken's Functions #####################

    messagebox.showinfo("Title", "You and your current unit have trained for 6 months." + \
                        "In the middle of the battle, the stealth team reports that the plan has failed.")
    choice = simpledialog.askinteger("Pick a number",
                                   "You have a choice to pick: 1 or 2")
################ Quinn's Functions #####################

>>>>>>> 98bd686a2ee437f536b0565dc56509a73b0527fa

################ Main #####################
root.destroy()
