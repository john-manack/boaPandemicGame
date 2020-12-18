from classes import Character

# Character Functions and Definitions
character1 = Character("Sherlock", 50, 75, "level one item", "Psychic Whiskers", "Cat")
print(character1)

def character_list():
    return [character1]

def digital_crafts_home():
    while True:
        action = input("What would you like to do? (1-4) ")
            print("""
            1. Continue Down Hallway
            2. Investigate Sound
            3. Open cabinet
            4. Go Home
            """)
            if action == "1"
                print("""
                You continue down the hallway.
                You are lead to an empty room at the end of the hallway.
                There you find a doll in the middle of the room.
                """)
                yesorno = input("Would you like to pick it up? (Y/N)")
                    if yesorno == "Y"
                    else: 
            elif action == "2"
                if self == character1
                    print("""
                    Your curiosity gets the best of you. 
                    """)
                else:
                print(")
            elif action == "3"

            elif action == "4"

            else:
                print("BLOOP. Can't do that patna'. Please choose again. ")

# DIGITAL CRAFTS
def digital_crafts():
    while True:
    # insert an effect that makes the text show up character by character 
        print("""
        You have arrived at Digital Crafts.
        The flickering fluorescent lights shed scattered rays on an ominous scene.
        You notice black computer monitors covered in dust. A coffee mug is shattered on a desk.
        Cobwebs cover closed cabinets and chewed up rubber duckies litter the floor.
        You could tell this once used to be a place of learning and success.
        """)
    # insert sound effect!!
        print("""
        *Suddenly, you hear a loud crash coming from up the stairs.*
        What's that!
        You are not alone.
        """)

    action = input("What would you like to do? (1-4) ")
        print("""
        1. Continue Down Hallway
        2. Investigate Sound
        3. Open cabinet
        4. Go Home
        """)
        if action == "1"
            print("""
            You continue down the hallway.
            You are lead to an empty room at the end of the hallway.
            There you find a doll in the middle of the room.
            """)
            yesorno = input("Would you like to pick it up? (Y/N)")
                if yesorno == "Y"
                    print("""
                    You pick up the doll. 
                    Suddenly it releases a poisonous gas!
                    Your health takes a -10 hit.
                    """)
                    self.health -= 10
                else:
                    return digital_crafts_home()
        elif action == "2"
            print("""
            Your curiosity gets the best of you. Let us not hope curiosity killed the cat.
            You walk upstairs and investigate the sound.
            """)
            # want to press enter key to keep going hmm
            print("""
            The room is dark, but you make out a faint outline in the corner of the room.
            """)
            print("""
            'Who goes there?!' Calls the voice.
            You answer back.
            Suddenly, a man with a scraggly beard and kind but withered eyes appears. He looks like he's been through a lot.
            """)
            print("""
            'My name is Sean. I used to teach here at Digital Crafts... But that was a long time ago.
            Since then, I haven't been able to leave the facility. Memories, ya know? But also, I'm a bit tied up.'
            Sean shows you a battery pack hooked up to the wall. Sean is a cyborg.
            'It's one of the few places in town that still has electricity...'
            You look around and see he has a small pouch next to him.
            """)
            yesorno = input("You want it? Its got some money in it. I don't need it anymore." (Y/N))
                if yesorno == "Y"
                    print("""Alright... But I won't let you just have all the answers!
                    You need a challenge and I need some exercise - let's fight!""")
                    # make sean character
                else:
                    return digital_crafts_home()
        elif action == "3"
            print("""
            You sweep away the cobwebs and open the cabinet.
            You find some old sanitizer.
            """)
            self.append("sanitizer")
            digital_craft_home()

        elif action == "4"
            return home()
        else:
            print("BLOOP. Can't do that patna'. Please choose again. ")