import time
import sys
from pygame import mixer
from classes import Character, Location

#///// mixer.init()





########################################################################################################
##################################### open story function ##############################################
########################################################################################################

def open_story():
    print("""
            _  .-')                                 .-') _  _ .-') _           .-') _   ('-.  _  .-')               
           ( \( -O )                               ( OO ) )( (  OO) )         (  OO) )_(  OO)( \( -O )              
  ,----.    ,------.  .-'),-----.  ,--. ,--.   ,--./ ,--,'  \     .'_       ,(_)----.(,------.,------.  .-'),-----. 
 '  .-./-') |   /`. '( OO'  .-.  ' |  | |  |   |   \ |  |\  ,`'--..._)      |       | |  .---'|   /`. '( OO'  .-.  '
 |  |_( O- )|  /  | |/   |  | |  | |  | | .-') |    \|  | ) |  |  \  '      '--.   /  |  |    |  /  | |/   |  | |  |
 |  | .--, \|  |_.' |\_) |  |\|  | |  |_|( OO )|  .     |/  |  |   ' |      (_/   /  (|  '--. |  |_.' |\_) |  |\|  |
(|  | '. (_/|  .  '.'  \ |  | |  | |  | | `-' /|  |\    |   |  |   / :       /   /___ |  .--' |  .  '.'  \ |  | |  |
 |  '--'  | |  |\  \    `'  '-'  '('  '-'(_.-' |  | \   |   |  '--'  /      |        ||  `---.|  |\  \    `'  '-'  '
  `------'  `--' '--'     `-----'   `-----'    `--'  `--'   `-------'       `--------'`------'`--' '--'     `-----'

You wake up in a daze.
Outside the window, it's dark and dreary. 
You look around the room and find a mirror..
An unfamiliar face stares back at you.

Who are you? 
""")

########################################################################################################
#################################### end open story function ###########################################
########################################################################################################




########################################################################################################
######################## character/location object and function definitions ############################
########################################################################################################

#name, health, purse, sex, punch_power, knife_power, shoot_power, defense)
character1 = Character("Dr. Robert Neville", 100, 500, "Male", "low", 25, 50, "high")
character2 = Character("Susan's Character", 100, 400, "Female", "medium", 25, 50, "medium")
character3 = Character("Carl Grimes", 100, 600, "Male", "high", 25, 50, "low")
character4 = Character("Chico Dusty", 100, 1000, "Male", "high", 25, 50, "low")
pubZombie = Character("Pub Zombie", 20, 100, "Male", "low", 0, 0, "low")
pub = Location("The Pub", "your favorite watering hole", "Bar Area", "Bathroom", "Dart Board")

def character_list():
    return [character1, character2, character3, character4]

def print_character_menu(pos1, char1, pos2, char2, pos3, char3, pos4, char4):
    print("-" * 110)
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        # "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name), (pos4 + char4.name)))
        "Name:", (char1.name), (char2.name), (char3.name), (char4.name)))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Health:", char1.health, char2.health, char3.health, char4.health))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Purse:", char1.purse, char2.purse, char3.purse, char4.purse))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Sex:", char1.sex, char2.sex, char3.sex, char4.sex))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Punch:", char1.punch_power.title(), char2.punch_power.title(), char3.punch_power.title(), char4.punch_power.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Defense:", char1.defense.title(), char2.defense.title(), char3.defense.title(), char4.defense.title()))

########################################################################################################
######################### end character object and function definitions ################################
########################################################################################################





########################################################################################################
############################################ def SELECT A PLAYER #######################################
########################################################################################################

def player_selection():
    print_character_menu("1. ", character1, "2. ",character2, "3. ",character3, "4. ",character4)

# Looping user input to choose character
    while True:
        character_choice = input("""
1. Doctor Robert Neville
2. Susan's Character
3. Carl Grimes
4. Chico Dusty

""")
        if character_choice == "1":
            player = character1
            print("""
Ahhh, Doctor Neville. It took quite some time
to gather your wits. They say that is a side effect
when you've got it...

You must move quickly now. It's spreading... Where will you go?
            """)
            return player
        elif character_choice == "2":
            player = character2
            print("""
Ahhh, Susan's Character. It took quite some time
to gather your wits. They say that is a side effect
when you've got it...

You must move quickly now. It's spreading... Where will you go?
            """)
            return player
        elif character_choice == "3":
            player = character3
            print("""
Ahhh, Mr. Grimes. Carl, is it? 
It took quite quite a while to gather your wits. 
They say that is a side effect when you've got it...

You must move quickly now. It's spreading... Where will you go?
            """)
            return player
        elif character_choice == "4":
            player = character4
            print("""
Ahhh, Chico Dusty. Father of Sir Lucious Leftfoot.
It took quite some time to gather your wits. 
They say that is a side effect when you've got it...

You must move quickly now. It's spreading... Where will you go?
            """)
            return player
        else:
            print("Choose your character by typing '1', '2', '3', or '4', then Enter or Return")

