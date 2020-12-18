class Character:
    def __init__(self, name, health, purse, bag, species):
        self.name = name
        self.health = health
        self.purse = purse
        self.bag = []
        self.special_power = special_power
        self.species = species

    def __str__(self):
        return f"""
        Name: {self.name}
        Health: {self.health}
        Purse: {self.purse}
        Special Power: {self.special_power}
        Species: {self.species}
        """
    
    def is_alive(self):
        return self.health > 0

    def special_power(self, other):