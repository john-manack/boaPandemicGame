import random
import time
from classes import Character, Location
from functions import open_story, character_list, print_character_menu, player_selection, pub_location, pub_menu, location_menu
import sys

# Music
# from pygame import mixer
# mixer.init()
# mixer.music.load("audio/TK_Intro_2.wav")
# mixer.music.play(-1)

open_story()
player=player_selection()
location_menu(player)