########################################################################################################
######################################### end SELECT A PLAYER ##########################################
########################################################################################################





########################################################################################################
####################################### ZOMBIE FIGHT FUNCTION ##########################################
########################################################################################################

def zombie_fight():
    if location == pub:
        zombie = pubZombie
        return zombie

    while zombie.health > 0 and player.health > 0:
            print("\nWhat do you want to do?")
            print("1. Run Away")
            print("2. Punch")
            if player.knife_power > 0:
                print ("3. Use Knife")
            if player.shoot_power > 0:
                print ("4. Use Gun")
            user_input = input()
    # Run Away
            if user_input == "1":
                player.health -= 20
                location_menu()
    # Punch
            elif user_input == "2":
                punch(player.punch, zombie)
    # Knife
            elif user_input == "3":
                knife(player.knife, zombie)   
    # Gun
            elif user_input == "4":
                shoot(player.shoot, zombie)

            else:
                print(
                    "Your keyboard skills need some work! You missed your chance to attack!\n")
                time.sleep(1.5)
    # Computer ATTACKS!
            if player.health > 0:
                # Opponent attacks player
                opponent_listzombie_list[0].attack(player)
                if player.alive() == False:
                    dead(player)




########################################################################################################
####################################### SELECT LOCATION FUNCTION #######################################
########################################################################################################

def location_menu():
# Looping user input to choose location
    while True:
        location_choice = input("""
1. The Pub
2. The High School
3. The Stadium
4. DigitalCrafts

""")
        if location_choice == "1":
            pub_location()
            pub_menu()
        elif location_choice == "2":
            highschool_location()
            highschool_menu()
        elif location_choice == "3":
            stadium_location()
            stadium_menu()
        elif location_choice == "4":
            digitalcrafts_location()
            digitalcrafts_menu()
        else:
            print("Enter \"1\", \"2\", \"2\", or \"4\"")
            location_menu()

########################################################################################################
################################### end SELECT LOCATION FUNCTION #######################################
########################################################################################################






########################################################################################################
################################## 1. PUB LOCATION & MENU FUNCTIONS ####################################
########################################################################################################

def pub_location():
    print("""
Ahh, the old pub. You've been coming here for years. It's been a while though, 
what with the pandemic and all. The smell of bar tar and cigarettes still lingers; 
this place was always packed. Now, a single bartender manages every patron. 
It's almost empty, but there are two young ladies sitting at the far end of the bar.
    """)
    # time.sleep(5)
    print("What will it be?")
    # time.sleep(3)

def pub_menu():
    bartenderencounter = 1
    location = pub
    while True:
            user_choice = input("""
1. Have a Pint 
2. Talk to the Bartender
3. Approach the Young Ladies
4. Leave

""")
            if user_choice == "1":
                # INPUT SOUNDBOARD OF POURING A BEER
                # time.sleep()
                # self.getdrunk()
                print("Will you have another?")
                pub_menu()
        
            
            elif user_choice == "2":
                #time.sleep(2)
                
                if bartenderencounter == 1:
                    print("""
You approach the bar. The bartender greets you with a smile..
"The usual?" he says, as he pours your whiskey.
It's nice to be here..
""")
                    #time.sleep(5)
                    # INPUT ZOMBIE BARTENDER SOUND
                    # time.sleep()
                    #/print("new menu to either talk to the girls or leave?")
                    bartenderencounter += 1

                elif bartenderencounter == 2:
                    print("""
You approach the bar. Your faithful bartender's back is turned.
He's more interested in his female patrons than you.
As you sit down, he turns to you and looks up, an empty stare on his face.
His mouth is...
""")
                    #///time.sleep(5)
                    print("""
Bleeding?
""")
                    # INPUT ZOMBIE BARTENDER SOUND
                    # time.sleep()
                    print("ZOMBIE FIGHT!")
                    
                    zombie_fight()
                    bartenderencounter += 1

                elif bartenderencounter > 2:
                    print("The bartender is dead")
                    pub_menu()


            elif user_choice == "3":
                #time.sleep(2)
                print("""
You can't help but notice these two gorgeous young ladies looking at you.
You approach them...
""")
                #time.sleep(5)
                print("""
"How are you, ladies?"
""")
                # INPUT LADIES SOUND
                # time.sleep()
                print("\"Hey there, handsome\" they say, in a slow, drawly unison.")
                pub_menu()
            
                   
            elif user_choice == "4":
                print("You couldn't be leaving any sooner... Where to?")
                location_menu()

########################################################################################################
############################### END 1. PUB LOCATION & MENU FUNCTIONS ###################################
########################################################################################################
