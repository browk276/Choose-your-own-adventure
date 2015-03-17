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

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "You and your current unit have trained for 6 months." + \
                        "In the middle of the battle, the stealth team reports that the plan has failed.")
    choice = simpledialog.askinteger("Pick a number",
                                   "You have a choice to pick: 1 or 2")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Student A Functions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You must make a decision for you and your unit.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("Move on the President",
                            "You chose right. You Win. THE END")

    elif (choice == 2):
        messagebox.showinfo("Total Chaos",
                            "You chose to cause as much destruction as you possilby can before... You Die. THE END")
    else:
        choice1()

################ Student B Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You must make a decision for you and your unit.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("Run Away",
                            "You think the situation is hopeless and you tell your unit to RUN!!! You ALL Die. THE END")

    elif (choice == 2):
        messagebox.showinfo("Split Up",
                            "You tell your unit to split up into muitiple groups to become unpredicable. YOU Live. THE END")
    else:
        choice2()

################ Main #####################
intro()

root.destroy()
