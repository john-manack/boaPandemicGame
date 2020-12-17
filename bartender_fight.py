import random
import time

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

carl = Character("Carl Grimes", 100, "low", 5, "Male", 0, 5)
bartender_zombie = Character("Bartender Zombie", 25, "low", 5, "Male", 10, 4)

def zombie_fight(good_guy, bad_guy):
    print("Get ready to battle %s!" % bad_guy.name)
    while good_guy.alive() and bad_guy.alive():
        good_guy.print_status()
        bad_guy.print_status()
        print("")
        print("Battle options:")
        print("1. fight %s" % bad_guy.name)
        print("2. do nothing")
        print("3. flee")
        user_input = str(input("Enter choice here: "))
        print("*" * 10)
        if user_input == "1":
            good_guy.attack(bad_guy)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if good_guy.alive():
            bad_guy.attack(good_guy)
            
        if bad_guy.dead():
            print("%s killed %s!" % (good_guy.name, bad_guy.name))