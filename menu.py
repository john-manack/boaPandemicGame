from character_classes import Character
from location_class import Location 
import time
import sys
from pygame import mixer

character1 = Character("Dr. Robert Neville", "Human", 100, "high", 0, "Male", "medium", 15, 25, 50, "high", 15, "SAM ATTACK!")
character2 = Character("Sherlock", "Cat", 100, "UNDT CHARISMA", 0, "UNDT SEX", "UNDT PUNCH POWER", 15, 25, 50, "UNDT DEFENSE LVL", 15, "Psychic Whiskers")
character3 = Character("Carl Grimes", "Human", 100, "low", 0, "Male", "medium", 15, 25, 50, "low", 15, "Trooper Drop Kick")
character4 = Character("Chico Dusty", "Human", 100, "UNDT CHARISMA", 0, "Male", "high", 15, 25, 50, "low", 15, "UNDT SPECIAL POWER")

bartender = Character("Bartender", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, 0, 0, None)
lunch_lady = Character("Lunch Lady", "Human", 100, "low", 999, "Female", 0, 0, 0, 0, 0, 0, None)
cashier = Character("Cashier", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, 0, 0, None)
sus_npc = Character("Susan NPC", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, 0, 0, None)

bar_zombie = Character("Bartender Zombie", "Zombie", 25, "low", 50, "Male", "low", 5, 0, 0, "low", 3, None)
hs_zombie = Character("Lunch Lady Zombie", "Zombie", 25, "low", 50, "Female", "low", 5, 0, 0, "low", 3, None)
cash_zombie = Character("Cashier Zombie", "Zombie", 25, "low", 50, "Male", "low", 5, 0, 0, "low", 3, None)
sus_npc_zombie = Character("Susan NPC Zombie", "Zombie", 25, "low", 50, "Male", "low", 5, 0, 0, "low", 3, None)

home = Location("Home", "This is my home", "room1 is my room", "room2 is the kitchen", "room3 is the garage")
pub = Location("Pub", "This is the pub", "room1 is my room", "room2 is the kitchen", "room3 is the garage")
highschool = Location("High-School", "This is the High-School", "room1 is my room", "room2 is the kitchen", "room3 is the garage")
stadium = Location("Stadium", "This is the Stadium", "room1 is my room", "room2 is the kitchen", "room3 is the garage")
dig_crafts = Location("DigitalCrafts", "This is Sus-pick", "room1 is my room", "room2 is the kitchen", "room3 is the garage")

def character_list():
    return [character1, character2, character3, character4]

def npc_list():
    return [bartender, lunch_lady, cashier, sus_npc]

def opponent_list(): 
    return [bar_zombie, hs_zombie, cash_zombie, sus_npc_zombie]

def location_list():
    return[home, pub, highschool, stadium, dig_crafts]

listof_places = []
listof_menus = []

def print_character_menu(pos1, char1, pos2, char2, pos3, char3, pos4, char4):
    print("-" * 110)
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        # "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name), (pos4 + char4.name)))
        "Name:", (char1.name), (char2.name), (char3.name), (char4.name)))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Species:", char1.species.title(), char2.species.title(), char3.species.title(), char4.species.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Health:", char1.health, char2.health, char3.health, char4.health))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Purse:", char1.purse, char2.purse, char3.purse, char4.purse))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Sex:", char1.sex, char2.sex, char3.sex, char4.sex))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Punch:", char1.power_lvl.title(), char2.power_lvl.title(), char3.power_lvl.title(), char4.power_lvl.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Defense:", char1.defense_lvl.title(), char2.defense_lvl.title(), char3.defense_lvl.title(), char4.defense_lvl.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Spec. Power:", char1.special_power.title(), char2.special_power.title(), char3.special_power.title(), char4.special_power.title()))
