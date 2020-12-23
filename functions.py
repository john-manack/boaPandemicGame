import time
import sys
from pygame import mixer
from classes import Character, Location

##### SOUND #####
mixer.init()
crash = mixer.Sound("audio/mirrorshattering.wav")
punch = mixer.Sound("audio/punch.wav")
knife = mixer.Sound("audio/knife.wav")
shoot = mixer.Sound("audio/shoot.wav")
Guncock = mixer.Sound("audio/Guncock.wav")
pourbeer = mixer.Sound("audio/pourbeer.wav")
zipper = mixer.Sound("audio/zipper.mp3")
cash = mixer.Sound("audio/cash.wav")
gas = mixer.Sound("audio/gas.wav")
creak = mixer.Sound("audio/creak.wav")
evildroid = mixer.Sound("audio/evildroid.wav")
slow_breathing = mixer.Sound("audio/slow_breathing.wav")
groan = mixer.Sound("audio/groan.wav")
sherlock = mixer.Sound("audio/sherlock.wav")
evil_laugh = mixer.Sound("audio/evil_laugh.wav")


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
                                                                    When you look outside the window its dark and dreary. 
                                                                        You look around the room and find a mirror,
                                                                            and you see an unfamiliar figure
                                                                            staring back at you. who are you? 
                                                                                        
                                                                                        Who are you? 
