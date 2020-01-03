# Created by: Sagar Ghai
# Description: Udacity Nanodegree project, Adventure Game
# Date: 2/1/2020
# License: None

import time
import random
villain = ['dragon', 'troll', 'bear', 'lion', 'dark magician']
villain_chosen = random.choice(villain)
cave_visited=False
house_visited=False

def play_again():
    """
        This finction ensures that I can handle the user request for playing again. It resets the global variables and restarts the game with a random new villain.
    """
    again = input("Would you like to play again? (yes/no)\n").lower()
    while True:
        if "yes" in again:
            print_and_sleep("Excelent! Restarting the game...",3)
            global cave_visited
            global house_visited
            global villain_chosen
            cave_visited = False
            house_visited = False
            villain_chosen = random.choice(villain)
            play()
            break
        elif "no" in again:
            print_and_sleep("Alright. Thank you for playing!")
            break
        else:
            again = input("Please enter a 'yes' or 'no'.\n")

def house(items):
    global house_visited
    if(not house_visited):
        house_visited = True
        print_and_sleep("You approach the door of the house.")
        print_and_sleep("You are about to knock when the door opens "
                   f"and out steps a {villain_chosen}.")
        print_and_sleep(f"Eep! This is a {villain_chosen}'s house!")
    else:
        print_and_sleep(f"The {villain_chosen} comes out furiously again and starts to attack you.")
    decision = input("Would you like to (1) fight or (2) run away?\n")
    while True:
        if decision == "1":
            if "sword" in items:
                print_and_sleep(f"As the {villain_chosen} moves to attack, you "
                            "unsheath your new sword and you ready "
                            "your shield.")
                print_and_sleep("The sword of Ogoroth and Shield of "
                            "Westoros shine brightly in your "
                            "possession as you brace yourself for the "
                            f"attack.\nBut the {villain_chosen} takes "
                            "one look at you shiny new toys and "
                            "runs away!", 3)
                print_and_sleep(f"You have rid the town of the {villain_chosen}. "
                            "You are victorious!")
                play_again()
                break
            else:
                print_and_sleep(f"The {villain_chosen} attacks you! You feel "
                            "a bit under-prepared for this, what "
                            "with only having a tiny dagger.", 2.5)
                print_and_sleep(f"You do your best...but your dagger is no "
                            f"match for the {villain_chosen}.")
                print_and_sleep("You have been defeated!")
                print_and_sleep("GAME OVER!")
                play_again()
                break
        elif decision == "2":
            print_and_sleep("You run as fast as you can back into the field.")
            print_and_sleep("You trip over a piece of wood on your way "
                        f"out, the {villain_chosen} almost grabs your foot.")
            print_and_sleep("You stand up and run as fast as you can "
                        "back into the field safely. Luckily, "
                        "you don't seem to have been followed.", 2.5)
            field(items)
            break
        else:
            decision = input("Would you like to (1) fight or (2) run away?\n")


def cave(items):
    global cave_visited
    if(not cave_visited):
        cave_visited = True
        print_and_sleep("You peer cautiously into the cave.")
        print_and_sleep("It turns out to be a very small cave and your "
                    "eye catches a glint of metal behind a rock.")
        print_and_sleep("You have found the magical Sword of Ogoroth "
                    "and the unbeatable Shield of Westoros.")
        print_and_sleep("You discard your silly old dagger and take "
                    "the sword with you.")
        print_and_sleep("You walk back out "
                    "to the field.", 3)
        items.append("sword")
    else:
        print_and_sleep("You peer cautiously into the cave.")
        print_and_sleep("It turns out to be a very small cave and you see your old dagger.")
        print_and_sleep("You decide to keep the sword and go back to the field")
    field(items)


def field(items):
    print_and_sleep("What would you like to do?")
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "Please enter 1 or 2.\n")
    while True:
        if choice == "1":
            house(items)
            break
        elif choice == "2":
            cave(items)
            break
        else:
            choice = input("Please, enter '1' or '2'.\n")

def print_and_sleep(message, delay_time=1):
    print(message)
    time.sleep(delay_time)

def intro():
    print_and_sleep("You find yourself standing in an open field, filled"
                " with grass and yellow wildflowers.")
    print_and_sleep(f"Rumor has it that a {villain_chosen} is somewhere around "
                "here, and has been terrifying the nearby village.", 3)
    print_and_sleep("In front of you is a house.")
    print_and_sleep("To your right is a dark cave.")
    print_and_sleep("In your hand you hold your trusty (but not "
                "very effective) dagger.")

def play():
    items = []
    intro()
    field(items)

if __name__ == '__main__':
    play()
