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

################ Quinn's Functions #####################
def ending1():
    messagebox.showinfo("YOU FAIL!", "You reject your friend's offer, and thier mission fails. You are oppressed until the end of your days.")
def stealth2(choice):
    if (choice == "1"):
        messagebox.showinfo("YOU FAIL!",
                            "You chose to try and eliminate the cause of the problem. You and your unit die with honor, sacrificing yourselves so the army can survive. YOU FAIL!")
    elif (choice == "2"):
        messagebox.showinfo("YOU FAIL!",
                            "You chose to report the problem to command. The army turns tail, leaving itself open. It is completely destroyed on the march out.  YOU FAIL!")
    elif (choice == "3"):
        messagebox.showinfo("YOU WIN!",
                            "You chose to split off and complete the mission objective on your own. You sneak past the enemey forces and assassinate the President. YOU WIN!")
    else:
        choice = simpledialog.askstring("Choose wisely", "You choose to take command of the stealth unit. You train for 6 months. In the middle of battle, the plan falls apart due to an unforseen element, and you are presented witha choice. 1) You can try to find and elminate the cause of the problem. 2) You can report the problem to command. 3) Your team can split off and complete the mission objective on their own. ")
        stealth2(choice)

################ Main #####################
intro()

root.destroy()
