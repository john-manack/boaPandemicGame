from characters_std import Character, Location, character1, character2, character3, character4, hs_zombie
import random
player = character3
zombie = hs_zombie



def highschool_print_intro():
    print("*" * 20)
    print("""
You arrive at an abandoned high school...
The smell of rotting food floats through the air.
You think you see a shadowy figure step behind a wall on the far side of the building.
The front doors are locked, but you notice a window that's been left ajar.
You climb through to find yourself in a dark hallway.
          """)
    print("*" * 20)

def highschool_menu():
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
                break

############### INVALID ENTRY - LOOP RESETS #########
            else:
                
                print("Sorry I didn't get that.")

#TEST FUNCTIONS
highschool_print_intro()
highschool_menu()