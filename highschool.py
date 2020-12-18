def highschool_print_intro():
    print("""
You arrive at an abandoned high school...
The smell of rotting food floats through the air.
You think you see a shadowy figure step behind a wall on the far side of the building.
The front doors are locked, but you notice a window that's been left ajar.
You climb through to find yourself in a dark hallway.
          """)

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
There are few desks overturned and the chalk-board on the wall is crooked....
It looks like there was some sort of struggle in here. 
Something shiny catches your eye under one of the desks... 
It's a golden wrist-watch! Wonder who this belonged to? 
You pick it up and put it in your pocket. 
You wander back into the hall.
                          """)
                    print("*" * 20)
                    # player.bag.append(watch)
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
Feeling a little thirsty, you approach the door and push it open.
What you see next sets your heart racing:
The beloved high school lunch lady is laying on the ground with her head turned.
You run up to check if she is still breathing. She isn't.
But is that her arm...... moving???
ZOMBIE ATTACK!")
                    """)
                    print("*" * 20)
                elif cafeteria_count >= 2:
                    print("*" * 20)
                    print("")
                    print("Hmm! You've seen all there is to see here! You wander back into the hall.")
                    print("")
                    print("*" * 20)

################ INTERACTION 3 ######################
            elif user_choice == "3":
                print("Enter auditorium. find a granola bar for a health boost")

################ LEAVE SCHOOL #######################
            elif user_choice == "4":
                break

############### INVALID ENTRY - LOOP RESETS #########
            else:
                print("Sorry I didn't get that.")

#TEST FUNCTIONS
highschool_print_intro()
highschool_menu()