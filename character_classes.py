import random
import time
from pygame import mixer

class Character:
    def __init__(self, name, species, health, charisma_lvl, purse, sex, power_lvl, punch_power, knife_power, shoot_power, defense_lvl, defense, special_power):
        self.name = name
        self.species = species
        self.health = health
        self.charisma_lvl = charisma_lvl
        self.purse = purse
        self.sex = sex
        self.power_lvl = power_lvl
        self.punch_power = punch_power
        self.knife_power = knife_power
        self.shoot_power = shoot_power
        self.defense_lvl = defense_lvl
        self.defense = defense
        self.special_power = special_power
        self.bag = []

    def __str__(self):
        return """
        Name: %s
        Health: %s
        Charisma: %s
        Species: %s
        Purse: %s
        Sex: %s
        Punch Power: %s
        Defense: %s
        """ % (self.name, self.health, self.charisma_lvl, self.species, self.purse, self.sex, self.power_lvl, self.defense_lvl) 

        
    def add_item(self, new_item):
        self.bag.append(new_item)
        print("%s was added to your bag" % (new_item))

    def bag_contents(self):
        # INPUT SOUNDBOARD OF UNZIPPING A BAG
        # time.sleep(1)
        print("Your bag contains %s" % (self.bag))
                

    def punch(self, enemy):
        if self.power_lvl == "low":
            punch = random.randint(1,3)
        if self.power_lvl == "medium":
            punch = random.randint(4,6)
        if self.power_lvl == "high":
            punch = random.randit(7,9)
        defense = enemy.add_defense()
        if defense > punch:
            defense = punch
        enemy.health -= (punch - defense)
        #//mixer.Sound.play(punch_se)
        #//time.sleep(1)
        print("\n\nYou PUNCHED the %s for %d damage!" % (enemy.name, punch))
        print ("%s BLOCKED your punch and has %d health left." % (enemy.name, enemy.health))

    def knife(self, enemy):
        self.knife_power == 25
        defense = enemy.add_defense()
        if defense > self.knife_power:
            defense = self.knife_power
        enemy.health -= (self.knife_power - defense)
        print("\n\nYou SLASHED the %s for %d damage!" % (enemy.name, self.knife_power))
    
    def shoot(self, enemy):
        self.shoot_power == 50
        defense = enemy.add_defense()
        if defense > self.shoot_power:
            defense = self.shoot_power
        enemy.health -= (self.shoot_power - defense)
        print("\n\nYou SLASHED the %s for %d damage!" % (enemy.name, self.shoot_power))
    
    def alive(self):
        return self.health > 0
    
    def dead(self):
        return self.health <= 0

    def add_defense(self):
        if self.defense_lvl == "low":
            return random.randint(1, 3)
        if self.defense_lvl == "medium":
            return random.randint(4, 6)
        if self.defense_lvl == "high":
            return random.randint(7, 9)
        self.defense += add_defense

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
    
    # Let's build out a special power after MVP is running.
    def special_power(self, other):
        pass

    def attack(self, enemy):
        enemy.health -= self.punch_power
        print("%s does %d damage to %s." % (self.name, self.punch_power, enemy.name))


class Location:
    def __init__(self, place, description, room1, room2, room3):
        self.place = place
        self.description = description
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3
        

    def __str__(self):
        return"""
        %s
        """ % (self.place)

