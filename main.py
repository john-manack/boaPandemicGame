import random
import time
from classes import Character, Location
from functions import open_story, character_list, print_character_menu, player_selection, pub_location, pub_menu, location_menu
import sys

# AUDIO
##### MUSIC #####
from pygame import mixer
mixer.music.load("audio/glitchmob.mp3")
mixer.music.play(-1)


open_story()
player = player_selection()
location_menu(player)