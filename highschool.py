def highschool_location():
    print("""
You arrive at an abandoned high school...
The smell of rotting food and dead fish floats through the air.
You think you see a shadowy figure rushing 
The front doors are locked, but you notice a window that's been left ajar.
You climb inside to find yourself in a dark hallway.
          """)
    while True:
            user_choice = print(input("Where do you want to go? (1-4)\n1. Classroom\n2. Cafeteria\n3. Office\n4. Auditorium\n5. Leave High School"))
            if user_choice == "1":
                if hs_zombie.is_alive():
                    print("You walk into the classroom down the hall. A zombie lifts its head from behind a desk and races toward you. You are attacked by a zombie!")
                    # self.zombie_fight(hs_zombie)
                elif hs_zombie.is_dead():
                    print("The room is empty. You killed the zombie laying on the ground.")
            elif user_choice == "2":
                print("The cafeteria reveals the source of the horrid smell. The freezers have been left open for days and a deer lies dead behind salad bar. You hear a dripping sound coming from the kitchen. You look under the sink and find a watch.")
                # self.get_item(watch)
            elif user_choice == "3":
                print("Enter office; principal is zombie. Zombie fight ensues.")
            elif user_choice == "4":
                print("Enter auditorium. find a granola bar for a health boost")
            elif user_choice == "5":
                break
            else:
                # INPUT SOUNDBOARD FAILED ME DARTH VADER
                # time.sleep(1.5)
                print("Sorry I didn't get that.")