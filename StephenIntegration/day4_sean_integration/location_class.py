import random
import time
from pygame import mixer

class Location:
    def __init__(self, place, description, room1, room2, room3):
        self.place = place
        self.description = description
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3


    def __str__(self):
        return "%s" % (self.place)



# class Home(Location):
#     def __init__(self, place, description, home_counts, room1, room2, room3):
#         super().__init__(place, description, home_counts, room1, room2, room3)
#         self.home_counts = 0

#         def home_count(self):
#             self.home_vists += 1

#         def room1(self):
#             pass

#         def room2(self):
#             pass

#         def room3(self):
#             pass

# class Pub(Location):
#     def __init__(self, place, description, pub_counts, room1, room2, room3):
#         super().__init__(place, description, pub_counts, room1, room2, room3)
#         self.pub_counts = 0

#         def pub_count(self):
#             self.pub_vists += 1


#         def room1(self):
#             pass

#         def room2(self):
#             pass

#         def room3(self):
#             pass

# class Highschool(Location):
#     def __init__(self, place, description, hs_counts, room1, room2, room3):
#         super().__init__(place, description, hs_counts, room1, room2, room3)
#         self.hs_counts = 0

#         def hs_count(self):
#             self.hs_vists += 1


#         def room1(self):
#             pass

#         def room2(self):
#             pass

#         def room3(self):
#             pass

# class Stadium(Location):
#     def __init__(self, place, description, stad_counts, room1, room2, room3):
#         super().__init__(place, description, stad_counts, room1, room2, room3)
#         self.stad_counts = 0

#         def stad_count(self):
#             self.stad_vists += 1


#         def room1(self):
#             pass

#         def room2(self):
#             pass

#         def room3(self):
#             pass

# class DigitalCrafts(Location):
#     def __init__(self, place, description, dc_counts, room1, room2, room3):
#         super().__init__(place, description, dc_counts, room1, room2, room3)
#         self.dc_counts = 0

#         def dc_count(self):
#             self.dc_vists += 1


#         def room1(self):
#             pass

#         def room2(self):
#             pass

#         def room3(self):
#             pass