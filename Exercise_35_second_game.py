from sys import exit

#this defines the function 'gold_room'
def gold_room():
    print("This room is full of gold.  How much do you take?")
#when the gold_room function is called
#the user gets a choice
    choice = input("> ")
    #there has to be a better way to check if there
    #is an integer in the input
    #what is interesting is the input is analyzed 
    #by each character
    if "0" in choice or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in choice:
        
        try:
           how_much = int(choice)
        except ValueError:
            #this works but all the other errors still
            #print...
           print("That's not an int!")
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

#this is interesting, this will call the input choice
#over and over again until you get out of the else
#statement
#this is hard because "take honey" / "taunt bear"
#or "open door" aren't easy to understand options
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()