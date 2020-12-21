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

#name, species, health, charisma level, purse, sex, punch, knife, shoot, defense)
character1 = Character("Dr. Robert Neville", 100, 500, "Male", "low", 24, 49, "high")
character2 = Character("Sherlock", 100, 400, "Female", "medium", 24, 49, "high")
character3 = Character("Carl Grimes", 100, 600, "Male", "high", 24, 49, "low")
character4 = Character("Chico Dusty", 100, 1000, "Male", "high", 24, 49, "low")
pubZombie = Character("Pub Zombie", 40, 100, "Male", "low", 0, 0, "low")
cyborgsean = Character("Cyborg Sean", 60, 100, "Male", "low", 0, 0, "medium")
hs_zombie = Character("Lunch Lady Zombie", 80, 100, "Female", "low", 0, 0, "medium")
#pub = Location("The Pub", "your favorite watering hole", "Bar Area", "Bathroom", "Dart Board")

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
        "Punch:", char1.punch.title(), char2.punch.title(), char3.punch.title(), char4.punch.title()))
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
2. Sherlock
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
Ahhh, Sherlock. It took quite some time
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
####################################### SELECT LOCATION FUNCTION #######################################
########################################################################################################

def location_menu(player):
# Looping user input to choose location
    while True:
        location_choice = input("""
1. The Pub
2. The High School
3. The Stadium
4. DigitalCrafts
5. Check Health
6. Check Bag

""")
        if location_choice == "1":
            pub_location()
            pub_menu(player)
        elif location_choice == "2":
            highschool_location()
            highschool_menu(player)
        elif location_choice == "3":
            stadium_location()
            stadium_menu(player)
        elif location_choice == "4":
            digitalcrafts_location()
            digitalcrafts_menu(player)
        elif location_choice == "5":
            player.print_status()
        elif location_choice == "6":
            player.bag_contents()   
        else:
            print("Enter \"1\", \"2\", \"2\", \"3\", \"4\", \"5\", or \"6\"")
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
    # time.sleep(5)
    print("What will it be?")
    # time.sleep(3)

def pub_menu(player): 
    bartenderencounter = 1
    while True:

# IF PUB ZOMBIE IS ALIVE:

            if pubZombie.health > 0:
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
                    pub_menu(player)
            
                
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
His mouth is.....      Bleeding?
""")
                        #///time.sleep(5)
                        print("""
ZOMBIE ATTACK!
""")
                        # INPUT ZOMBIE BARTENDER SOUND
                        # time.sleep()                   
                        while pubZombie.health > 0 and player.health > 0:
                            print("\nWhat do you want to do?")
                            print("1. Run Away")
                            print("2. Punch")
                            if player.knife >= 25:
                                print ("3. Use Knife")
                            # if player.shoot_power > 0:
                            #     print ("4. Use Gun")
                            user_input = input()
                    # Run Away
                            if user_input == "1":
                                player.health -= 20
                                location_menu(player)
                    # Punch
                            elif user_input == "2":
                                player.do_punch(pubZombie)
                    # Knife
                            elif user_input == "3":
                                player.do_knife(pubZombie)
                    # Gun
                            # elif user_input == "4":
                            #     shoot(player.shoot, zombie)

                            else:
                                print("You entered an invalid option and missed your chance to strike!")
                                #time.sleep(1.5)
                    # ZOMBIE ATTACKS!
                            if player.health > 0 and pubZombie.health > 0:
                                # Opponent attacks player
                                pubZombie.do_punch(player)
                            
                            if player.health <= 0:
                                print ("The %s KILLED YOU!!! Better luck next time...")
                                quit
                            
                            if pubZombie.health <= 0:
                                print ("""
                            
%s KILLED %s!! 
%s's health is %d.

....Now what?""" % (player.name, pubZombie.name, player.name, player.health))
                        bartenderencounter += 1

                    elif bartenderencounter > 2:
                        print("The bartender is dead")
                        pub_menu(player)


                elif user_choice == "3":
                    print("""
You can't help but acknowledge the two gorgeous young ladies at the end of the bar.
You approach them...
""")
                    #time.sleep(5)
                    print("""
"How are you, ladies?"
""")
                    # INPUT LADIES SOUND
                    # time.sleep()
                    print("""
\"Get lost, creep,\" says the older, less attractive one.
                    
Today may not be your day...""")
                    pub_menu(player)                
                    
                elif user_choice == "4":
                    print("You couldn't be leaving any sooner... Where to?")
                    location_menu(player)
        
            else:

# IF PUB ZOMBIE IS DEAD:

                user_choice = input("""
1. Have a Pint 
2. Approach the Young Ladies
3. Leave

