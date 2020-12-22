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

#########################name, ###########health, purse, sex, punch, knife, shoot, defense)
character1 = Character("Dr. Robert Neville", 100, 500, "Male", "medium", "high")
character2 = Character("Sherlock", 100, 400, "Female", "medium", "high")
character3 = Character("Carl Grimes", 100, 600, "Male", "high", "low")
character4 = Character("Chico Dusty", 100, 1000, "Male", "high", "low")
pubZombie = Character("Pub Zombie", 40, 100, "Male", "low", "low")
cyborgsean = Character("Cyborg Sean", 60, 100, "Male", "low", "medium")
hs_zombie = Character("Lunch Lady Zombie", 80, 100, "Female", "low", "medium")
mall_zombie = Character("Body Building Zombie", 90, 100, "Male", "medium", "medium")
plot_zombie = Character("Parking Lot Zombie", 40, 100, "Male", "low", "low")



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
############################################ def SELECT A PLAYER #######################################
########################################################################################################

def player_selection():
    print_character_menu("1. ", character1, "2. ",character2, "3. ",character3, "4. ",character4)

# Looping user input to choose character
    while True:
        print("-" * 192)
        character_choice = input("""
                                                                                    1. Doctor Robert Neville
                                                                                    2. Sherlock
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
            print("""
                                                                        Ahhh, Sherlock. It took quite some time
                                                                        to gather your wits. They say that is a side effect
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
        location_choice = input("""
                                                                                    1. The Pub
                                                                                    2. The High School
                                                                                    3. The Mall
                                                                                    4. DigitalCrafts
                                                                                    5. Check Health
                                                                                    6. Check Bag
        """)
        print("-" * 192)
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
        else:
            print("""
                                                                                Enter \"1\", \"2\", \"3\", \"4\", \"5\", or \"6\"
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
    # time.sleep(5)
    print("What will it be?")
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
                if user_choice == "1":
                    print("That'll be $5")
                    # INPUT SOUNDBOARD OF POURING A BEER
                    # time.sleep()
                    # self.getdrunk()
                    player.purse -= 5
                    pint_count += 1
                    user_choice = input("Will you have another?\n1. Yes\n2. No\n")
                    if user_choice == "1" and pint_count <= 5:
                        player.purse -= 5
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
                        time.sleep(5)
                        print("You wake up at home not remembering what happened last night.")
                        location_menu(player)
                    if user_choice == "1" and pint_count >= 6:
                        print("""
                        I think its time to go home..........
                        .....................................

                        You wake up at home now what?
                        """)
                        location_menu(player)
                    if user_choice == "2":
                        pub_menu(player)
                    
                elif user_choice == "2":
                    #time.sleep(2)
                    
                    if player.bartenderencounter == 1:
                        print("""
You approach the bar. The bartender greets you with a smile..
"The usual?" he says, as he pours your whiskey.
It's nice to be here..
""")
                        #time.sleep(5)
                        # INPUT ZOMBIE BARTENDER SOUND
                        # time.sleep()
                        #/print("new menu to either talk to the girls or leave?")
                        player. bartenderencounter += 1

                    elif player.bartenderencounter == 2:
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
                            if "knife" in player.bag:
                                print ("3. Use Knife")
                            if "gun" in player.bag:
                                print ("4. Use Gun")
                            user_input = input()
                    # Run Away
                            if user_input == "1":
                                player.health -= 20
                                location_menu(player)
                    # Punch
                            elif user_input == "2":
                                player.do_punch(pubZombie)
                    # Knife
                            elif user_input == "3" and "knife" in player.bag:
                                player.do_knife(pubZombie)
                    # Gun
                            elif user_input == "4" and "gun" in player.bag:
                                player.do_shoot(pubZombie)

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
                        player.bartenderencounter += 1

                    elif player.bartenderencounter > 2:
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
                    print("That'll be $5")
                    player.purse -= 5
                    pint_count += 1
                    user_choice = input("Will you have another?\n1. Yes\n2. No\n")
                    if user_choice == "1" and pint_count <= 5:
                        player.purse -= 5
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
                        time.sleep(5)
                        print("You wake up at home not remembering what happened last night.")
                        location_menu(player)
                    if user_choice == "1" and pint_count >= 6:
                        print("""
                        I think its time to go home..........
                        .....................................

                        You wake up at home now what?
                        """)
                        location_menu(player)
                    if user_choice == "2":
                        pub_menu(player)
                    # pub_menu(player)

                elif user_choice == "2":
                    if player.ladies_count == 1:
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
                        player.ladies_count += 1
                        pub_menu(player)
                    elif player.ladies_count >= 2:
                        print("""
"That was some showing with the bartender. Hope the knife we gave you helps..."
""")                
                    
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
    while True:
        user_choice = input("Where do you want to go? (1-4)\n1. Auditorium\n2. Cafeteria\n3. Classroom\n4. Leave High School\nEnter selection here: ")

################ INTERACTION 1 ######################
        if user_choice == "1":
            if player.auditorium_count == 1:
                if "Lock-picking Kit" in player.bag:
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
                        player.auditorium_count += 1
                else:
                    print("*" * 20)
                    print("")
                    print("This door is locked! If only there were a way to pick the lock...")
                    print("")
                    print("*" * 20)
            elif player.auditorium_count >= 2:
                print("*" * 20)
                print("")
                print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                print("")
                print("*" * 20)

################ INTERACTION 2 ######################
        elif user_choice == "2":
            if player.cafeteria_count == 1:
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
                    if "knife" in player.bag:
                        print ("3. Use Knife")
                    if "gun" in player.bag:
                        print ("4. Use Gun")
                    user_input = input()
            # Run Away
                    if user_input == "1":
                        player.health -= 20
            # Punch
                    elif user_input == "2":
                        player.do_punch(hs_zombie)
            # Knife
                    elif user_input == "3" and "knife" in player.bag:
                        player.do_knife(hs_zombie)
            # Gun
                    elif user_input == "4" and "gun" in player.bag:
                        player.do_shoot(hs_zombie)

                    else:
                        print("You entered an invalid option and missed your chance to strike!")
                        #time.sleep(1.5)
            # ZOMBIE ATTACKS!
                    if player.health > 0:
                        # Opponent attacks player
                        hs_zombie.do_punch(player)
                    
                    if player.health <= 0:
                        print ("The %s KILLED YOU!!! Better luck next time..." % hs_zombie)
                        quit()
                    
                    if hs_zombie.health <= 0:
                        print ("""
%s KILLED %s!! 
%s's health is %d.
....Now what?""" % (player.name, hs_zombie.name, player.name, player.health))
                player.cafeteria_count += 1
            elif player.cafeteria_count >= 2:
                print("*" * 20)
                print("")
                print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                print("")
                print("*" * 20)

################ INTERACTION 3 ######################
        elif user_choice == "3":
            if player.classroom_count == 1:    
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
                print("Your bag contents are now %s." % player.bag)
                player.classroom_count += 1
            elif player.classroom_count >= 2:
                print("*" * 20)
                print("")
                print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                print("")
                print("*" * 20)
                
################ LEAVE SCHOOL #######################
        elif user_choice == "4":
            location_menu(player)

############### INVALID ENTRY - LOOP RESETS #########
        else:
            
            print("Sorry I didn't get that.")

########################################################################################################
############################# 3. MALL LOCATION & MENU FUNCTIONS ########################################
########################################################################################################


def mall_location():
    print("*" * 20)
    print("""
    Oooh, the mall. You haven't came here in forever!!! You remember coming here
    with your friends to hang out and meet new people. Instead of the amazing smell
    of all the different types of food, from the food market, it now smells like 
    rotting flesh. As you are walking towards the entrance from the parking lot
    all the abandoned cars windows are shattered and scattered across the ground.
    Loud crunching of the glass echos out........
        """)
    print("*" * 20)
    time.sleep(4)

def mall_menu(player): 
    while plot_zombie.health > 0 and player.health > 0:
        print("*" * 20)
        print("""
        Just as you are about to reach the entrance you hear a deep growling voice 
        coming from behind one of the cars in the first row of the parking lot...
        It has heard the loud crunching and is slowly making it's way to you.
        """)
        time.sleep(2)
        print("")
        print("*" * 20)
        print("\nWhat do you want to do?")
        print("1. Run Away")
        print("2. Punch")
        if "knife" in player.bag:
            print ("3. Use Knife")
        if "gun" in player.bag:
            print ("4. Use Gun")
        user_input = input()
        if user_input == "1":
            player.health -= 20
    # Punch
        if user_input == "2":
            player.do_punch(plot_zombie)
# Knife
        if user_input == "3" and "knife" in player.bag:
            player.do_punch(plot_zombie)
# Gun
        if user_input == "4":
            player.do_shoot(plot_zombie)
        else:
            print("*" * 20)
            print("you entered an invalid option and zombie struck you!")
            print("*" * 20)

        if player.health > 0:
        # Opponent attacks player
            plot_zombie.do_punch(player)
        if player.health <= 0:
            print("*" * 20)
            print ("The %s KILLED YOU!!! Better luck next time..." % (plot_zombie.name))
            print("*" * 20)
        if plot_zombie.health <= 0:
            print("*" * 20)
            print ("""%s KILLED %s!! 
            %s's health is %d.
            ....Now what?""" % (player.name, plot_zombie.name, player.name, player.health))
            print("*" * 20)

    while True:
        user_choice = input("Where do you want to go? (1-4)\n1. Gamestop\n2. Staff Lounge\n3. Beretta\n4. Leave Mall\nEnter selection here: ")

################ INTERACTION 1 ######################
        if user_choice == "1":
            if player.gamestop_count == 1:
                print("*" * 20)
                print(""" 
                You are walking toward GameStop which is in the middle of the Plaza level. 
                There are mannequins everywhere and graffiti written all of the walls...
                As you are right outside of the doors you notice 2 mannequins, one is 
                a male mannequin wearing an orange hoodie. The other a female mannequin
                wearing a black hat covering her face, as well as a black leather jacket.
                I guess ill just name you Fred and Marge. When you enter something catches
                your eye.
                """)
                print("*" * 20)
                time.sleep(4)
                print("""
                You walk over to the mannequin behind the cashier counter and ask

                Aye hank whose the girl in the uuuggghh........

                Nvm aye maybe another time.
                """)
                print("*" * 20)
                time.sleep(2)
                player.gamestop_count += 1
            elif player.gamestop_count == 2:
                print("*" * 20)
                print("""
                While opening the door to GameStop you say
                'Aye morning Marge, morning Fred, anything new happen since
                I've been gone? Just as you ask you notice someone has been 
                in here since all the videos on the shelf have been rummaged 
                through. As you look around you hear a faint moan and some 
                coughing.... 
                """)
                print("*" * 20)
                time.sleep(5)
                print("""
                When you approach the distressed noises, you walk over
                a dead zombie, to see a man pointing a gun at you. He says                 
                "Hands up.. cough.. cough.. Thats far enough" 
                As you tell him you are not infected and was just coming to check
                what was happening.
                He then states "I need you to do something for me cough.. cough.. 
                as obviously I am not going to make it much longer if you couldn't
                tell already." 
                Sure what do you need some bandages?
                "No, here take this" as he hands you the gun "Before I turn into one
                of those things I need you to stop that from happening!
                But....
                "No buts cough.. cough.. I would hate for my body to be one of them
                cough.. grr.. and walking around attacking people grr.. cough.. do it
                now or it's going to be late grrr...
                BOOM........................
                """)
                print("*" * 20)
                time.sleep(2)
############### ADD GUN SHOT                
                player.bag.append("gun")
                print("Your bag contents are now %s." % player.bag)
                print("*" * 20)
                player.gamestop_count += 1
            elif player.gamestop_count >= 3 and player.gvisit_count == 1:
                print("*" * 20)
                print("")
                print("""
                As the events of what happened previously here still haunt you,
                you decide not to go back in just yet to find out what you've been
                wanting since your first visit.
                """)
                print("*" * 20)
                player.gvisit_count += 2
            elif player.gamestop_count >= 3 and player.gvisit_count >= 2:
                print("*" * 20)
                print("")
                print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                print("")
                print("*" * 20)


################ INTERACTION 2 ######################
        elif user_choice == "2":
            if player.stafflounge_count == 1:
                if "Lock-picking Kit" in player.bag:
                    print("*" * 20)
                    print("""
                    You use your lock-picking kit to pick the locked door.
                    The staff lounge is pitch black and has an awful odor.
                    Once the door room opens it sheds only a little bit of
                    light into the room. You find the light switch on the wall
                    right next to the door and flip it and nothing happens.
                    As you look into the room you see the furniture all in
                    disarray and the lights on the walls were smashed. With the 
                    light from the hall still just barely shinning through you 
                    see a lamp at the far end of the room. With nothing to hold 
                    the door open you make your way into the room the stench of 
                    something just keeps getting worse. As you turn on the lamp 
                    and turn around the room is filled with bodies just torn to
                    shreds. On one of the couches you see a duffle bag and it
                    seems to be full of something. When you make your way to the
                    bag you trip over something.....
                    """)
                    print("*" * 20)
                    time.sleep(4)
                    print("""
                    GGGRRRRR.....

                    As you stumble back to your feet you realise this big body 
                    building zombie had tripped you and is now getting up himself
                    and coming at you.
                    """)
                    print("*" * 20)
                    time.sleep(3)
                    while mall_zombie.health > 0 and player.health > 0:
                        print("\nWhat do you want to do?")
                        print("1. Run Away")
                        print("2. Punch")
                        if "knife" in player.bag:
                            print("3. Use Knife")
                        if "gun" in player.bag:
                            print("4. Use Gun")
                        user_input = input()
                        print("*" * 20)
                # Run Away
                        if user_input == "1":
                            player.health -= 20
                # Punch
                        elif user_input == "2":
                            player.do_punch(mall_zombie)
                # Knife
                        elif user_input == "3" and "knife" in player.bag:
                            player.do_knife(mall_zombie)
                # Gun
                        elif user_input == "4" and "gun" in player.bag:
                            player.do_shoot(mall_zombie)

                        else:
                            # print("*" * 20)
                            print("You entered an invalid option and missed your chance to strike!")
                            print("*" * 20)
                        #time.sleep(1.5)
                # ZOMBIE ATTACKS!
                        if player.health > 0:
                            # Opponent attacks player
                            mall_zombie.do_punch(player)
                    
                        if player.health <= 0:
                            # print("*" * 20)
                            print("The %s KILLED YOU!!! Better luck next time...") % (mall_zombie.name)
                            print("*" * 20)
                            quit
                    
                        if mall_zombie.health <= 0:
                            # print("*" * 20)
                            print ("""
                            %s KILLED %s!! 
                            %s's health is %d.
                            ....Now whats inside that bag?

                            Majority of it is just work out clothes that are way to big 
                            and haven't been washed in forever. You come across a wallet.
                            ooohh $150.
                            """ % (player.name, mall_zombie.name, player.name, player.health))
                            player.purse += 150
                            time.sleep(4)
                            print("*" * 20)
                            print("You now have $%s." % player.purse)
                            print("*" * 20)
                            player.stafflounge_count += 1
                elif "Lock-picking Kit" not in player.bag:
                    print("*" * 20)
                    print("")
                    print("This door is locked! If only there were a way to pick the lock...")
                    print("")
                    print("*" * 20)
            elif player.stafflounge_count >= 2:
                print("*" * 20)
                print("")
                print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                print("")
                print("*" * 20)

################ INTERACTION 3 ######################
        elif user_choice == "3":
            while True:
                if "gun" in player.bag and player.beretta_count >= 2 and player.dontvisit_count == 1:
                    print("*" * 20)
                    print("""
                    As you walk towards Beretta you notice something down one of the other
                    corridors that you have seen somewhere else...

                    You turn down that corridor and rush to check if you were just imagining it.

                    You weren't .......

                    "What the hell you doing over here Fred?

                    "What the hell are you.. NO! NOO! NOOOOO!"

                    As you reach in your bag, to grab your gun you continue walking towards him.....

                    "No! What the hell you doing over her Fred? How did you get over here?" 

                    "Fred if you are real you better tell me right now."
                    
                    No answer from the mannequin...

                    You start shooting at him until he falls apart and hits the floor.

                    "DAMNIT FRED!!! DAMNIT!!!!"
                    """)
                    print("*" * 20)
                    time.sleep(5)
                    player.dontvisit_count += 5

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
                    print("*" * 20)
                    time.sleep(4)
                    print("")
                    while True:
                        if "mask" in player.bag and "respirator" in player.bag and "Sam's dog collar" in player.bag:
                            print("Sorry we are sold out of everything")
                            print("*" * 20)
                            player.beretta_count += 1
                            mall_menu(player)
                        else:
                            # print("*" * 20)
                            print(player.itemslist)
                            print("")
                            user_input = input("What would you like to buy (1-3) ")
                            print("*" * 20)
                            if user_input == "1" and "mask" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $25")
                                print("*" * 20)
                                player.purse -= 25
                                player.bag.append("mask")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                print("*" * 20)
                            elif "mask" in player.bag:
                                # print("*" * 20)
                                print("Masks are sold out")
                                print("*" * 20)
                            if user_input == "2" and "respirator" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $30")
                                print("*" * 20)
                                player.purse -= 30
                                player.bag.append("respirator")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                print("*" * 20)
                            elif "respirator" in player.bag:
                                # print("*" * 20)
                                print("Respirator are sold out")
                                print("*" * 20)
                            if user_input == "3" and "Sam's dog collar" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $500")
                                print("*" * 20)
                                player.purse -= 500
                                player.bag.append("Sam's dog collar")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                print("*" * 20)
                            elif "Sam's dog collar" in player.bag:
                                # print("*" * 20)
                                print("You bought the only dog collar")
                                # print("*" * 20)
                            if "Sam's dog collar" in player.bag and "respirator" in player.bag and "mask" in player.bag:
                                # print("*" * 20)
                                print("Everything is sold out. Thanks for visiting check back soon to see if we have more supplies.")
                                print("*" * 20)
                                player.beretta_count += 1
                                mall_menu(player)
                            else:
                                # print("*" * 20)
                                print("Will there be anything else youd like to buy?")
                                print("*" * 20)
                                user_choice = input("(y/n) ").lower()
                                if user_choice != "n":
                                    # print("*" * 20)
                                    print("ALRIGHTY THEN")
                                    print("*" * 20)
                                if user_choice == "n":
                                    print("*" * 20)
                                    player.beretta_count += 1
                                    mall_menu(player)
                            player.beretta_count += 1
                if player.beretta_count >= 2:
                    while True:
                        if "mask" in player.bag and "respirator" in player.bag and "Sam's dog collar" in player.bag:
                            # print("*" * 20)
                            print("Sorry we are sold out of everything")
                            print("*" * 20)
                            player.beretta_count += 1
                            mall_menu(player)
                        else:
                            # print("*" * 20)
                            print(player.itemslist)
                            print("")
                            user_input = input("What would you like to buy (1-3) ")
                            print("*" * 20)
                            if user_input == "1" and "mask" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $25")
                                print("*" * 20)
                                player.purse -= 25
                                player.bag.append("mask")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                print("*" * 20)
                            elif "mask" in player.bag:
                                # print("*" * 20)
                                print("Masks are sold out")
                                print("*" * 20)
                            if user_input == "2" and "respirator" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $30")
                                print("*" * 20)
                                player.purse -= 30
                                player.bag.append("respirator")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                print("*" * 20)
                            elif "respirator" in player.bag:
                                # print("*" * 20)
                                print("Respirator are sold out")
                                print("*" * 20)
                            if user_input == "3" and "Sam's dog collar" not in player.bag:
                                # print("*" * 20)
                                print("That'll be $500")
                                print("*" * 20)
                                player.purse -= 500
                                player.bag.append("Sam's dog collar")
                                # print("*" * 20)
                                print("Your bag contains %s and you now have $%d" % (player.bag, player.purse))
                                # print("*" * 20)
                            elif "Sam's dog collar" in player.bag:                         
                                # print("*" * 20)
                                print("You bought the only dog collar")
                                print("*" * 20)
                            if "Sam's dog collar" in player.bag and "respirator" in player.bag and "mask" in player.bag:
                                # print("*" * 20)
                                print("Everything is sold out, Thanks for visiting check back soon to see ")
                                print("*" * 20)
                                player.beretta_count += 1
                                mall_menu(player)
                            else:
                                # print("*" * 20)
                                print("Will there be anything else youd like to buy?")
                                print("")
                                user_choice = input("(y/n) ").lower()
                                print("*" * 20)
                                if user_choice != "n":
                                    # print("*" * 20)
                                    print("")
                                    print("ALRIGHTY THEN")
                                    print("*" * 20)
                                if user_choice == "n":
                                    print("*" * 20)
                                    player.dontvisit_count += 3
                                    player.beretta_count += 1
                                    mall_menu(player)

                
################ LEAVE Mall #######################
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
    while True:
        user_choice = input("Where do you want to go? (1-4)\n1. Continue Down Hallway\n2. Head Upstairs\n3. Open Cabinet\n4. Leave Digital Crafts\nEnter selection here: ")
        if user_choice == "1":
            if player.dc_hallway_count == 1:
                print("""
    You continue down the hallway.
    You are lead to an empty room at the end of the hallway.
    There you find a doll in the middle of the room.
    """)
                yesorno = input("Would you like to pick it up? (Y/N) ")
                yesorno = yesorno.lower()
                if yesorno == "y":
                    print("""
    You pick up the doll. 
    Suddenly it releases a poisonous gas!
    Your health takes a -10 hit.
    """)
                    player.health -= 10
                    player.dc_hallway_count += 1
                    print("%s's health: %d" % (player.name, player.health))
            elif player.dc_hallway_count >= 2:
                print("Hmm! There's just the empty remnants of the poison doll here... You head back into the hallway.")
        elif user_choice == "2":
            if player.dc_sound_count == 1:
                print("""
Your curiosity gets the best of you. Let us not hope curiosity kills the cat.
You walk upstairs and investigate the sound.
""")
                # time.sleep(4)
                print("""
The room is dark, but you make out a faint outline in the corner of the room.
""")
                # time.sleep(2)
                print("""
'Who goes there?!' Calls the voice.
You answer back.
Suddenly, a man with a scraggly beard and kind but withered eyes appears. He looks like he's been through a lot.
""")
                # time.sleep(2)
                print("""
'My name is Sean. I used to teach here at Digital Crafts... But that was a long time ago.
Since then, I haven't been able to leave the facility. Memories, ya know? But also, I'm a bit tied up.'
Sean shows you a battery pack hooked up to the wall. Sean is a cyborg.
'It's one of the few places in town that still has electricity...'
You look around and see he has a small pouch next to him.
""")
                # time.sleep(2)
                yesorno = input("'You want it? It's got some money in it. I don't need it anymore.' (Y/N)" )
                yesorno = yesorno.lower()
                if yesorno == "y":
                    print("""
Alright... But I won't let you just have all the answers!
You need a challenge - let's fight!""")
                    print("Cyborg Sean challenges you to a duel!")
                    while cyborgsean.health > 0 and player.health > 0:
                                print("\nWhat do you want to do?")
                                print("1. Run Away")
                                print("2. Punch")
                                if "knife" in player.bag:
                                    print ("3. Use Knife")
                                if "gun" in player.bag:
                                    print ("4. Use Gun")
                                user_input = input()
                        # Run Away
                                if user_input == "1":
                                    player.health -= 20
                        # Punch
                                elif user_input == "2":
                                    player.do_punch(cyborgsean)
                        # Knife
                                elif user_input == "3" and "knife" in player.bag:
                                    player.do_knife(cyborgsean)
                        # Gun
                                elif user_input == "4" and "gun" in player.bag:
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
                                    player.dc_sound_count += 1
                else:
                    print("Okay. Bye bye.")
            elif player.dc_sound_count >= 2:
                print('The mangled wreckage of Cyborg Sean lay sparking. You can hear him softly repeating "group debug... group debug..."')
        elif user_choice == "3":
            if player.dc_cabinet_count == 1:
                print("""
You sweep away the cobwebs and open the cabinet.
You find some old sanitizer.
""")
                player.bag.append("Sanitizer")
                print("Your bag contents is now %s." % player.bag)
                player.dc_cabinet_count += 1
            elif player.dc_cabinet_count >= 2:
                print("Hmm! The cabinet is empty... You've seen all there is to see here.")
        elif user_choice == "4":
            location_menu(player)
        else:
            print("BLOOP. Can't do that patna'. Please choose again. ")