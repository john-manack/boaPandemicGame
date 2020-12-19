from class_std import Character, Location
import time
import sys
from pygame import mixer

##################################
### DEFINE PLAYABLE CHARACTERS ###
##################################

# name, species, health, charisma_lvl, purse, sex, punch_power, knife_power, shoot_power, defense, special_power
character1 = Character("Dr. Robert Neville", "Human", 100, "high", 0, "Male", "UNDT PUNCH POWER", 25, 50, "UNDT DEFENSE", "UNDT SPECIAL POWER")

character2 = Character("Sherlock", "Cat", 100, "UNDT CHARISMA", 0, "UNDT SEX", "UNDT PUNCH POWER", 25, 50, "UNDT DEFENSE", "Psychic Whiskers")

character3 = Character("Carl Grimes", "Human", 100, "low", 0, "Male", "medium", 25, 50, "low", "Trooper Drop Kick")

character4 = Character("Chico Dusty", "Human", 100, "UNDT CHARISMA", 0, "Male", "high", 25, 50, "low", "UNDT SPECIAL POWER")

##################################
##### DEFINE CHARACTER LIST ######
##################################

def character_list():
    return [character1, character2, character3, character4]

def print_character_menu(pos1, char1, pos2, char2, pos3, char3, pos4, char4):
    print("-" * 110)
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        # "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name), (pos4 + char4.name)))
        "Name:", (char1.name), (char2.name), (char3.name), (char4.name)))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Species:", char1.species.title(), char2.species.title(), char3.species.title(), char4.species.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Health:", char1.health, char2.health, char3.health, char4.health))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Purse:", char1.purse, char2.purse, char3.purse, char4.purse))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Sex:", char1.sex, char2.sex, char3.sex, char4.sex))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Punch:", char1.punch_power.title(), char2.punch_power.title(), char3.punch_power.title(), char4.punch_power.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Defense:", char1.defense.title(), char2.defense.title(), char3.defense.title(), char4.defense.title()))
    print("{:<12}|| {:<22}|| {:<22}|| {:<22}|| {:<22}|".format(
        "Spec. Power:", char1.special_power.title(), char2.special_power.title(), char3.special_power.title(), char4.special_power.title()))

##################################
# DEFINE NONPLAYABLE CHARACTERS  #
##################################
# name, species, health, charisma_lvl, purse, sex, punch_power, knife_power, shoot_power, defense, special_power
bartender = Character("Bartender", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, None)
lunch_lady = Character("Lunch Lady", "Human", 100, "low", 999, "Female", 0, 0, 0, 0, None)
cashier = Character("Cashier", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, None)
sus_npc = Character("Susan NPC", "Human", 100, "low", 999, "Male", 0, 0, 0, 0, None)

bar_zombie = Character("Bartender Zombie", "Zombie", 25, "low", 50, "Male", 5, 0, 0, 3, None)
hs_zombie = Character("Lunch Lady Zombie", "Zombie", 25, "low", 50, "Female", 5, 0, 0, 3, None)
cash_zombie = Character("Cashier Zombie", "Zombie", 25, "low", 50, "Male", 5, 0, 0, 3, None)
sus_npc_zombie = Character("Susan NPC Zombie", "Zombie", 25, "low", 50, "Male", 5, 0, 0, 3, None)

def npc_list():
    return [bartender, lunch_lady, cashier, sus_npc, bar_zombie, hs_zombie, cash_zombie, sus_npc_zombie]

##################################
####### DEFINE LOCATIONS  ########
##################################
highschool = Location("High School", "This is the highschool", "Classroom", "Cafeteria", "Auditorium")