""")
                if user_choice == "1":
                    # INPUT SOUNDBOARD OF POURING A BEER
                    # time.sleep()
                    # self.getdrunk()
                    print("Will you have another?")
                    pub_menu(player)

                elif user_choice == "2":
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
                    print("""
\"Hey there, handsome\" says the pale, glassy eyed brunette, 
in a slow, almost infectious drawl. "You saved us from that plague of a bartender.
We thought we were history."

"Just an instinct these days," you reply, as you notice the color
running away from her face.

"Here," she says. "Take this." As she pulls a large, glinting
blade from her handbag. "I'm not much with it. But it may help you next time..."
""")            
                    player.knife += 1
                    player.add_item("knife")
                    pub_menu(player)  
                
                    
                elif user_choice == "3":
                    print("You couldn't be leaving any sooner... Where to?")
                    location_menu(player)
            

########################################################################################################
############################### END 1. PUB LOCATION & MENU FUNCTIONS ###################################
########################################################################################################





########################################################################################################
################################## 2. HIGH SCHOOL LOCATION & MENU FUNCTIONS ####################################
########################################################################################################

def highschool_location():
    print("*" * 20)
    print("""
You arrive at an abandoned high school...
The smell of rotting food floats through the air.
You think you see a shadowy figure step behind a wall on the far side of the building.
The front doors are locked, but you notice a window that's been left ajar.
You climb through to find yourself in a dark hallway.
          """)
    print("*" * 20)

def highschool_menu(player):
    classroom_count = 1
    cafeteria_count = 1
    auditorium_count = 1

    while True:
            user_choice = input("Where do you want to go? (1-4)\n1. Classroom\n2. Cafeteria\n3. Auditorium\n4. Leave High School\nEnter selection here: ")

################ INTERACTION 1 ######################
            if user_choice == "1":
                if classroom_count == 1:
                    print("*" * 20)
                    print(""" 
You walk into the classroom down the hall. 
There are few desks overturned and the chalk-board on the wall is crooked...
It looks like there was some sort of struggle in here. 
Something shiny catches your eye under one of the desks... 
It's a little lock-picking kit! Must have belonged to a misbehaving highscooler!
You pick it up and slip it in your bag. 
You wander back into the hall.
                          """)
                    print("*" * 20)
                    player.bag.append("Lock-picking Kit")
                    print("Your bag contents is now %s." % player.bag)
                    classroom_count += 1
                elif classroom_count >= 2:
                    print("*" * 20)
                    print("")
                    print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                    print("")
                    print("*" * 20)

################ INTERACTION 2 ######################
            elif user_choice == "2":
                if cafeteria_count == 1:
                    print("*" * 20)
                    print("""
The cafeteria reveals the source of the horrid smell. 
The freezers have been left open for days,
and the putrid food has been plundered thrown all over the cafeteria by someone...
... or something.
You hear the sound of a sink running coming from the kitchen.
Is someone in there? You approach the door and push it open.
What you see next sets your heart racing:
The beloved high school lunch lady is laying on the ground with her head turned.
You run up to check if she is still breathing. No breath. No pulse.
But is that her arm...... moving???
ZOMBIE ATTACK!")
                    """)
                    print("*" * 20)
                    while hs_zombie.health > 0 and player.health > 0:
                        print("\nWhat do you want to do?")
                        print("1. Run Away")
                        print("2. Punch")
                        # if player.knife_power > 0:
                        #     print ("3. Use Knife")
                        # if player.shoot_power > 0:
                        #     print ("4. Use Gun")
                        user_input = input()
                # Run Away
                        if user_input == "1":
                            player.health -= 20
                # Punch
                        elif user_input == "2":
                            player.do_punch(hs_zombie)
                # Knife
                        # elif user_input == "3":
                        #     knife(player.knife, zombie)   
                # Gun
                        # elif user_input == "4":
                        #     shoot(player.shoot, zombie)

                        else:
                            print("You entered an invalid option and missed your chance to strike!")
                            #time.sleep(1.5)
                # ZOMBIE ATTACKS!
                        if player.health > 0:
                            # Opponent attacks player
                            hs_zombie.do_punch(player)
                        
                        if player.health <= 0:
                            print ("The %s KILLED YOU!!! Better luck next time...")
                            quit
                        
                        if hs_zombie.health <= 0:
                            print ("""
%s KILLED %s!! 
%s's health is %d.
....Now what?""" % (player.name, hs_zombie.name, player.name, player.health))
                    cafeteria_count += 1
                elif cafeteria_count >= 2:
                    print("*" * 20)
                    print("")
                    print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                    print("")
                    print("*" * 20)

################ INTERACTION 3 ######################
            elif user_choice == "3":
                if "Lock-picking Kit" in player.bag:
                    if auditorium_count == 1:
                        print("*" * 20)
                        print("""
