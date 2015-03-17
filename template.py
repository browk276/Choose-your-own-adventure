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


################ AJ's Functions #####################


################ Ken's Functions #####################
def intro():
    # note to self ask for their name
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Choice 1", "4727 years ago the world was a different place. That was the year 2015, and the government was only about to create the idea that has led to humans miserable existence today. Today on your train ride home from the Armpit you allow yourself to remember the story, even though it's painful.")
    messagebox.showinfo("Choice 1","Humans were allowed to control their own life for the most part, they could buy a house, a car, have any family they want, or not have one, and they could even entertain themselves with the occasional time-waster.")
    messagebox.showinfo("Choice 1","But shortly after that, in the year 2017 after the new American President Sernie Banders was basically bought and forcibly elected to the President seat. The Political Party that was behind it, The Republicrats. They had only planned for a whole year to pull this off, but they were able to take both Houses of Congress and the Judiciary branch, basically take over the entire government")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1 or 2.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Quinn's Functions #####################


################ Main #####################
root.destroy()
