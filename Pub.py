import time


def pub_location():
    print("""
Ahh, the old pub. You've been coming here for years. It's been a while though, 
what with the pandemic and all. The smell of bar tar and cigarettes still lingers; 
this place was always packed. Now, a single bartender manages every patron. 
It's almost empty, but there are two young ladies sitting at the far end of the bar.
    """)
    time.sleep(5)
    print("What will it be?")
    time.sleep(3)

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
                # INPUT SOUNDBOARD OF POURING A BEER
                # time.sleep()
                # self.getdrunk()
                print("Will you have another?")
                pub_menu()
        
            
            elif user_choice == "2":
                time.sleep(2)
                
                if bartenderencounter == 1:
                    print("""
You approach the bar. The bartender greets you with a smile..
"The usual?" he says, as he pours your whiskey.
It's nice to be here..
""")
                    time.sleep(5)
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
                    #///time.sleep(5)
                    print("""
Bleeding?
""")
                    # INPUT ZOMBIE BARTENDER SOUND
                    # time.sleep()
                    print("ZOMBIE FIGHT!")
                    #/ self.zombie_fight(pubZombie)
                    bartenderencounter += 1

                elif bartenderencounter > 2:
                    print("The bartender is dead")
                    pub_menu()



            elif user_choice == "3":
                time.sleep(2)
                print("""
You can't help but notice these two gorgeous young ladies looking at you.
You approach them...
""")
                time.sleep(5)
                print("""
"How are you, ladies?"
""")
                # INPUT LADIES SOUND
                # time.sleep()
                print("\"Hey there, handsome\" they say, in a slow, drawly unison.")
                pub_menu()
            
            
            
            elif user_choice == "4":
                location_menu()


pub_location()
pub_menu()