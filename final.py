# Choose.py
# by [YourNameHere]
# Description: starter code for the Choose Your
# Own Adventure Project

from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

name = simpledialog.askstring("Name?","What's your name?")
################ Ken's Functions #####################
def intro():
    """ Introductory Function -> starts the story going """
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
    choice = simpledialog.askstring("Choose wisely",
                                   "You have a choice to pick: 1 or 2. If you pick 1, you choose to join Zinoviya's army; if you pick 2, you chose to NOT join her army.").strip().lower()[0]
    if choice == "1":
        choice1i()
    elif choice == "2":
        death()
    else:
        intro()
def choice1i():
    """Second function called, develops the story further, and presents choice of unit command to player"""
    messagebox.showinfo("Choice 2", "Well, I don't know Zinoviya.....")
    messagebox.showinfo("Choice 2", "Oh, come on, you complain just as loudly as I do! You just gotta join! Finally put all of that attitude of yours to the test.")
    messagebox.showinfo("Choice 2", "Well....... HHHMMM........ Sure, I'll join, I will do whatever you need me to do.")
    messagebox.showinfo("Choice 2", "You don't know how cool this is going to be. Now we need to split up or the police will find us. We'll contact you when we are prepared to recieve you. Now, turn around.")
    messagebox.showinfo("Choice 2", "Why do I have to turn around?")
    messagebox.showinfo("Choice 2", "Plausible Deniability, now... TURN AROUND.")
    messagebox.showinfo("Choice 2", "Suddenly you hear a WHOOSH, feel a little wind, and then silence. You turn around and Zinoviya is gone.")
    messagebox.showinfo("Choice 2", "Flash Forward about half an hour.")
    messagebox.showinfo("Choice 2", "Hello Honey, I'm home from the Armpit!")
    messagebox.showinfo("Choice 2", "Oh, "+name+" your home, I'm in the kitchen.")
    messagebox.showinfo("Choice 2", "Honey, I made a promise to help a friend with something, so if you see Zinoviya come around looking for me, just go ahead and tell her where I am.")
    messagebox.showinfo("Choice 2", "Okay "+name+". I can do that.")
    messagebox.showinfo("Choice 2", "You walk into the bedroom, flop down on the bed, and your eyes are about to close when suddenly you feel a WHOOSH of wind and a needle jabs into your kneck, and then you fall completely asleep.")
    messagebox.showinfo("Choice 2", "The next thing you know, you are on a bed, strapped down, and unable to move.")
    messagebox.showinfo("Choice 2", "Senses on high alert, you lift you head up and look around. You are in what looks like a normal shared hospital room, 2 beds, X-ray machines, portable CAT Scan machine, heart monitor, and the like.")
    messagebox.showinfo("Choice 2", "While you are looking at the equipment, trying to determine if there's anything wrong with you, a bloodcurdling scream of pain eminates from the glass door at the end of your room.")
    messagebox.showinfo("Choice 2", "Looking down the length of your body at the door, you see several doctors and nurses race into a similar room down the hallway, as a twitching, burned man falls to the floor.")
    messagebox.showinfo("Choice 2", "Curious, you watch the doctors lifting the man back into his bed after administering a muscle relaxant. Then you realize that the icon on his door reads I.C.U.")
    messagebox.showinfo("Choice 2", "Panic rising in your throat, you turn to your door and see to your horror the letters, '.U.C.I.' No longer allowing the scream to stay in your throat, you scream, and scream, and scream. Then out of the blue, a cold sensation enters you body through the arm and your I.V., almost instantly you black out.")
    messagebox.showinfo("Choice 2", "When you wake up next, there are two people standing over you, you recognize Zinoviya, but the man next to her is unfamiliar")
    messagebox.showinfo("Choice 2", "Hello, "+name+", how are you feeling?")
    messagebox.showinfo("Choice 2", "Angry.")
    messagebox.showinfo("Choice 2", "This time the odd man replies, I am sorry, I do not approve of Administration's methods either, sometimes. I was told that you were willing to join our growing army?")
    messagebox.showinfo("Choice 2", "Yeah.")
    messagebox.showinfo("Choice 2", "Then, in that case I am here to describe to you what the conversion process entails. We, will be turning you into a completely different subspecies of human, Homo Superior. We have three main powers, telepathy, teleportation, and telekinesis. But, as you may be worried about...")
    messagebox.showinfo("Choice 2", "It's NOT painful. Zinoviya interrupts.")
    messagebox.showinfo("Choice 2", "Will you consent to this procedure?")
    messagebox.showinfo("Choice 2", "Well, I already told her yes.")
    messagebox.showinfo("Choice 2", "Good, but I may want to warn you, some temporary memory loss can happen as a result; at some point in the future, any point, you will forget everything that you don't need to remember, you will remeber the layout of this base, you training, and the Administration Hierarchy, but you will forget everything else. When that does happen, come find Zinoviya, and your training will be complete.")
    messagebox.showinfo("Choice 2", "Okay, Doc.")
    messagebox.showinfo("Choice 2", "As the cold fluid again enters your body Zinoviya calls out one last time, 'Goodnight, Sweet Prince.'")
    messagebox.showinfo("Choice 2", "Suddenly you are in another room, sitting at a chair in front of a HUGE desk. Behind it, is a man who you, oddly, recognize. He is in the middle of talking...")
    messagebox.showinfo("Choice 2", "Will you command the Stealth Unit, or you Current unit? The Stealth Unit will be sneaking into the base and sabotaging the enemies response capabilities, if you choose to take command of your Current Unit, you will be the leader of 50 Infantrymen.")
    choice = simpledialog.askstring("Choose Wisely","You have a choice to pick: 1 or 2. If you pick 1, you choose to command the Stealth Unit; if you pick 2, you chose to command your Current Unit.").strip().lower()[0]
    if choice == "1":
        stealth()
    elif choice == "2":
        current()
    else:
        choice1i()
