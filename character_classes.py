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

# class Npc():

#     def __init__(self, name, purse, sex, npc_class, npc_type):
#         self.name = name
#         self.species = species
#         self.npc_class = str(npc_class)
#         if npc_type == 'minion' or npc_type == 'rival' or npc_type == 'nemesis':
#             self.npc_type = npc_type
#         else:
#             print('\n', "Must choose 'minion', 'rival', or 'nemeses'.",'\n\n')
#             print(" Example calling npc object: npc('Duke Skyhawker', 'human', 'pirate', 'rival')", '\n')
#             raise SystemExit

# def general_skills(self):
#         if self.npc_type == 'minion':
#             skill_limit = 2
#         elif self.npc_type == 'rival':
#             skill_limit = 3
#         elif self.npc_type == 'nemesis':
#             skill_limit = 4
 
#         try:
#             qty = career[self.npc_class][1][0] + type_rules[self.npc_type][2][0]
#             return dict(zip(random.sample(general_skills,qty),[(random.randint(0,skill_limit) + 1) for number in range(1,qty + 1)]))
#         except ValueError:
#             return "Max amount of knowledge skills is 22"