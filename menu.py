from dr_robert_neville import Character
from script import open_story
import time
import sys
from pygame import mixer

character1 = Character("Dr. Robert Neville", 100, "high", 5, "Male", 0)
character2 = Character("Susan", 100, "medium", 10, "Female", 0)
character3 = Character("John", 100, "medium", 15, "Male", 0)
character4 = Character("Stephen", 100, "low", 20, "Male", 0)

clerk = Character("Clerk", 100, "low", 999, "Female", 0)
cashier = Character("Cashier", 100, "low", 999, "Female", 0)
def character_menu():
    print("1. ", str(character1), "2. ", str(character2), "3. ", str(character3), "4. ", str(character4))
    while True:
            user_choice = input("Choose your character wisely? (1-4) ")
            if user_choice == "1":
                player = character1
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice == "2":
                player = character2
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice == "3":
                player = character3
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice == "4":
                player = character4
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            else:
                # INPUT SOUNDBOARD FAILED ME DARTH VADER
                # time.sleep(1.5)
                print("YOU HAVE FAILED ME FOR THE LAST TIME!")

def player_died(player):
    print("%s is dead." % (player.name))
    # Create a word graphic
    # INPUT SOUNDBOARD RELATED TO LOSING
    # time.sleep(1.5)
    # PRINT SOMETHING
    sys.exit(0)

def ending():
    # create word graphic as well print out a congratulations message
    # INPUT SOUNDBOARD RELATED TO BEATING THE GAME
    # time.sleep(5)
    sys.exit(0)

open_story()

time.sleep(2)
print("Press enter to continue")

character_menu()
