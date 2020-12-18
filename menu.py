from script import open_story
from character_classes import Character
from location_class import Location
import time
import sys
from pygame import mixer

character1 = Character("Dr. Robert Neville", 100, "high", 5, "Male", 0, 5)
character2 = Character("Susan", 100, "medium", 10, "Female", 0, 5)
character3 = Character("Carl Grimes", 100, "medium", 15, "Male", 0, 5)
character4 = Character("Stephen", 100, "low", 20, "Male", 0, 5)

bartender = Character("Bartender", 100, "low", 999, "Male", 0, 5)
hs_clerk = Character("hs_clerk", 100, "low", 999, "Male or Female", 0, 5)
cashier = Character("Cashier", 100, "low", 999, "Female", 0, 5)
sus_npc = Character("Sus_Npc", 100, "low", 999, "Male or Female", 0, 5)

bar_zombie = Character("Bartender Zombie", 25, "low", 5, "Male", 10, 4)
hs_zombie = Character("Hs_Zombie", 25, "low", 5, "Male", 10, 4)
cash_zombie = Character("Cashier Zombie", 25, "low", 5, "Male", 10, 4)
sus_npc_zombie = Character("Sus_Npc Zombie", 25, "low", 5, "Male", 10, 4)

home = Location("Home", "This is my home", "room1 is my room", "room2 is the kitchen", "room3 is the garage", 0)
pub = Location("Pub", """
Ahh, the old pub. You've been coming here for years. It's been a while though,
what with the pandemic and all. The smell of bar tar and cigarettes still lingers; 
this place was always packed. Now, a single bartender manages every patron. 
It's almost empty, but there are two young ladies sitting at the far end of the bar.
""", "room1 is my room", "room2 is the kitchen", "room3 is the garage", 0)
highschool = Location("High-School", "This is the High-School", "room1 is my room", "room2 is the kitchen", "room3 is the garage", 0)
stadium = Location("Stadium", "This is the Stadium", "room1 is my room", "room2 is the kitchen", "room3 is the garage", 0)
dig_crafts = Location("DigitalCrafts", "This is Sus-pick", "room1 is my room", "room2 is the kitchen", "room3 is the garage", 0)

def character_list():
    return [character1, character2, character3, character4]

def npc_list():
    return [bartender, hs_clerk, cashier, sus_npc]

def opponent_list(): 
    return [bar_zombie, hs_zombie, cash_zombie, sus_npc_zombie]

def location_list():
    return[home, pub, highschool, stadium, dig_crafts]

# def pub_room_list():
#     return[]

# def highschool_room_list():
#     return[]

# def stadium_room_list():
#     return []

# def dig_crafts_room_list():
#     return []
    
def character_menu():
    print("1. ", str(character1), "2. ", str(character2), "3. ", str(character3), "4. ", str(character4))
    while True:
            user_choice1 = input("Choose your character wisely? (1-4) ")
            if user_choice1 == "1":
                player = character1
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice1 == "2":
                player = character2
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice1 == "3":
                player = character3
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            elif user_choice1 == "4":
                player = character4
                # INPUT SOUNDBOARD RELATED TO CHARACTER
                # time.sleep()
                return player
            else:
                # INPUT SOUNDBOARD FAILED ME DARTH VADER
                # time.sleep(1.5)
                print("YOU HAVE FAILED ME FOR THE LAST TIME!")

def location_menu():
    print("1. ", str(pub.place))
    while True:
        location_choice = input("Where would you like to go? (1-4) ")
        if location_choice == "1": # and location.vists <=0
            location = pub
            print(location.description)
            pub_menu()

            

            return pub
            # pub_location()
            # pub_menu()
        if location_choice == "2":
            location = highschool
            return highschool
        if location_choice == "3":
            location = stadium
            return stadium
        if location_choice == "4":
            location = dig_crafts
            return dig_crafts
        else:
            print("YOU HAVE FAILED ME FOR THE LAST TIME")
    

# def highschool_location(player, key_word):
#     player.location = key_word

# def pub_description():
#     print("""
# Ahh, the old pub. You've been coming here for years. It's been a while though,
# what with the pandemic and all. The smell of bar tar and cigarettes still lingers; 
# this place was always packed. Now, a single bartender manages every patron. 
# It's almost empty, but there are two young ladies sitting at the far end of the bar.
# """)
#     # time.sleep(5)
#     print("What will it be?")
#     # time.sleep(3)

def pub_menu():
    bartenderencounter = 1
    while True:
            user_choice = input("""
1. Have a Pint 
2. Talk to the Bartender
3. Approach the Young Ladies
4. Leave
""")
            if user_choice == "1":
                # self.getdrunk()
                print("Will you have another?")
                pub_menu()
                # INPUT SOUNDBOARD OF POURING A BEER
                # time.sleep()
            elif user_choice == "2":
                # time.sleep(2)
                if bartenderencounter == 1:
                    print("""
You approach the bar. The bartender greets you with a smile..
"The usual?" he says, as he pours your whiskey.
It's nice to be here..
""")
                    # time.sleep(5)
                    # INPUT ZOMBIE BARTENDER SOUND
                    # time.sleep()
                    print("new menu to either talk to the girls or leave?")
                    #/self.zombie_fight(pubZombie)
                    bartenderencounter += 1
                elif bartenderencounter == 2:
                    print("""
You approach the bar. Your faithful bartender's back is turned.
He's more interested in his female patrons than you.
As you sit down, he turns to you and looks up, an empty stare on his face.
His mouth is...
""")
                    # time.sleep(5)
                    print("""
Bleeding?
""")
                    # INPUT ZOMBIE BARTENDER SOUND
                    # time.sleep()
                    zombie_fight()
                    bartenderencounter += 1
                elif bartenderencounter > 2:
                    print("The bartender is dead")
                    pub_menu()

            elif user_choice == "3":
                # time.sleep(2)
                print("""
You can't help but notice these two gorgeous young ladies looking at you.
You approach them...
""")
                # time.sleep(5)
                print("""
"How are you, ladies?"
""")
                # INPUT ZOMBIE BARTENDER SOUND
                # time.sleep()
                print("\"Hey there, handsome\" they say, in a slow, drawly unison.")
                #/self.zombie_fight(pubZombie)
                pub_menu()
            elif user_choice == "4":
                location_menu()


# def stadium_location(player, key):
#     player.location = key_word


def zombie_fight():
    while True:
        print("Get ready to battle %s!" % bar_zombie.name)
        while bar_zombie.alive(): #player.alive() and
            player.print_status()
            bar_zombie.print_status()
            print("")
            print("Battle options:")
            print("1. fight %s" % bar_zombie.name)
            print("2. do nothing")
            print("3. flee")
            user_input = str(input("Enter choice here: "))
            print("*" * 10)
            if user_input == "1":
                player.attack(bar_zombie)
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)
            
            if player.alive():
                bar_zombie.attack(player)
                
            if bar_zombie.dead():
                print("%s killed %s!" % (player.name, bar_zombie.name))

# def player_died(player):
#     print("%s is dead." % (player.name))
#     # Create a word graphic
#     # INPUT SOUNDBOARD RELATED TO LOSING
#     # time.sleep(1.5)
#     # PRINT SOMETHING
#     sys.exit(0)

def ending():
    # create word graphic as well print out a congratulations message
    # INPUT SOUNDBOARD RELATED TO BEATING THE GAME
    # time.sleep(5)
    sys.exit(0)







