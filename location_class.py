class Location():
    def __init__(self, place, description, room1, room2, room3, visits):
        self.place = place
        self.description = description
        self.visits = 0

    def __str__(self):
        return"""
        %s
        %s
        """ % (self.place, self.description)

    def to_visit(self):
        self.visits += 1
    
    # def location_menu():
    #     print("1. ", str(pub.place))
    #     location_choice = input("Where would you like to go? (1-4) ")
    #     if location_choice == "1":
    #         location = pub
    #         return pub
    #         # pub_location()
    #         # pub_menu()
    #     if location_choice == "2":
    #         location = highschool
    #         return highschool
    #     if location_choice == "3":
    #         location = stadium
    #         return stadium
    #     if location_choice == "4":
    #         location = dig_crafts
    #         return dig_crafts
    #     else:
    #         print("YOU HAVE FAILED ME FOR THE LAST TIME")