""")

########################################################################################################
#################################### end open story function ###########################################
########################################################################################################




########################################################################################################
######################## character/location object and function definitions ############################
########################################################################################################

#########################name, ###########health, purse, sex, punch, defense)
character1 = Character("Dr. Robert Neville", 100, 500, "Male", "medium", "medium")
character2 = Character("Sherlock the Cat", 100, 400, "Female", "medium", "medium")
character3 = Character("Carl Grimes", 100, 600, "Male", "high", "low")
character4 = Character("Chico Dusty", 100, 1000, "Male", "high", "low")
pubZombie = Character("Pub Zombie", 40, 100, "Male", "low", "low")
cyborgsean = Character("Cyborg Sean", 60, 100, "Male", "low", "medium")
hs_zombie = Character("Lunch Lady Zombie", 80, 100, "Female", "low", "medium")
mall_zombie = Character("Body Building Zombie", 90, 100, "Male", "medium", "medium")
plot_zombie = Character("Parking Lot Zombie", 40, 100, "Male", "low", "low")
cdcZombie = Character("CDC MEGA ZOMBIE", 600, 10000, "Male", "extra_high", "medium")



def character_list():
    return [character1, character2, character3, character4]

def print_character_menu(pos1, char1, pos2, char2, pos3, char3, pos4, char4):
    print("-" * 192)
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    # "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name), (pos4 + char4.name)))
                                                    "Name:", (char1.name), (char2.name), (char3.name), (char4.name)))
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    "Health:", char1.health, char2.health, char3.health, char4.health))
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    "Purse:", char1.purse, char2.purse, char3.purse, char4.purse))
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    "Sex:", char1.sex, char2.sex, char3.sex, char4.sex))
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    "Punch:", char1.punch.title(), char2.punch.title(), char3.punch.title(), char4.punch.title()))
    print("                                         {:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
                                                    "Defense:", char1.defense.title(), char2.defense.title(), char3.defense.title(), char4.defense.title()))

########################################################################################################
######################### end character object and function definitions ################################
########################################################################################################


########################################################################################################
################################### ASCII GRAPHIC FUNCTIONS ############################################
########################################################################################################

def zombieattack_art():
    print("""
                                                                    ______  _______  _______  ______  _________ _______ 
                                                                    / ___   )(  ___  )(       )(  ___ \ \__   __/(  ____ \\
                                                                    \/   )  || (   ) || () () || (   ) )   ) (   | (    \/
                                                                        /   )| |   | || || || || (__/ /    | |   | (__    
                                                                       /   / | |   | || |(_)| ||  __ (     | |   |  __)   
                                                                      /   /  | |   | || |   | || (  \ \    | |   | (      
                                                                     /   (_/\| (___) || )   ( || )___) )___) (___| (____/\\
                                                                    (_______/(_______)|/     \||/ \___/ \_______/(_______/
                                                                                                                        
                                                                _______ __________________ _______  _______  _        _  _ 
                                                                (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\( )( )
                                                                | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| || |
                                                                | (___) |   | |      | |   | (___) || |      |  (_/ / | || |
                                                                |  ___  |   | |      | |   |  ___  || |      |   _ (  | || |
                                                                | (   ) |   | |      | |   | (   ) || |      |  ( \ \ (_)(_)
                                                                | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \ _  _ 
                                                                |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_)(_)
    """)
    print("*" * 192)

def cyborgattack_art():
    print("""
                                                                    _______           ______   _______  _______  _______ 
                                                                    (  ____ \|\     /|(  ___ \ (  ___  )(  ____ )(  ____ \\
                                                                    | (    \/( \   / )| (   ) )| (   ) || (    )|| (    \/
                                                                    | |       \ (_) / | (__/ / | |   | || (____)|| |      
                                                                    | |        \   /  |  __ (  | |   | ||     __)| | ____ 
                                                                    | |         ) (   | (  \ \ | |   | || (\ (   | | \_  )
                                                                    | (____/\   | |   | )___) )| (___) || ) \ \__| (___) |
                                                                    (_______/   \_/   |/ \___/ (_______)|/   \__/(_______)
                                                                                                                        
                                                                _______ __________________ _______  _______  _        _  _ 
                                                                (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\( )( )
                                                                | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| || |
                                                                | (___) |   | |      | |   | (___) || |      |  (_/ / | || |
                                                                |  ___  |   | |      | |   |  ___  || |      |   _ (  | || |
                                                                | (   ) |   | |      | |   | (   ) || |      |  ( \ \ (_)(_)
                                                                | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \ _  _ 
                                                                |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_)(_)
    """)
    print("*" * 192)

def player_dies():
    print("""
                                                                  _______              ______  _________ _______  ______   _  _ 
                                                        |\     /|(  ___  )|\     /|    (  __  \ \__   __/(  ____ \(  __  \ ( )( )
                                                        ( \   / )| (   ) || )   ( |    | (  \  )   ) (   | (    \/| (  \  )| || |
                                                         \ (_) / | |   | || |   | |    | |   ) |   | |   | (__    | |   ) || || |
                                                          \   /  | |   | || |   | |    | |   | |   | |   |  __)   | |   | || || |
                                                           ) (   | |   | || |   | |    | |   ) |   | |   | (      | |   ) |(_)(_)
                                                           | |   | (___) || (___) |    | (__/  )___) (___| (____/\| (__/  ) _  _ 
                                                           \_/   (_______)(_______)    (______/ \_______/(_______/(______/ (_)(_)
    """)
    print("*" * 192)
    exit()

def you_win():
    print("""
                                                                          _______                       _________ _        _  _ 
                                                                |\     /|(  ___  )|\     /|    |\     /|\__   __/( (    /|( )( )
                                                                ( \   / )| (   ) || )   ( |    | )   ( |   ) (   |  \  ( || || |
                                                                 \ (_) / | |   | || |   | |    | | _ | |   | |   |   \ | || || |
                                                                  \   /  | |   | || |   | |    | |( )| |   | |   | (\ \) || || |
                                                                   ) (   | |   | || |   | |    | || || |   | |   | | \   |(_)(_)
                                                                   | |   | (___) || (___) |    | () () |___) (___| )  \  | _  _ 
                                                                   \_/   (_______)(_______)    (_______)\_______/|/    )_)(_)(_)
                                                                                                
                                                                You have defeated all of the massive mutant zombies and cyborgs
                                                                in your path. You have discovered the vaccine for the virus
                                                                and acquired all the information you need to deploy it.
                                                                The world will be back to normal in no time...
    """)
    time.sleep(10)
    print("""
                                                                                            Or will it?
    """)
    print("*" * 192)
    time.sleep(2)
    exit()

########################################################################################################
##################################### END ASCII GRAPHIC FUNCTIONS ######################################
########################################################################################################




########################################################################################################
############################################ def SELECT A PLAYER #######################################
########################################################################################################

def player_selection():
    print_character_menu("1. ", character1, "2. ",character2, "3. ",character3, "4. ",character4)

# Looping user input to choose character
    while True:
        print("-" * 192)
        character_choice = input("""
                                                                                    1. Doctor Robert Neville

                                                                                    2. Sherlock the Cat

                                                                                    3. Carl Grimes

                                                                                    4. Chico Dusty
        """)
        print("-" * 192)
        if character_choice == "1":
            player = character1
            print("""
                                                                    Ahhh, Doctor Neville. It took quite some time
                                                                    to gather your wits. They say that is a side effect
                                                                    when you've got it...
                                                                    You must move quickly now. It's spreading... Where will you go?
            """)
            print("-" * 192)
            location_menu(player)

        elif character_choice == "2":
            player = character2
            sherlock.play()
            print("""
                                                                    Ahhh, Sherlock the Cat, such a freaky feline. It took quite some 
                                                                    time to gather your wits. They say that is a side effect
                                                                    when you've got it...
                                                                    You must move quickly now. It's spreading... Where will you go?
            """)
            print("-" * 192)
            location_menu(player)

        elif character_choice == "3":
            player = character3
            print("""
                                                                    Ahhh, Mr. Grimes. Carl, is it? 
                                                                    It took quite quite a while to gather your wits. 
                                                                    They say that is a side effect when you've got it...
                                                                    You must move quickly now. It's spreading... Where will you go?
            """)
            print("-" * 192)
            location_menu(player)

        elif character_choice == "4":
            player = character4
            print("""
                                                                    Ahhh, Chico Dusty. Father of Sir Lucious Leftfoot.
                                                                    It took quite some time to gather your wits.
                                                                    They say that is a side effect when you've got it...
                                                                    You must move quickly now. It's spreading... Where will you go?
            """)
            print("-" * 192)
            location_menu(player)

        else:
            print("""
                                                            Choose your character by typing '1', '2', '3', or '4', then Enter or Return
            """)
            print("-" * 192)

########################################################################################################
######################################### end SELECT A PLAYER ##########################################
########################################################################################################





########################################################################################################
####################################### SELECT LOCATION FUNCTION #######################################
########################################################################################################

def location_menu(player):
# Looping user input to choose location
    while True:
        if pubZombie.health <= 0 and cyborgsean.health <= 0 and hs_zombie.health <= 0 and mall_zombie.health <= 0 and plot_zombie.health <=0:
            location_choice = input("""
                                                                                        1. The Pub
                                                                                        
                                                                                        2. The High School
                                                                                        
                                                                                        3. The Mall
                                                                                        
                                                                                        4. Digital Crafts
                                                                                        
                                                                                        5. Check Health
                                                                                        
                                                                                        6. Check Bag
                                                                                        
                                                                                        7. Go to the CDC
            """)
            print("*" * 192)
        else:
            location_choice = input("""
                                                                                        1. The Pub

                                                                                        2. The High School
                                                                                        
                                                                                        3. The Mall
                                                                                        
                                                                                        4. Digital Crafts
                                                                                        
                                                                                        5. Check Health
                                                                                        
                                                                                        6. Check Bag
            """)
            print("*" * 192)
        if location_choice == "1":
            pub_location()
            pub_menu(player)
        elif location_choice == "2":
            highschool_location()
            highschool_menu(player)
        elif location_choice == "3":
            mall_location()
            mall_menu(player)
        elif location_choice == "4":
            digitalcrafts_location()
            digitalcrafts_menu(player)
        elif location_choice == "5":
            player.print_status()
        elif location_choice == "6":
            player.bag_contents()
        elif location_choice == "7" and pubZombie.health <= 0 and cyborgsean.health <= 0 and hs_zombie.health <= 0 and mall_zombie.health <= 0 and plot_zombie.health <=0:
            cdc_location()
            cdc_menu(player)
        elif location_choice == "17":
            player_selection()
        else:
            print("""
                                                                            Enter "1", "2", "3", "4", "5", or "6"
            """)
            print("-" * 192)
            location_menu(player)

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
    print("-" * 192)
    time.sleep(7)
    print("""
                                                                                        What will it be?
    """)
    # time.sleep(3)

def pub_menu(player):
    pint_count = 0 
    while True:

# IF PUB ZOMBIE IS ALIVE:

            if pubZombie.health > 0:
                user_choice = input("""
                                                                                    1. Have a Pint 

                                                                                    2. Talk to the Bartender
                                                                                    
                                                                                    3. Approach the Young Ladies
                                                                                    
                                                                                    4. Leave
                """)
                print("*" * 192)
                if user_choice == "1" and pint_count <= 5:
                    print("*" * 192)
                    print("""
                                                                                        That'll be $5
                    """)
                    pourbeer.play()
                    time.sleep(4)
                    cash.play()
                    time.sleep(1)
                    player.purse -= 5
                    print("""
                                                                                        You now have $%d
                    """ % (player.purse))
                    print("*" * 192)
                    player.health -=2
                    if player.health <= 0:
                        player_dies()
                    pint_count += 1
                    
                        
                    if user_choice == "1" and player.gamestop_count >= 2 and pint_count >=6:
                        print("""
                                                            ya... ya... ya..., ok!! ill take your advice and go say hey to her....
                                                            You leave the bar and just start walking....

                                                            once you go inside you ask the mannequin behind the cashier counter
                                                            "Aye Hank whose the girl in the.. Never mind I'll find out for myself.

                                                            As you walk to the back where this mannequin wearing a fur coat is standing you say

                                                            "I promised my friends that I would say hello to you....

                                                            Hello.....

                                                            Hello.....

                                                            Please say hello to me

                                                            PPleease say hello to me!!!!"
                        """)
                        print("*" * 192)
                        time.sleep(5)
                        print("""
                                                                You wake up at home not remembering what happened last night.
                        """)
                        print("*" * 192)
                        location_menu(player)
                    if user_choice == "1" and pint_count >= 6:
                        print("""
                                                                                I think it's time to go home..........

                                                                                ......................................

                                                                                ......................................
                        """)
                        # SNORING NOISES
                        time.sleep(5)
                        print("""
                                                                                You wake up at home... 
                
                                                                                Now what?
                        """)
                        print("*" * 192)
                        location_menu(player)
                    if user_choice == "2":
                        print("*" * 192)
                        pub_menu(player)
                    
                elif user_choice == "2":
                    #time.sleep(2)
                    
                    if player.bartenderencounter == 1:
                        print("""
                                                                You approach the bar. The bartender greets you with a smile..
                                                                "The usual?" he says, as he pours your whiskey.
                                                                It's nice to be here..
                        """)
                        print("*" * 192)
                        player.bartenderencounter += 1
                    
                    elif player.bartenderencounter == 2:
                        print("""
                                                              You approach the bar. Your faithful bartender's back is turned.
                                                              He's more interested in his female patrons than you.
                                                              As you sit down, he turns to you and looks up, an empty stare on his face.
                                                              His mouth is.....      
                        """)
                        time.sleep(10)
                        print("""
                                                                                            Bleeding?
                        """)
                        print("*" * 192)
                        time.sleep(2)
                        # INPUT ZOMBIE BARTENDER SOUND
                        while pubZombie.health > 0 and player.health > 0:
                            zombieattack_art()
                            print("""
                                                                                    What do you want to do?
                                                                                    1. Run Away
                                                                                    
                                                                                    2. Punch""")
                            if "knife" in player.bag:
                                print ("""
                                                                                    3. Use Knife""")
                            if "Gun" in player.bag:
                                print ("""                                          
                                                                                    4. Use Gun""")
                            user_input = input()
                            print("*" * 192)
                    # Run Away
                            if user_input == "1":
                                player.health -= 20
                                pub_menu(player)
                    # Punch
                            elif user_input == "2":
                                player.do_punch(pubZombie)
                                punch.play()
                    # Knife
                            elif user_input == "3" and "knife" in player.bag:
                                player.do_knife(pubZombie)
                                knife.play()
                    # Gun
                            elif user_input == "4" and "Gun" in player.bag:
                                player.do_shoot(pubZombie)
                                shoot.play()

                            else:
                                print("""
                                                                You entered an invalid option and missed your chance to strike!
                                """)
                                print("*" * 192)
                                time.sleep(1.5)
                    # ZOMBIE ATTACKS!
                            if player.health > 0 and pubZombie.health > 0:
                                time.sleep(1.5)
                                pubZombie.do_punch(player)
                                punch.play()
                            
                            if player.health <= 0:
                                print ("""
                                                                    The %s KILLED YOU!!! Better luck next time...
                                """)
                                print("*" * 192)
                                player_dies()
                            
                            if pubZombie.health <= 0:
                                print ("""
                        
                                                                                %s KILLED %s!! 
                                                                                %s's health is %d.
                                                                                ....Now what?
                                """ % (player.name, pubZombie.name, player.name, player.health))
                                print("*" * 192)
                        player.bartenderencounter += 1

                    elif player.bartenderencounter > 2:
                        print("""
                                                                                    The bartender is dead
                        """)
                        print("*" * 192)
                        pub_menu(player)


                elif user_choice == "3":
                    if player.ladies1_count == 1:
                        print("""
                                                        You can't help but acknowledge the two gorgeous young ladies at the end of the bar.
                                                        You approach them...
                        """)
                        time.sleep(5)
                        print("""
                                                                                    "How are you, ladies?"
                        """)
                    # INPUT LADIES SOUND
                        time.sleep(2)
                        print("""
                                                                                    Get lost, creep,
                                                                                    says the older, less attractive one.
                                                                                                        
                                                                                    Today may not be your day...
                        """)
                        print("*" * 192)
                        player.ladies1_count +=1
                        pub_menu(player)
                    else:
                        print("""
                                                                                    "Get lost, creep,
                                                                                    Maybe if you do something spectacular you
                                                                                    can talk to us!"

                                                                                    Today still isn't your day...
                        """)
                        print("*" * 192)
                        pub_menu(player)
                    
                elif user_choice == "4":
                    print("""
                                                                            You couldn't be leaving any sooner... 
                                                                            
                                                                            Where to?
                    """)
                    print("*" * 192)
                    location_menu(player)
        
            else:

# IF PUB ZOMBIE IS DEAD:

                user_choice = input("""
                                                                                    1. Have a Pint 

                                                                                    2. Approach the Young Ladies
                                                                                    
                                                                                    3. Leave
                """)
                print("*" * 192)
                if user_choice == "1" and pint_count <= 5:
                    print("""
                                                                                        That'll be $5
                    """)
                    pourbeer.play()
                    time.sleep(4)
                    cash.play()
                    time.sleep(1)
                    player.purse -= 5
                    print("""
                                                                                        You now have $%d
                    """ % (player.purse))
                    print("*" * 192)
                    player.health -=2
                    if player.health <= 0:
                        player_dies()
                    pint_count += 1
                    if user_choice == "1" and player.gamestop_count >= 2 and pint_count >=6:
                        print("""
                                                            ya... ya... ya..., ok!! ill take your advice and go say hey to her....
                                                            You leave the bar and just start walking....

                                                            once you go inside you ask the mannequin behind the cashier counter
                                                            "Aye Hank whose the girl in the.. Never mind I'll find out for myself.

                                                            As you walk to the back where this mannequin wearing a fur coat is standing 
                                                            you say

                                                            "I promised my friends that I would say hello to you....

                                                            Hello.....

                                                            Hello.....

                                                            Please say hello to me

                                                            PPleease say hello to me!!!!"
                        """)
                        print("*" * 192)
                        time.sleep(5)
                        print("""
                                                                You wake up at home not remembering what happened last night.
                        """)
                        print("* " * 192)
                        location_menu(player)
                    if user_choice == "1" and pint_count >= 6:
                    print("""
                                                                                I think it's time to go home..........

                                                                                ......................................

                                                                                ......................................
                        """)
                        # SNORING NOISES
                        time.sleep(5)
                        print("""
                                                                                You wake up at home... 
                
                                                                                Now what?
                        """)
                        print("*" * 192)
                        location_menu(player)
                    if user_choice == "2":
                        pub_menu(player)
                    

                elif user_choice == "2":
                    if player.ladies_count == 1:
                        #time.sleep(2)
                        print("""
                                                            You can't help but notice these two gorgeous young ladies looking at you.
                                                            You approach them...
                        """)
                        time.sleep(2)
                        print("""
                                                                                    "How are you, ladies?"
                        """)
                        # INPUT LADIES SOUND
                        time.sleep(1)
                        print("""
                                                        "Hey there, handsome" says the pale, glassy eyed brunette, 
                                                        in a slow, almost infectious drawl. "You saved us from that plague of a bartender.
                                                        We thought we were history."
                                                        "Just an instinct these days," you reply, as you notice the color
                                                        running away from her face.
                                                        "Here," she says. "Take this." As she pulls a large, glinting
                                                        blade from her handbag. "I'm not much with it. But it may help you next time..."
                        """)
                        time.sleep(5)
                        print("*" * 192)            
                        player.knife += 1
                        player.bag.append("knife")
                        zipper.play()
                        time.sleep(1)
                        print("""
                                                                            Your bag now contains %s
                        """ % (player.bag))
                        print("*" * 192)

                        player.ladies_count += 1
                        pub_menu(player)
                    elif player.ladies_count >= 2:
                        print("""
                                                                            "That was some show with the bartender. 
                                                                            Hope the knife we gave you helps..."
                        """)
                        print("*" * 192)                 
                    
                elif user_choice == "3":
                    print("""
                                                                            You couldn't be leaving any sooner... 
                    """)
                    time.sleep(1)
                    print("""
                                                                                           Where to?
                    """)
                    print("*" * 192)
                    location_menu(player)
            

########################################################################################################
############################### END 1. PUB LOCATION & MENU FUNCTIONS ###################################
########################################################################################################





########################################################################################################
################################## 2. HIGH SCHOOL LOCATION & MENU FUNCTIONS ############################
########################################################################################################

def highschool_location():
    print("""
                                                            You arrive at an abandoned high school...
                                                            The smell of rotting food floats through the air.
                                                            You think you see a shadowy figure step behind a 
                                                            wall on the far side of the building.
                                                            The front doors are locked, but you notice a window that's been left ajar.
                                                            You climb through to find yourself in a dark hallway.
    """)
    print("*" * 192)

def highschool_menu(player):
    while True:
        print("""
                                                                                Where do you want to go? (1-4)

                                                                                1. Auditorium

                                                                                2. Cafeteria
                                                                                
                                                                                3. Classroom
                                                                                
                                                                                4. Leave High School                                                                                
        """)
        user_choice = input()
        print("*" * 192)

################ INTERACTION 1 ######################
        if user_choice == "1":
            if player.auditorium_count == 1:
                if "Lock-Picks" in player.bag:
                        print("""
                                                                    You use your Lock-Picks to pick the locked door.
                                                                    You enter the school auditorium, which is cool and dark.
                                                                    The large burGundy curtains hanging over the stage are 
                                                                    ripped and tattered. To your left is the sound booth, 
                                                                    so you decide to investigate.As soon as you open the 
                                                                    saloon-style door, you notice a $25 bill on the floor 
                                                                    beneath the sound board. Neat!
                        """)
                        print("*" * 192)
                        player.purse += 25
                        cash.play()
                        time.sleep(1)
                        print("""
                                                                        You added $25 to your purse! You now have $%s!
                        """ % player.purse)
                        print("*" * 192)
                        player.auditorium_count += 1
                else:
                    print("""
                                                            This door is locked! If only there were a way to pick the lock...
                    """)
                    print("*" * 192)
            elif player.auditorium_count >= 2:
                print("""
                                                        Hmm! You've seen all there is to see here! You wander back into the hall.
                """)
                print("*" * 192)

################ INTERACTION 2 ######################
        elif user_choice == "2":
            if player.cafeteria_count == 1:
                print("""
                                                                    The cafeteria reveals the source of the horrid smell. 
                                                                    The freezers have been left open for days,
                                                                    and the putrid food has been plundered and thrown 
                                                                    all over the cafeteria by someone...
                                                                    
                                                                    ... or something.
                """)
                time.sleep(5)
                print("""
                                                                  You hear the sound of a sink running, it's coming from the 
                                                                  kitchen. Is someone in there? You approach the door and 
                                                                  push it open. What you see next sets your heart racing...
                """)
                # Heart beat sound if possible
                time.sleep(4)
                print("""
                                                                        The beloved high school lunch lady is laying 
                                                                        on the ground with her head turned. You run up 
                                                                        to check if she is still breathing. 
                """)
                time.sleep(3)
                print("""
                                                                        No breath.....
                """)
                time.sleep(.75)
                print("""
                                                                        No pulse......
                """)
                time.sleep(.75)
                print("""
                                                                        But is that her arm...... moving???
                """)
                print("*" * 192)
                time.sleep(2)
                while hs_zombie.health > 0 and player.health > 0:
                    zombieattack_art()
                    print("""
                                                                                    What do you want to do?

                                                                                    1. Run Away
                                                                                    
                                                                                    2. Punch""")
                    if "knife" in player.bag:
                        print ("""
                                                                                    3. Use Knife""")
                    if "Gun" in player.bag:
                        print ("""
                                                                                    4. Use Gun""")
                    user_input = input()
                    print("*" * 192)
            # Run Away
                    if user_input == "1":
                        player.health -= 20
                        print("*" * 192)
                        highschool_menu(player)
                        
            # Punch
                    elif user_input == "2":
                        player.do_punch(hs_zombie)
                        punch.play()
            # Knife
                    elif user_input == "3" and "knife" in player.bag:
                        player.do_knife(hs_zombie)
                        knife.play()
            # Gun
                    elif user_input == "4" and "Gun" in player.bag:
                        player.do_shoot(hs_zombie)
                        shoot.play()

                    else:
                        print("""
                                                                You entered an invalid option and missed your chance to strike!
                        """)
                        print("*" * 192)
            # ZOMBIE ATTACKS!
                    if player.health > 0 and hs_zombie.health > 0:
                        time.sleep(1.5)
                        hs_zombie.do_punch(player)
                        punch.play()
                    
                    if player.health <= 0:
                        print ("""
                                                                    The %s KILLED YOU!!! Better luck next time...
                        """ % hs_zombie)
                        print("*" * 192)
                        player_dies()
                    
                    if hs_zombie.health <= 0:
                        print ("""
                                                                                %s KILLED %s!! 
                                                                                
                                                                                %s's health is %d.
                                                                                ....Now what?
                        """ % (player.name, hs_zombie.name, player.name, player.health))
                        print("*" * 192)
                player.cafeteria_count += 1
            elif player.cafeteria_count >= 2:
                print("""
                                                        Hmm! You've seen all there is to see here! You wander back into the hall.
                """)
                print("*" * 192)

################ INTERACTION 3 ######################
        elif user_choice == "3":
            if player.classroom_count == 1:    
                print(""" 
                                                                    You walk into the classroom down the hall. 
                                                                    There are few desks overturned and the 
                                                                    chalk-board on the wall is crooked...
                                                                    It looks like there was some sort of struggle in here. 
                                                                    Something shiny catches your eye under one of the desks... 
                                                                    It's a little Lock-Picks! Must have belonged 
                                                                    to a misbehaving highscooler! You pick it up and 
                                                                    slip it in your bag. You wander back into the hall.
                        """)
                print("*" * 192)
                zipper.play()
                time.sleep(1)
                player.bag.append("Lock-Picks")
                print("""
                                                                    Your bag contents are now %s.
                """ % player.bag)
                print("*" * 192)
                player.classroom_count += 1
            elif player.classroom_count >= 2:
                print("""
                                                            Hmm! You've seen all there is to see here! You wander back into the hall.
                """)
                print("*" * 192)
                
################ LEAVE SCHOOL #######################
        elif user_choice == "4":
            print("*" * 192)
            location_menu(player)

############### INVALID ENTRY - LOOP RESETS #########
        else:
            
            print("""
                                                                                    Sorry I didn't get that.
            """)

########################################################################################################
############################## END 2. HIGH SCHOOL LOCATION & MENU FUNCTIONS ############################
########################################################################################################





########################################################################################################
############################# 3. MALL LOCATION & MENU FUNCTIONS ########################################
########################################################################################################


def mall_location():
    print("""
                                                        Oooh, the mall. You haven't been here in forever!!! You remember coming here
                                                        with your friends to hang out and meet new people. Instead of the amazing smell
                                                        of all the different types of food, from the food market, it now smells like 
                                                        rotting flesh. As you are walking towards the entrance from the parking lot
                                                        all the abandoned cars windows are shattered and scattered across the ground.
                                                        Loud crunching of the glass echos out........
        """)
    print("*" * 192)
    time.sleep(4)

def mall_menu(player):
    if player.mall_count == 1:
        print("""
                                                        Just as you are about to reach the entrance you hear a deep growling voice 
                                                        coming from behind one of the cars in the first row of the parking lot...
                                                        It has heard the loud crunching and is slowly making it's way to you.
        """)
        print("*" * 192)
        player.mall_count += 1
    while plot_zombie.health > 0 and player.health > 0:
        zombieattack_art()
        time.sleep(2)
        print("""
                                                                                    What do you want to do?

                                                                                    1. Run Away
                                                                                    
                                                                                    2. Punch""")
        if "knife" in player.bag:
            print ("""
                                                                                    3. Use Knife""")
        if "Gun" in player.bag:
            print ("""
                                                                                    4. Use Gun""")
        user_input = input("")
        print("*" * 192)
        if user_input == "1":
            print("*" * 192)
            # player.health -= 20
            location_menu(player)
# Punch
        elif user_input == "2":
            player.do_punch(plot_zombie)
            punch.play()
# Knife
        elif user_input == "3" and "knife" in player.bag:
            player.do_knife(plot_zombie)
            knife.play()
# Gun
        elif user_input == "4" and "Gun" in player.bag:
            player.do_shoot(plot_zombie)
            shoot.play()
        else:
            print("""
                                                                    You entered an invalid option and zombie struck you!
            """)
            print("*" * 192)

        if player.health > 0 and plot_zombie.health > 0:
            time.sleep(1.5)
            plot_zombie.do_punch(player)
            punch.play()
        if player.health <= 0:
            print ("""
                                                                    The %s KILLED YOU!!! Better luck next time...
            """ % (plot_zombie.name))
            print("*" * 192)
            player_dies()
        if plot_zombie.health <= 0:
            print ("""
                                                                                %s KILLED %s!! 
                                                                                
                                                                                %s's health is %d.
            """ % (player.name, plot_zombie.name, player.name, player.health))
            print("*" * 192)

    while True:
        print("""
                                                                                    Where do you want to go? (1-4)
                                                                                    
                                                                                    1. Gamestop
                                                                                    
                                                                                    2. Staff Lounge
                                                                                    
                                                                                    3. Beretta
                                                                                    
                                                                                    4. Leave Mall
        """)
        user_choice = input()

################ INTERACTION 1 ######################
        if user_choice == "1":
            if player.gamestop_count == 1:
                print(""" 
                                                        You are walking toward GameStop which is in the middle of the Plaza level. 
                                                        There are mannequins everywhere and graffiti written all of the walls...
                                                        As you are right outside of the doors you notice 2 mannequins, one is 
                                                        a male mannequin wearing an orange hoodie. The other a female mannequin
                                                        wearing a black hat covering her face, as well as a black leather jacket.
                                                        I guess ill just name you Fred and Marge. When you enter something catches
                                                        your eye.
                """)
                time.sleep(4)
                print("""
                                                            You walk over to the mannequin behind the cashier counter and ask

                                                            Aye hank whose the girl in the uuuggghh........

                                                            Nvm aye maybe another time.
                """)
                print("*" * 192)
                time.sleep(2)
                player.gamestop_count += 1
            elif player.gamestop_count == 2:
                print("""
                                                                While opening the door to GameStop you say
                                                                'Aye morning Marge, morning Fred, anything new happen since
                                                                I've been gone? Just as you ask you notice someone has been 
                                                                in here since all the games on the shelves have been rummaged 
                                                                through. As you look around you hear a faint moan and some 
                                                                coughing.... 
                """)
                time.sleep(8)
                print("""
                                                            When you approach the distressed noises, you walk over
                                                            a dead zombie, to see a man pointing a Gun at you. He says                 
                                                            "Hands up.. cough.. cough.. Thats far enough" 
                                                            As you tell him you are not infected and was just coming to check
                                                            what was happening.
                                                            He then states "I need you to do something for me cough.. cough.. 
                                                            as obviously I am not going to make it much longer if you couldn't
                                                            tell already."
                """)
                time.sleep(9)
                print("""
                                                            Sure what do you need some bandages?
                                                            "No, here take this" as he hands you the Gun "Before I turn into one
                                                            of those things I need you to stop that from happening!
                                                            But....
                                                            "No buts cough.. cough.. I would hate for my body to be one of them
                                                            cough.. grr.. and walking around attacking people grr.. cough.. do it
                                                            now or it's going to be late grrr...
                """)
                print("*" * 192)
                time.sleep(9)
                shoot.play()
                player.bag.append("Gun")
                print("""
                                                                    Your bag contents are now %s.
                """ % player.bag)
                print("*" * 192)
                player.gamestop_count += 1
            elif player.gamestop_count >= 3 and player.gvisit_count == 1:
                print("""
                                                            As the events of what happened previously here still haunt you,
                                                            you decide not to go back in just yet to find out what you've been
                                                            wanting since your first visit.
                """)
                print("*" * 192)
                player.gvisit_count += 2
            elif player.gamestop_count >= 3 and player.gvisit_count >= 2:
                print("""
                                                        Hmm! You've seen all there is to see here! You wander back into the hall.
                """)
                print("*" * 192)


################ INTERACTION 2 ######################
        elif user_choice == "2":
            if player.stafflounge_count == 1:
                if "Lock-Picks" in player.bag:
                    print("""
                                                                You use your Lock-Picks to pick the locked door.
                                                                The staff lounge is pitch black and has an awful odor.
                                                                Once the door room opens it sheds only a little bit of
                                                                light into the room. You find the light switch on the wall
                                                                right next to the door and flip it.... 
                    """)
                    time.sleep(7)
                    print("""
                                                                Nothing happens.
                                                                
                                                                As you look into the room you see the furniture all in
                                                                disarray and the lights on the walls were smashed. With the 
                                                                light from the hall still just barely shinning through you 
                                                                see a lamp at the far end of the room. With nothing to hold 
                                                                the door open you make your way into the room the stench of 
                                                                something just keeps getting worse. As you turn on the lamp 
                                                                and turn around, the room is filled with bodies just torn to
                                                                shreds. 
                    """)
                    time.sleep(13)
                    print("""
                                                                On one of the couches you see a duffle bag and it
                                                                seems to be full of something. When you make your way to the
                                                                bag you trip over something.....
                    """)
                    time.sleep(5)
                    print("""
                                                                GGGRRRRR.....

                                                                As you stumble back to your feet you realise this big body 
                                                                building zombie had tripped you and is now getting up himself
                                                                and coming at you.
                    """)
                    print("*" * 192)
                    time.sleep(7)
                    while mall_zombie.health > 0 and player.health > 0:
                        zombieattack_art()
                        print("""
                                                                                    What do you want to do?

                                                                                    1. Run Away
                                                                                    
                                                                                    2. Punch""")
                        if "knife" in player.bag:
                            print("""
                                                                                    3. Use Knife""")
                        if "Gun" in player.bag:
                            print("""
                                                                                    4. Use Gun""")
                        user_input = input()
                        print("*" * 192)
                # Run Away
                        if user_input == "1":
                            player.health -= 20
                            mall_menu(player)
                # Punch
                        elif user_input == "2":
                            player.do_punch(mall_zombie)
                            punch.play()
                # Knife
                        elif user_input == "3" and "knife" in player.bag:
                            player.do_knife(mall_zombie)
                            knife.play()
                # Gun
                        elif user_input == "4" and "Gun" in player.bag:
                            player.do_shoot(mall_zombie)
                            shoot.play()

                        else:
                            # print("*" * 192)
                            print("""
                                                                You entered an invalid option and missed your chance to strike!
                            """)
                            print("*" * 192)
                # ZOMBIE ATTACKS!
                        if player.health > 0 and mall_zombie.health > 0:
                            time.sleep(1.5)
                            mall_zombie.do_punch(player)
                            punch.play()
                    
                        if player.health <= 0:
                            # print("*" * 192)
                            print("""
                                                                    The %s KILLED YOU!!! Better luck next time...
                            """ % (mall_zombie.name)
                            print("*" * 192)
                            player_dies()
                    
                        if mall_zombie.health <= 0:
                            # print("*" * 192)
                            print ("""
                                                                                %s KILLED %s!! 
                                                                                
                                                                                %s's health is %d.

                                                                ....Now what's inside that bag?
                                                                Majority of it is just work out clothes that are way too big 
                                                                and haven't been washed in forever. You come across a wallet.
                                                                ooohh $150.
                            """ % (player.name, mall_zombie.name, player.name, player.health))
                            print("*" * 192)
                            player.purse += 150
                            cash.play()
                            time.sleep(4)
                            print("""
                                                                                    You now have $%s.
                            """ % player.purse)
                            print("*" * 192)
                            player.stafflounge_count += 1
                elif "Lock-Picks" not in player.bag:
                    print("""
                                                                This door is locked! If only there were a way to pick the lock...
                    """)
                    print("*" * 192)
            elif player.stafflounge_count >= 2:
                print("""
                                                        Hmm! You've seen all there is to see here! You wander back into the hall.
                """)
                print("*" * 192)

################ INTERACTION 3 ######################
        elif user_choice == "3":
            if player.beretta_count == 1:
                    print("""
                                              You walk into Beretta which is on the main floor. Everything is still neat and organized
                                              as your walking through the store this mans voice starts talking to you from the other-side 
                                              of the store.

                                              "OH hey a customer"
                                              While walking towards the voice you shout out "Whose there?" Once you get to where the voice
                                              came from.
                                              The voice replies from the other side now "OOP im over here now"
                                              You think to yourself what the hell is going on while you walk towards the voice again.
                                              When you reach the counter you ask again "Who is .." the computer monitor turns around
                                              and says
                                              "Im giphy, the stores cashier haven't seen anyone in here in quite some time. I was built when
                                              all this mess started. How can I help you today we have a small variety of items still."
                    """)
                    print("*" * 192)
                    time.sleep(15)
                    print("")
            if "Gun" in player.bag and player.beretta_count >= 2 and player.dontvisit_count == 1:
                print("""
                                                        As you walk towards Beretta you notice something down one of the other
                                                        corridors that you have seen somewhere else...

                                                        You turn down that corridor and rush to check if you were just imagining it.
                """)
                time.sleep(5)
                print("""
                                                        You weren't .......

                                                        "What the hell you doing over here Fred?

                                                        "What the hell are you.. NO! NOO! NOOOOO!"

                                                        As you reach in your bag, to grab your Gun you continue walking towards him.....
                """)
                time.sleep(5)
                print("""
                                                        "No! What the hell you doing over her Fred? How did you get over here?" 

                                                        "Fred if you are real you better tell me right now."
                                                        
                                                        No answer from the mannequin...
                """)
                time.sleep(4)
                ar_15.play()
                time.sleep(2)
                print("""
                                                        You start shooting at him until he falls apart and hits the floor.

                                                        "DAMNIT FRED!!! DAMNIT!!!!"
                """)
                print("*" * 192)
                time.sleep(4)
                player.dontvisit_count += 5
            while True:
                if "Mask" in player.bag and "Respirator" in player.bag and "Sam's dog collar" in player.bag:
                    print("""
                                                                                  Sorry we are sold out of everything
                    """)
                    print("*" * 192)
                    player.beretta_count += 1
                    mall_menu(player)
                else:
                    # print("*" * 192)
                    player.beretta_count += 1
                    print("""
                                                                                What would you like to buy:
                                                                                
                                                                                1. Mask
                                                                                
                                                                                2. Respirator
                                                                                
                                                                                3. An old dog collar

                                                                                4.Nothing, Leave
                    """)
                    print("*" * 192)
########### PURCHASE Mask ########################################################
                    if user_input == "1" and "Mask" in player.bag:
                        # print("*" * 192)
                        print("""
                                                                                      Masks are sold out
                        """)
                        print("*" * 192)
                    elif user_input == "1" and "Mask" not in player.bag and player.purse < 25:
                        print("""
                                                                                You ain't got the cash, bub.
                        """)
                        print("*" * 192)
                    elif user_input == "1" and "Mask" not in player.bag and player.purse >= 25:
                        print("""
                                                                                        That'll be $25
                        """)
                        print("*" * 192)
                        cash.play()
                        player.purse -= 25
                        time.sleep(1.5)
                        player.bag.append("Mask")
                        zipper.play()
                        print("""
                                                                    Your bag contains %s and you now have $%d
                        """ % (player.bag, player.purse))
                        print("*" * 192)
########### PURCHASE Respirator ########################################################
                    elif user_input == "2" and "Respirator" in player.bag:
                        print("""
                                                                                  Respirators are sold out
                        """)
                        print("*" * 192)                    
                    elif user_input == "2" and "Respirator" not in player.bag and player.purse < 30:
                        print("""
                                                                                You ain't got the cash, bub.
                        """)
                        print("*" 192)
                    elif user_input == "2" and "Respirator" not in player.bag and player.purse >= 30:
                        print("""
                                                                                        That'll be $30
                        """)
                        print("*" * 192)
                        cash.play()
                        player.purse -= 30
                        time.sleep(1.5)
                        player.bag.append("Respirator")
                        zipper.play()
                        print("""
                                                                    Your bag contains %s and you now have $%d
                        """ % (player.bag, player.purse))
                        print("*" * 192)
########### PURCHASE DOG COLLAR ########################################################
                    elif user_input == "3" and "Sam's dog collar" in player.bag:
                        print("""
                                                                                You bought the only dog collar
                        """)
                        print("*" * 192)
                    elif user_input == "3" and "Sam's dog collar" not in player.bag and player.purse < 500:
                        print("""
                                                                                 You ain't got the cash, bub.
                        """)
                    elif user_input == "3" and "Sam's dog collar" not in player.bag and player.purse >= 500:
                        print("""
                                                                                        That'll be $500
                        """)
                        print("*" * 192)
                        cash.pay()
                        player.purse -= 500
                        time.sleep(1.5)
                        print("""
                                                                            As you wipe the dust off the collars name tag...
                                                                            Your eyes start to water up and bead down your
                                                                            face, as your dogs name was Sam..............
                        """)
                        be_alright.play()
                        player.bag.append("Sam's dog collar")
                        zipper.play()
                        print("""
                                                                Your bag contains %s and you now have $%d
                        """ % (player.bag, player.purse))
                        print("*" * 192)
                    if user_choice == "4":
                        print("*" * 192
                        mall_menu(player))

                
################ LEAVE Mall #######################
        elif user_choice == "4":
            print("*" * 192)
            location_menu(player)

############### INVALID ENTRY - LOOP RESETS #########
        else:
            print("""
                                                                                    Sorry I didn't get that.
            """)
            print("*" * 192)



########################################################################################################
############################# 4. DIGITALCRAFTS LOCATION & MENU FUNCTIONS ###############################
########################################################################################################

def digitalcrafts_location():
    mixer.music.load("audio/tron.mp3")
    mixer.music.play(-1)
    print("""
                                                                            You have arrived at Digital Crafts.                                

                                                    The flickering fluorescent lights shed scattered rays on an ominous scene.
                                                    You notice black computer monitors covered in dust. A coffee mug is shattered on a desk.
                                                    Cobwebs cover closed cabinets and chewed up rubber duckies litter the floor.
                                                    You could tell this once used to be a place of learning and success.
    """)
    print("*" * 192)
    time.sleep(2)
    crash.play()
    print("""
                                                                *Suddenly, you hear a loud crash coming from up the stairs.*

                                                                What's that!
                                                                You are not alone.
    """)
    print("*" * 192)

def digitalcrafts_menu(player):
    time.sleep(2)
    while True:
        print("""
                                                                                Where do you want to go? (1-4)
                                                                                
                                                                                1. Continue Down Hallway
                                                                                
                                                                                2. Head Upstairs
                                                                                
                                                                                3. Open Cabinet
                                                                                
                                                                                4. Leave Digital Crafts
        """)
        print("*" * 192)
        if user_choice == "1":
            if player.dc_hallway_count == 1:
                print("""
                                                                   You continue down the hallway.
                                                                   You are lead to an empty room at the end of the hallway.
                                                                   There you find a doll in the middle of the room.
                """)
                print("*" * 192)
                print("""
                                                                                    Would you like to pick it up? (Y/N) 
                """)
                yesorno = input()
                print("*" * 192)
                yesorno = yesorno.lower()
                if yesorno == "y":
                    print("""
                                                                                   You pick up the doll. 
                                                                                   Suddenly it releases a poisonous gas!
                    """)
                    print("*" * 192)
                    gas.play()
                    time.sleep(1)
                    print("""
                                                                                Your health takes a -10 hit.
                    """)
                    print("*" * 192)

                    player.health -= 10
                    player.dc_hallway_count += 1
                    print("""
                                                                                    %s's health: %d
                    """ % (player.name, player.health))
                    print("*" * 192)
            elif player.dc_hallway_count >= 2:
                print("""
                                                                Hmm! There's just the empty remnants of the poison doll here...
                                                                You head back into the hallway.
                """)
                print("*" * 192)
        elif user_choice == "2":
            if player.dc_sound_count == 1:
                print("""
                                                                                Your curiosity gets the best of you.
                                                                                Let us not hope curiosity kills the cat...

                                                                                You walk upstairs and investigate the sound.
                """)
                print("*" * 192)
                creak.play()
                time.sleep(2)
                print("""
                                                        The room is dark, but you make out a faint outline in the corner of the room.
                """)
                slow_breathing.play()
                time.sleep(2)
                print("""
                                                                                'Who goes there?!' Calls a voice.
                                                                                You answer back.

                                                            Suddenly, a man with a scraggly beard and kind but withered eyes appears.
                                                            He looks like he's been through a lot.
                """)
                time.sleep(2)
                print("""
                                                            'My name is Sean. I used to teach here at Digital Crafts... 
                                                            But that was a long time ago.
                                                            Since then, I haven't been able to leave the facility. 
                                                            Memories, ya know? 
                                                            But also, I'm a bit tied up.'

                                                            Sean shows you a battery pack hooked up to the wall. 
                                                            Sean is a cyborg.

                                                            'It's one of the few places in town that still has electricity...'

                                                            You look around and see he has a small pouch next to him.
                """)
                time.sleep(2)
                print("""
                                                          You want it? It's got some money in it. I don't need it anymore. (Y/N) 
                """)
                yesorno = input()
                print("*" * 192)
                yesorno = yesorno.lower()
                if yesorno == "y":
                    print("""
                                                                   Alright... But I won't let you just have all the answers!
                """)
                    print("""
                                                                                    You need a challenge - let's fight!
                    """)
                    print("*" * 192)
                    cyborgattack_art()
                    evildroid.play()
                    time.sleep(2)
                    print("Cyborg Sean challenges you to a duel!")
                    while cyborgsean.health > 0 and player.health > 0:
                        cyborgattack_art()
                                print("""
                                                                                    What do you want to do?

                                                                                    1. Run Away

                                                                                    2. Punch""")
                                if "knife" in player.bag:
                                    print ("""
                                                                                    3. Use Knife""")
                                if "Gun" in player.bag:
                                    print ("""
                                                                                    4. Use Gun""")
                                user_input = input()
                        # Run Away
                                if user_input == "1":
                                    player.health -= 20
                                    evil_laugh.play()
                                    print("""
                                                                      You choose to run away.
                                                                      You hear Cyborg Sean's voice echo in the distance.

                                                                      'Hah Hah Hah better luck next time.'
                                    """)
                                    print("*" * 192)
                                    digitalcrafts_menu(player)
                        # Punch
                                elif user_input == "2":
                                    player.do_punch(cyborgsean)
                                    punch.play()
                        # Knife
                                elif user_input == "3" and "knife" in player.bag:
                                    player.do_knife(cyborgsean)
                                    knife.play()
                        # Gun
                                elif user_input == "4" and "Gun" in player.bag:
                                    player.do_shoot(cyborgsean)
                                    shoot.play()

                                else:
                                    print("""
                                                                You entered an invalid option and missed your chance to strike!
                                    """)
                                    print("*" * 192)
                        
                        # CYBORG ATTACKS!
                                if player.health > 0 and cyborgsean.health > 0:
                                    time.sleep(1.5)
                                    cyborgsean.do_punch(player)
                                    punch.play()
                                
                                if player.health <= 0:
                                    print ("""
                                                                    CYBORG SEAN KILLED YOU!!! Better luck next time...
                                    """)
                                    print("*" * 192)
                                    player_dies()
                                
                                if cyborgsean.health <= 0:
                                    groan.play()
                                    print ("""
                                                                                %s KILLED %s!! 
                                                                                %s's health is %d.
                                                                                ....Now what?
                                    """ % (player.name, cyborgsean.name, player.name, player.health))
                                    print("*" * 192)
                                    player.dc_sound_count += 1
                                    time.sleep(1.5)
                                    cash.play()
                                    print("""
                                                                             You take the pocket money and leave.
                                    """)
                                    player.purse += 50
                                    print("""
                                                                                        You now have $%s.
                                    """ % (player.purse))
                                    print("*" * 192)
                else:
                    print("""
                                                                                        Okay. Bye bye.
                    """)
                    print("*" * 192)
            elif player.dc_sound_count >= 2:
                print("""
                                                              The mangled wreckage of Cyborg Sean lay sparking. 
                                                              You can hear him softly repeating "group debug... group debug..."
                """)
                print("*" * 192)
                groan.play()
        elif user_choice == "3":
            if player.dc_cabinet_count == 1:
                creak.play()
                print("""
                                                                      You sweep away the cobwebs and open the cabinet.
                                                                      You find some old sanitizer.
                """)
                player.bag.append("Sanitizer")
                zipper.play()
                print("""
                                                                                Your bag contents is now %s.
                """ % (player.bag))
                print("*" * 192)
                player.dc_cabinet_count += 1
            elif player.dc_cabinet_count >= 2:
                print("""
                                                            Hmm! The cabinet is empty... You've seen all there is to see here.
                """)
                print("*" * 192)
        elif user_choice == "4":
            print("""
                                                                              You dash out of there... Where to?
            """)
            print("*" * 192)
            location_menu(player)
        else:
            print("""
                                                                      BLOOP. Can't do that patna'. Please choose again. 
            """)




########################################################################################################
################################## 7. CDC LOCATION & MENU FUNCTIONS ####################################
########################################################################################################

def cdc_location():
    print("""
                                                            The Center for Disease Control may as well be ground zero.
                                                            Healthcare professionals used to work around the clock here, 
                                                            trying to produce a vaccine for the virus, while millions of people
                                                            named Karen denounced their efforts on facebook.

                                                            How close did they get? Nobody knows. The CDC was shut down
                                                            when a Maskless group of Karens gathered outside in protest.
                                                            You must get inside and find out.
    """)
    print("*" * 192)
    # time.sleep(5)
    print("""
                                                                                    What will you do next?
    """)
    print("*" * 192)
    # time.sleep(3)

def cdc_menu(player): 
    while True:

        print("""
                                                                                        1. Check the Lab 

                                                                                        2. Check the Cooler

                                                                                        3. Check the Immunology Wing

                                                                                        4. Leave
""")
print("*" * 192)
        if user_choice == "1":
            # time.sleep()
            print("""
                                                                You wander into the lab, careful not to touch anything.

                                                                There is an IV drip bag and some unused needles on the counter.

                                                                Your health could use a boost. 
            """)   
            print("*" * 192)
            print("""
                                                                                        1. Use IV
                                                                                        
                                                                                        2. Do not use IV
            """)
            user_input = input()
            print("*" * 192)
            if user_input == "1":
                player.health += 50
                print("""
                                                                                Your health increased by 50
                """)
                print("""
                                                                                %s's health: %d
                """ % (player.name,player.health))
                print("*" * 192)
                cdc_menu(player)  
                user_choice = input
            elif user_input == "2":
                print("""
                                                                            You can never be too careful, huh?
                """)
                print("*" * 192)
                cdc_menu(player)

    
        elif user_choice == "2":
            #time.sleep(2)
            print("""
                                                            You've heard the vaccine would have to be refrigerated.

                                                            The cooler on the second floor seems like a good place to investigate.

                                                            There's a small case of viles on the bottom shelf of the cooler...
""")   
            print("""
                                                                      You take out a vile. Its label reads 'ZomPanVac-20'

                                                                      You have the vaccine! But does it work?

                                                                      There's only one way to find out...
            """)   
            player.bag.append("Vaccine")
            print("""
                                                                                 1. Take the Vaccine
                                                                                
                                                                                 2. Do not take the Vaccine
            """)
            user_input = input()
            print("*" * 192)
            if user_input == "1" and player.vaccine_count == 1:
                player.health += 10000
                print("""
                                                                        It works! Your health increased by 10,000
                                                                        
                                                                                %s's health: %d
                """ % (player.name,player.health))
                print("*" * 192)
                player.vaccine_count += 1
                cdc_menu(player)
            elif user_input == "1" and player.vaccine_count >= 1:
                print("""
                                                                                Sorry, you had your chance...
                """)
                print("*" * 192)
                cdc_menu(player)
            elif user_input == "2":
                print("""
                                                                              You can never be too careful, huh?
                """)
                print("*" * 192)
                cdc_menu(player)

    
        
        elif user_choice == "3":
            if "Vaccine" in player.bag:
                print("""
                                                        You know the Immunology Wing will have the information you need to deploy the vaccine.

                                                        You go there to figure out how you can defeat the virus once and for all.

                                                        You open the door to the Immunology center. 

                                                        A massive, highly evolved mutant blocks your path...
                """)   
                print("*" * 192)
                    # time.sleep()                   
                while cdcZombie.health > 0 and player.health > 0:
                    zombieattack_art()
                    print("""
                                                                                    What do you want to do?
                                                                                    
                                                                                    1. Run Away

                                                                                    2. Punch
                    """)
                    if "knife" in player.bag:
                        print ("""
                                                                                    3. Use Knife""")
                    if "Gun" in player.bag:
                        print ("""
                                                                                    4. Use Gun
                        """)
                    
                    user_input = input()
                    print("*" * 192)
            # Run Away
                    if user_input == "1":
                        player.health -= 20
                        cdc_menu(player)
            # Punch
                    elif user_input == "2":
                        player.do_punch(cdcZombie)
                        punch.play()
            # Knife
                    elif user_input == "3":
                        player.do_knife(cdcZombie)
                        knife.play()
            # Gun
                    elif user_input == "4":
                        player.do_shoot(cdcZombie)
                        shoot.play()

                    else:
                        print("""
                                                                You entered an invalid option and missed your chance to strike!
                        """)
                        print("*" * 192)
                        #time.sleep(1.5)
            # ZOMBIE ATTACKS!
                    if player.health > 0 and cdcZombie.health > 0:
                        time.sleep(1.5)
                        cdcZombie.do_punch(player)
                        punch.play()
                    
                    if player.health <= 0:
                        print ("""
                                                                        The %s KILLED YOU!!! Better luck next time...
                        """ % (cdcZombie.name))
                        print("*" * 192)
                        player_dies()
                    
                    if cdcZombie.health <= 0:
                        you_win()

            elif "vaccine" not in player.bag:
                print("""
                                                                You must have the vaccine to access the Immunology Center...
                """)
                print("*" * 192)
                cdc_menu(player)

        
        elif user_choice == "4":
            print("""
                                                                      You couldn't be leaving any sooner... Where to?
            """)
            location_menu(player)


########################################################################################################
############################### END 7. CDC LOCATION & MENU FUNCTIONS ###################################
########################################################################################################