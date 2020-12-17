import random
import time
from pygame import mixer

class Character:
    def __init__(self, name, health, charisma_lvl, purse, sex, infection, power):
        self.name = name
        self.health = health
        self.charisma_lvl = charisma_lvl
        self.purse = purse
        self.sex = sex
        self.infection = 0
        self.bag = []
        self.power = power
        # self.location = location
        
    def add_item(self, new_item):
        self.bag.append(new_item)
        print("%s was added to your bag" % (new_item))

    def bag_contents(self):
        # INPUT SOUNDBOARD OF UNZIPPING A BAG
        # time.sleep(1)
        print("Your bag contains %s" % (self.bag))
                
    def pay(self, other_person):
        if self.charisma_lvl == "low":
            pay = random.randint(1, 5)
        if self.charisma_lvl == "medium":
            pay = random.randint(6, 10)
        if self.charisma_lvl == "high":
            pay = random.randint(11, 15)
        other_person.purse += pay
        # INPUT SOUNDBOARD OF KA-CHING
        # time.sleep(1)
        print('You got paid $%d, you now have $%s!' % (pay, other_person.purse))
        
    def get_infected(self):
        self.infection += 5
        while self.infection > 0:
            self.health -= self.infection

    def __str__(self):
        return """
        Name: %s
        Gender: %s
        Health: %s
        Charisma_lvl: %s
        Purse: %d
        Infection: %d
        """ % (self.name, self.sex, self.health, self.charisma_lvl, self.purse, self.infection)

    def alive(self):
        return self.health > 0
    
    def dead(self):
        return self.health <= 0
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("%s does %d damage to %s." % (self.name, self.power, enemy.name))
    
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Location():
    def __init__(self, place, description, room1, room2, room3):
        self.place = place
        self.description = description
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3

    def __str__(self):
        return"""
        %s
        %s
        """ % (self.place, self.description)
# def room1(self, place):

    def location_menu():
        print("1. ", str(pub.place))
        while True:
            location_choice = input("Where would you like to go? (1-4) ")
            if location_choice == "1":
                location = pub
                print(str(player))
                # location = pub
                pub_location()
                pub_menu()
            if location_choice == "2":
                location = highschool
                return highschool
            if location_choice == "3":
                location = stadium
                return stadium
            if location_choice == "4":
                location = susan_location
                return susan_location
            else:
                print("YOU HAVE FAILED ME FOR THE LAST TIME")
    