def stealth1():
    """one of the third functions called"""
    messagebox.showinfo("Choice 3", "Well, General Gasket, I think I will train the Stealth Unit, that sounds like it matches my skill set better.")
    messagebox.showinfo("Choice 3", "Okay, thank you for your dedication to help serve the cause.")
    messagebox.showinfo("Choice 3", "On the way out you send out a telepathic call to your team members, informing them of a meeting that you would like to hold tomorrow morning, really early, so that you can get to know all of you team members before training starts.")
    messagebox.showinfo("Choice 3", "Now, six months later, you and your teams have finished training; not normal training, but the kind that turns your entire team into a single person, you all know exactly how the others are going to act, you all know each others weaknesses and strengths, you all know exactly know how to defend each other, work with each other, you have succesfully become one 'Person'")
    messagebox.showinfo("Choice 3", "You have a 5-man team, including 2 men, Ljubo Dragovic, he's the master telepeth of the group, he is so powerful he can even attack non-telepaths, Javor Gavrilovic, the master telekinetic, he could crush the world if he wanted to (long story), Eliisabet she is the teleportation geek, and could teleport in any circumstance imaginable, and finally Ásta Olvirsson, an Iclandic timecontroller, that is pretty self-explanatory.")
    messagebox.showinfo("Choice 3", "Flash forward, you are in the enemy base, and have succesfully taken down their defenses when you notice something, they have passive defenses that were previously unknown to the army, now you have a choice.")
    choice = simpledialog.askstring("Choose Wisely","Your team is tired, but can go on, if you pick '1' you decide to go and deactivate the new defenses, if you pick '2' you chose to turn the problem over to mission command and follow orders, or if you pick '3' you chose to accomplish the armies ultimate goal of assassinating the World President, whose base, the army is  in the process of attacking.").strip().lower()[0]
    stealth2(choice)

def current():
    """one of the third functions called"""
    messagebox.showinfo("Choice 3", "Well, General Gasket, I think that my current unit is the best I could be in.")
    messagebox.showinfo("Choice 3", "Good choice soldier, dismissed.")
    messagebox.showinfo("Choice 3", "After six months of training you are one of the commanders that form the 3-man team known as mission command. You recieve a report from the Stealth Team, they are informing you that the mission has been compromised, and that the army is currently being surrounded and 'Can't possibly make it out!' What do you order you unit to do?")
    choice1()
################ AJ's Functions #####################

def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You must make a decision for you and your unit.  Now you must choose, 1 is to continue in your efforts to Find and kill the World President, 2 is to order your unit to do as much damage as possible before they die (it is hopeless right?)," + \
                                     "3 is to turn tail and run, and to try to salvage as much of the army as possible, and 4 is to split up into teams of 3, take evasive maneuvers, and try to be unpredictabe while trying to take out the President anyways.")
    if (choice == 1):
        messagebox.showinfo("Move on the President",
                            "You choose to carry out your mission to kill the president no matter what happens. You Win. THE END")
    elif (choice == 2):
        messagebox.showinfo("Total Chaos",
                            "You choose to cause as much destruction as you possilby can before... You Die. THE END")
    elif (choice == 3):
        messagebox.showinfo("Run Away",
                            "You think the situation is hopeless and you tell your unit to RUN!!! You ALL Die. THE END")
    elif (choice == 4):
        messagebox.showinfo("Split Up",
                            "You tell your unit to split up into muitiple groups in a last ditch effort to" + \
                            " become unpredicable. YOU Live, but the mission fails. THE END")
    else:
        choice2()
################ Quinn's Functions #####################


################ Main #####################
intro()
root.destroy()
