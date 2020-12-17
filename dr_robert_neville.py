import random
import time
from pygame import mixer

class Character:
    def __init__(self, name, health, charisma_lvl, purse, sex, infection):
        self.name = name
        self.health = health
        self.charisma_lvl = charisma_lvl
        self.purse = purse
        self.sex = sex
        self.infection = 0
        self.bag = []
        
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

    def is_alive(self):
        return self.health > 0

