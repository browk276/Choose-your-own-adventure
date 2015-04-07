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
def intro():
    # note to self ask for their name
    """ Introductory Function -> starts the story going """
<<<<<<< HEAD
    messagebox.showinfo("Title", "You and your current unit have trained for 6 months." + \
                        "In the middle of the battle, the stealth team reports that the plan has failed.")
    choice = simpledialog.askinteger("Pick a number",
                                   "You have a choice to pick: 1 or 2")
=======
    messagebox.showinfo("Choice 1", "4727 years ago the world was a different place. That was the year 2015, and the government was only about to create the idea that has led to humans miserable existence today. Today on your train ride home from the Armpit you allow yourself to remember the story, even though it's painful.")
    messagebox.showinfo("Choice 1","Humans were allowed to control their own life for the most part, they could buy a house, a car, have any family they want, or not have one, and they could even entertain themselves with the occasional time-waster.")
    messagebox.showinfo("Choice 1","But shortly after that, in the year 2017 after the new American President Sernie Banders was basically bought and forcibly elected to the President seat. The Political Party that was behind it, The Republicrats. They had only planned for a whole year to pull this off, but they were able to take both Houses of Congress and the Judiciary branch, basically take over the entire government")
    messagebox.showinfo("Choice 1","They then borrowed millions of trillions of dollars from other countries, and, using their new ‘wealth,’ they made war on all of the other countries, and were successful in conquering the whole world.")
    messagebox.showinfo("Choice 1","Then the whole point of their plan became apparent. All of the rich, and their Politician cronies forcibly moved everyone out of the southern Hemisphere; now that by itself wasn’t so bad, but when all of the rich, and the politicians all moved south, leaving laws that prohibited everyone with less than $1,000,000 annual income in their place.")
    messagebox.showinfo("Choice 1","Now in the year 6742 after thousands of rebellions you are unsure about the possibility of any rebellion being successful.")
    messagebox.showinfo("Choice 1","The train jerks, as it pulls to a stop at your train station. Getting up, you shake those thoughts out of your head, put your gas mask on, and walk out into the ruined atmosphere of the northern hemisphere.")
    messagebox.showinfo("Choice 1","As you walk down East 3rd your best friend Zinoviya steps out of a shadow and joins you. ")
    messagebox.showinfo("Choice 1","Hello Zinoviya, how are you?")
    messagebox.showinfo("Choice 1","I’m okay " +name+ ". But I have something to ask you privately, do you have a second?")
    messagebox.showinfo("Choice 1","Yeah, sure.")
    messagebox.showinfo("Choice 1","You remember all of the thousands of failed rebellions, they were missing something. There’s a small group of us, though we are getting bigger, and we have that something missing. I can’t talk about it out in the open, too dangerous, but I can ask you if you will help us. Will you help us " +name+ "?")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1 or 2. If you pick 1, you choose to join Zinoviya's army; if you pick 2, you chose to NOT join her army.")
>>>>>>> 98bd686a2ee437f536b0565dc56509a73b0527fa
    if choice == 1:
        choice1()
    elif choice == 2:
        #quinn's death function
    else:
        intro()
intro()




################ Quinn's Functions #####################

>>>>>>> 98bd686a2ee437f536b0565dc56509a73b0527fa

################ Main #####################
root.destroy()
