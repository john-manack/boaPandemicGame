import time
from classes import Character
import random

# Character Functions and Definitions
character1 = Character("Sherlock", 100, 400, "Female", "Feline ", "medium", 50, 25, "high", "Psychic Whiskers")
cyborgsean = Character("Sean", 30, 100, "Male", "Cyborg", "low", 0, 25, "medium", "None")

def character_list():
    print(character1)

# DIGITAL CRAFTS
def digitalcrafts_location():
    # insert an effect that makes the text show up character by character 
    print("""
    You have arrived at Digital Crafts.
    The flickering fluorescent lights shed scattered rays on an ominous scene.
    You notice black computer monitors covered in dust. A coffee mug is shattered on a desk.
    Cobwebs cover closed cabinets and chewed up rubber duckies litter the floor.
    You could tell this once used to be a place of learning and success.
    """)
    time.sleep(3)
    # insert sound effect!!
    print("""
    *Suddenly, you hear a loud crash coming from up the stairs.*
    What's that!
    You are not alone.
    """)


def digitalcrafts_menu():
    time.sleep(2)
    actionlist = ["1. Continue Down Hallway", 
    "2. Investigate Sound",
    "3. Open Cabinet",
    "4. Leave"]
    print(actionlist)
    while len(actionlist) >= 1:
        action = input("What would you like to do? (1-4) ")
        if action == "1":
            print("""
            You continue down the hallway.
            You are lead to an empty room at the end of the hallway.
            There you find a doll in the middle of the room.
            """)
            yesorno = input("Would you like to pick it up? (Y/N) ")
            if yesorno == "Y":
                print("""
                You pick up the doll. 
                Suddenly it releases a poisonous gas!
                Your health takes a -10 hit.
                """)
                # need to change character to player
                character1.health -= 10
                # want to return character stats
                print(f"Your new stats are: {character1.health})")
                actionlist.pop(0)
                print(actionlist)
                # how to loop around with new changes
                digitalcrafts_menu()
            else:
                digitalcrafts_menu()
        elif action == "2":
            print("""
            Your curiosity gets the best of you. Let us not hope curiosity kills the cat.
            You walk upstairs and investigate the sound.
            """)
            time.sleep(4)
            print("""
            The room is dark, but you make out a faint outline in the corner of the room.
            """)
            time.sleep(2)
            print("""
            'Who goes there?!' Calls the voice.
            You answer back.
            Suddenly, a man with a scraggly beard and kind but withered eyes appears. He looks like he's been through a lot.
            """)
            time.sleep(2)
            print("""
            'My name is Sean. I used to teach here at Digital Crafts... But that was a long time ago.
            Since then, I haven't been able to leave the facility. Memories, ya know? But also, I'm a bit tied up.'
            Sean shows you a battery pack hooked up to the wall. Sean is a cyborg.
            'It's one of the few places in town that still has electricity...'
            You look around and see he has a small pouch next to him.
            """)
            time.sleep(2)
            yesorno = input("You want it? Its got some money in it. I don't need it anymore. (Y/N)" )
            if yesorno == "Y":
                print("""Alright... But I won't let you just have all the answers!
                You need a challenge - let's fight!""")
                print("Cyborg Sean challenges you to a duel!")
                while character1.health > 0:
                    action = input("""
                    What will you do? 
                    1. Punch
                    2. Knife
                    3. Shoot
                    4. Flee
                    """)
                    if action == "1":
                        character1.do_punch
                    elif action == "2":
                        character1.do_knife
                    elif action == "3":
                        character1.do_shoot
                    elif action == "4":
                        digitalcrafts_menu()
                    else:
                        print("BLOOP. Can't do that patna'. Please choose again. ")
            else:
                print("Okay. Bye bye.")
                digitalcrafts_menu()
        elif action == "3":
            print("""
            You sweep away the cobwebs and open the cabinet.
            You find some old sanitizer.
            """)
            character1.bag.append("Sanitizer")
            print(character1.bag)
            actionlist.pop(2)
            print(actionlist)
            digitalcrafts_menu()

        elif action == "4":
            location_menu()
        else:
            print("BLOOP. Can't do that patna'. Please choose again. ")

# Cyborg Sean fight!
def sean_fight(self, zombie):
    print("Cyborg Sean challenges you to a duel!")
    while character1.health > 0:
        action = input("""
        What will you do? 
        1. Punch
        2. Knife
        3. Shoot
        4. Flee
        """)
        if action == "1":
            do_punch(self, zombie)
        elif action == "2":
            do_knife(self, zombie)
        elif action == "3":
            do_shoot(self, zombie)
        elif action == "4":
            digitalcrafts_menu()
        else:
            print("BLOOP. Can't do that patna'. Please choose again. ")

# CONSTRUCTION ZONE - TESTING
character_list()
digitalcrafts_location()
digitalcrafts_menu()