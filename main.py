import random
import time
from script import open_story
from menu import character_list, npc_list, opponent_list, location_list, character_menu, location_menu, pub_menu, zombie_fight, ending 
from character_classes import Character
from location_class import Location

# def story_flow():
#     while player.alive():


open_story()
time.sleep(2)
print("Press enter to continue")

player = character_menu()
while player.alive():
    location = location_menu()
    


    





