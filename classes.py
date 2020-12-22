import random
import time
from pygame import mixer

class Character:
    def __init__(self, name, health, purse, sex, punch, defense):
        self.name = name
        self.health = health
        self.purse = purse
        self.sex = sex
        self.punch = punch
        self.knife = 25
        self.shoot = 50
        self.defense = defense
        self.bag = []
        self.classroom_count = 1
        self.auditorium_count = 1
        self.cafeteria_count = 1
        self.bartenderencounter = 1
        self.ladies_count = 1
        self.dc_hallway_count = 1
        self.dc_sound_count = 1
        self.dc_cabinet_count = 1
        self.gamestop_count = 1
        self.stafflounge_count = 1
        self.beretta_count = 1
        self.dontvisit_count = 1
        self.gvisit_count = 1
        self.itemslist = ["1. mask",
        "2. respirator",
        "3. an old dog collar"]
        # self.location = location
    
    def __str__(self):
        return """
        Name: %s
        Health: %s
        Purse: %s
        Sex: %s
        Infection: %s
        Punch Power: %s
        """ % (self.name, self.health, self.purse, self.sex, self.infection, self.punch) 

    def add_item(self, new_item):
        self.bag.append(new_item)
        print("%s was added to your bag" % (new_item))
    
    def do_punch(self, zombie):
        if self.punch == "low":
            damage = random.randint(1,3)
        if self.punch == "medium":
            damage = random.randint(4,6)
        if self.punch == "high":
            damage = random.randint(7,9)
        if self.punch == 50:
            damage = 50
        defense = zombie.add_defense()
        # if defense < damage:
        #     defense = 8
        zombie.health -= (damage - defense)
        #//mixer.Sound.play(punch_se)
        #//time.sleep(1)
        print("\n\n%s PUNCHED %s for %d damage!" % (self.name, zombie.name, (damage - defense)))
        print("%s health: %d \n%s health: %s " % (self.name, self.health, zombie.name, zombie.health))
        
    def do_knife(self, zombie):
        self.knife == 25
        defense = zombie.add_defense()
        zombie.health -= (self.knife - defense)
        print("\n\n%s SLASHED %s for %d damage!" % (self.name, zombie.name, (self.knife - defense)))
        print("%s health: %d \n%s health: %s " % (self.name, self.health, zombie.name, zombie.health))

    def do_shoot(self, zombie):
        self.shoot == 50
        defense = zombie.add_defense()
        zombie.health -= (self.shoot - defense)
        print("\n\nYou Shot %s for %d damage!" % (zombie.name, (self.shoot - defense)))
        print("%s health: %d \n%s health: %s " % (self.name, self.health, zombie.name, zombie.health))

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0

    def add_defense(self):
        if self.defense== "low":
            return random.randint(1, 3)
        if self.defense == "medium":
            return random.randint(4, 6)
        if self.defense == "high":
            return random.randint(7, 9)
        
    def bag_contents(self):
        # INPUT SOUNDBOARD OF UNZIPPING A BAG
        # time.sleep(1)
        print("Your bag contains %s" % (self.bag))
    
    def print_status(self):
        # INPUT SOUNDBOARD OF UNZIPPING A BAG
        # time.sleep(1)
        print("Your health: %d" % (self.health))
                
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
        
    # def get_infected(self):
    #    self.infection += 5
    #    while self.infection > 0:
    #        self.health -= self.infection


    # # Let's build out a special power after MVP is running.
    # def special_power(self, other):
    #     pass

    # def attack(self, enemy):
    #     enemy.health -= self.punch_power
    #     print("%s does %d damage to %s." % (self.name, self.punch_power, enemy.name))



class Location():
    def __init__(self, place, description, room1, room2, room3):
        self.place = place
        self.description = description
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3

#     def __str__(self):
#         return"""
#         %s
#         %s
#         """ % (self.place, self.description)
# # def room1(self, place):