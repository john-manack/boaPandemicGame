import random
import time
from script import open_story
from menu import character_list, npc_list, opponent_list, location_list, character_menu, location_menu, pub_menu, zombie_fight, ending 
from character_classes import Character
from location_class import Location
from items import Items, Bandage 


# def game_flow(player, location):
#     return player.alive():



open_story() # from script
time.sleep(2)
print("Press Enter To Revail Your Fate!")
player = character_menu() # from menu
while player.alive():
    location = location_menu(player)
    
    


    