You use your lock-picking kit to pick the locked door.
You enter the school auditorium, which is cool and dark.
The large burgundy curtains hanging over the stage are ripped and tattered.
To your left is the sound booth, so you decide to investigate.
As soon as you open the saloon-style door, you notice a $25 bill on the floor benieth the sound board.
Neat!
                            """)
                        player.purse += 25
                        print("You added $25 to your purse! The contents of your purse is now %s!" % player.purse)
                        auditorium_count += 1
                    elif auditorium_count >= 2:
                        print("*" * 20)
                        print("")
                        print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                        print("")
                        print("*" * 20)
                else:
                    print("This door is locked! If only there were a way to pick the lock...")
################ LEAVE SCHOOL #######################
            elif user_choice == "4":
                location_menu(player)

############### INVALID ENTRY - LOOP RESETS #########
            else:
                
                print("Sorry I didn't get that.")




########################################################################################################
############################# 4. DIGITALCRAFTS LOCATION & MENU FUNCTIONS ###############################
########################################################################################################

def digitalcrafts_location():
    # insert an effect that makes the text show up character by character 
    print("""
You have arrived at Digital Crafts.
The flickering fluorescent lights shed scattered rays on an ominous scene.
You notice black computer monitors covered in dust. A coffee mug is shattered on a desk.
Cobwebs cover closed cabinets and chewed up rubber duckies litter the floor.
You could tell this once used to be a place of learning and success.
""")
    #time.sleep(3)
    # insert sound effect!!
    print("""
*Suddenly, you hear a loud crash coming from up the stairs.*
What's that!
You are not alone.
""")

def digitalcrafts_menu(player):
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
                player.health -= 10
                # want to return character stats
                print("%s's health: %d" % (player.name, player.health))
                actionlist.pop(0)
                print(actionlist)
                # how to loop around with new changes
                digitalcrafts_menu(player)
            else:
                digitalcrafts_menu(player)
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
            yesorno = input("'You want it? It's got some money in it. I don't need it anymore.' (Y/N)" )
            if yesorno == "Y":
                print("""
Alright... But I won't let you just have all the answers!
You need a challenge - let's fight!""")
                print("Cyborg Sean challenges you to a duel!")
                while cyborgsean.health > 0 and player.health > 0:
                            print("\nWhat do you want to do?")
                            print("1. Run Away")
                            print("2. Punch")
                            if player.knife >= 25:
                                print ("3. Use Knife")
                            if player.shoot >= 50:
                                print ("4. Use Gun")
                            user_input = input()
                    # Run Away
                            if user_input == "1":
                                player.health -= 20
                                location_menu(player)
                    # Punch
                            elif user_input == "2":
                                player.do_punch(cyborgsean)
                    # Knife
                            elif user_input == "3":
                                player.do_knife(cyborgsean)
                    # Gun
                            elif user_input == "4":
                                player.do_shoot(cyborgsean)

                            else:
                                print("You entered an invalid option and missed your chance to strike!")
                                #time.sleep(1.5)
                    # ZOMBIE ATTACKS!
                            if player.health > 0 and cyborgsean.health > 0:
                                # Opponent attacks player
                                cyborgsean.do_punch(player)
                            
                            if player.health <= 0:
                                print ("The %s KILLED YOU!!! Better luck next time...")
                                quit
                            
                            if cyborgsean.health <= 0:
                                print ("""
                            
%s KILLED %s!! 
%s's health is %d.

....Now what?""" % (player.name, cyborgsean.name, player.name, player.health))
                digitalcrafts_menu(player)

            else:
                print("Okay. Bye bye.")
                digitalcrafts_menu(player)
        elif action == "3":
            print("""
You sweep away the cobwebs and open the cabinet.
You find some old sanitizer.
            """)
            player.bag.append("Sanitizer")
            print(player.bag)
            actionlist.pop(2)
            print(actionlist)
            digitalcrafts_menu(player)

        elif action == "4":
            location_menu(player)
        else:
            print("BLOOP. Can't do that patna'. Please choose again. ")

# # Cyborg Sean fight!
# def sean_fight(player, zombie):
#     print("Cyborg Sean challenges you to a duel!")
#     while player.health > 0:
#         action = input("""
#         What will you do? 
#         1. Punch
#         2. Knife
#         3. Shoot
#         4. Flee
#         """)
#         if action == "1":
#             player.do_punch(cyborgsean)
#         elif action == "2":
#             player.do_knife(cyborgsean)
#         elif action == "3":
#             player.do_shoot(cyborgsean)
#         elif action == "4":
#             digitalcrafts_menu(player)
#         else:
#             print("BLOOP. Can't do that patna'. Please choose again. ")