import random
import time
from pygame import mixer

class Character:
    def __init__(self, name, health, purse, sex, punch, knife, shoot, defense):
        self.name = name
        self.health = health
        self.purse = purse
        self.sex = sex
        self.punch = punch
        self.knife = knife
        self.shoot = shoot
        self.defense = defense
        self.bag = []
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
        defense = zombie.add_defense()
        # if defense < damage:
        #     defense = 8
        zombie.health -= (damage - defense)
        #//mixer.Sound.play(punch_se)
        #//time.sleep(1)
        print("\n\n%s PUNCHED %s for %d damage!" % (self.name, zombie.name, damage))
        print("%s health: %d \n%s health: %s " % (self.name, self.health, zombie.name, zombie.health) )
        
        

    def do_knife(self, zombie):
        self.knife == 25
        defense = zombie.add_defense()
        zombie.health -= (self.knife - defense)
        print("\n\n%s SLASHED %s for %d damage!" % (self.name, zombie.name, self.knife))
        print("%s health: %d \n%s health: %s " % (self.name, self.health, zombie.name, zombie.health) )

    def do_shoot(self, zombie):
        self.shoot_power == 50
        defense = zombie.add_defense()
        if defense > self.shoot_power:
            defense = self.shoot_power
        zombie.health -= (self.shoot_power - defense)
        print("\n\nYou SLASHED %s for %d damage!" % (zombie.name, self.shoot_power))

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0

    def add_defense(self):
        if self.defense == "low":
            return random.randint(1, 3)
        if self.defense == "medium":
            return random.randint(4, 6)
        if self.defense == "high":
            return random.randint(7, 9)
        
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

    def print_status(self):
        print("You have %d health." % (self.health))



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

  
    