############################################################################################################################
###########################                                           ###########################
############################################################################################################################
def character_menu():
    print_character_menu("1. ", character1, "2. ", character2, "3. ", character3, "4. ", character4)
    while True:
        character_choice = input("""
1. Doctor Robert Neville
2. Susan's Character
3. Carl Grimes
4. Chico Dusty
""")
        character_choice = input("Choose your character wisely? (1-4) ")
        if character_choice == "1":
            player = character1
            print("""
Ahhh, Doctor Neville. It took quite some time
to gather your wits. They say that is a side effect
when you've got it...
You must move quickly now. It's spreading... Where will you go?
            """)
            # INPUT SOUNDBOARD RELATED TO CHARACTER
            # time.sleep()
            return player
        elif character_choice == "2":
            player = character2
            print("""
Ahhh, Susan's Character. It took quite some time
to gather your wits. They say that is a side effect
when you've got it...
You must move quickly now. It's spreading... Where will you go?
            """)
            # INPUT SOUNDBOARD RELATED TO CHARACTER
            # time.sleep()
            return player
        elif character_choice == "3":
            player = character3
            print("""
Ahhh, Mr. Grimes. Carl, is it? 
It took quite quite a while to gather your wits. 
They say that is a side effect when you've got it...
You must move quickly now. It's spreading... Where will you go?
            """)
            # INPUT SOUNDBOARD RELATED TO CHARACTER
            # time.sleep()
            return player
        elif character_choice == "4":
            player = character4
            print("""
Ahhh, Chico Dusty. Father of Sir Lucious Leftfoot.
It took quite some time to gather your wits. 
They say that is a side effect when you've got it...
You must move quickly now. It's spreading... Where will you go?
            """)
            # INPUT SOUNDBOARD RELATED TO CHARACTER
            # time.sleep()
            return player
        else:
            # INPUT SOUNDBOARD FAILED ME DARTH VADER
            # time.sleep(1)
            print("YOU HAVE FAILED ME FOR THE LAST TIME!")
            time.sleep(2)
            print("Choose your character by inputing 1, 2, 3, or 4")
############################################################################################################################
###########################           ADD GRAPHICS TO LOCATION MENU                              ###########################
############################################################################################################################
def location_menu(player):
    while True:
        location_choice = int(input("""
Where would you like to go?

1. The Pub
2. The High School
3. The Stadium
4. DigitalCrafts
"""))
        if location_choice == 1: # and location.vists <=0
            location = pub
            listof_places.append(location_choice)
            place_visit(player, listof_places, location_choice)
            return location
        if location_choice == 2:
            location = highschool
            listof_places.append(location_choice)
            place_visit(player, listof_places, location_choice)
            return location
        if location_choice == 3:
            location = stadium
            listof_places.append(location_choice)
            place_visit(player, listof_places, location_choice)
            return location
        if location_choice == 4:
            location = dig_crafts
            listof_places.append(location_choice)
            place_visit(player, listof_places, location_choice)
            return location
        else:
            print("YOU HAVE FAILED ME FOR THE LAST TIME")
    print(location.description)
#############################################################################################################################
####################################### COME BACK HERE TO CHANGE COUNTER FOR EACH LOCATION
#############################################################################################################################
def place_visit(player, listof_places, location_choice):
    if listof_places.count(location_choice) <= 1:
        pub_description(player)
    else:
        pub_menu(player)

#############################################################################################################################
####################################### COME BACK HERE TO CHANGE 
####################################### WHEN EACH FIGHT WILL TAKE
#######################################         PLACE
#############################################################################################################################

# def pub_menu(player, listof_places, user_choice):
#     if listof_places.count(user_choice) <= 2:
        
#     else:
#         pub_menu(player)

#############################################################################################################################
####################################### COME BACK HERE TO CHANGE DESCRIPTION FUNCTION
#############################################################################################################################

def pub_description(player):
    while True:
        print("""
Ahh, the old pub. You've been coming here for years. It's been a while though,
what with the pandemic and all. The smell of bar tar and cigarettes still lingers; 
this place was always packed. Now, a single bartender manages every patron. 
It's almost empty, but there are two young ladies sitting at the far end of the bar.
""")
        # time.sleep(5)
        print("What will it be?")
        
        # time.sleep(3)
        pub_menu(player)

#############################################################################################################################
##################      COME BACK HERE TO CHANGE EACH LOCATION MENU     ####################################################
#############################################################################################################################

def pub_menu(player):
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
                pub_menu(player)
                # INPUT SOUNDBOARD OF POURING A BEER
                # time.sleep()
            elif user_choice == "2":
                # time.sleep(2)
                if bartenderencounter == 1 :
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
                    zombie_fight(player)
                    bartenderencounter += 1
                elif bar_zombie.dead():
                    print("""
                    You approach the bar. The new bartender greets you with a shocked look..
"Sorry about that, he was fine this morning and wasn't showing any signs of turning." he says, as he pours your whiskey.
It's nice to be here..
""")
                    pub_menu(player)

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
                pub_menu(player)
            elif user_choice == "4":
                print("Alright I think its about that time too leave.")
                time.sleep(2)
                location_menu(player)

def zombie_fight(player):
    while True:
        print("Get ready to battle %s!" % bar_zombie.name)
        while player.alive() and bar_zombie.alive():
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
                pub_menu(player)




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







