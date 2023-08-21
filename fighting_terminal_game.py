"""
OOP

Class based programming

Create a blueprint for a real world object or idea then use member functions, constructors etc to create the logic for working

self keyword in python refers to the current object of the class. It is a reference to the current instance of the class

self keyword can be anything, magic, coffee etc. 

__init__() method is the constructor. It can be used to initialise varibles during object instantiation


use setter and getter methods like in java to set and get class variables

"""


import random

class Game:
    def __init__(self):
        self.players = [{"Lion":96},{"Tiger":99},{"Wolf":92},{"Man_with_knife":78},{"Bear":90}]

    def start(self):
        while True:
            choice = input(" Choose 1 for Lion, \n Choose 2 for Tiger, \n Choose 3 for Man, \n Choose 4 for Bear,\n Choose 0 for exit... \n ")
            
            choice = int(choice)

            if choice == 0 :
                break
            else:
                comp_choice = random.choice([0,1,2,3])

                # chosen_by_comp = self.players[comp_choice]
                
                print(f"Now your {list(self.players[choice].keys())[0]} is fighting {list(self.players[comp_choice].keys())[0]}")

                if list(self.players[choice].values())[0] > list(self.players[comp_choice].values())[0]:
                    print("You won!")
                elif list(self.players[choice].values())[0] == list(self.players[comp_choice].values())[0]:
                    print("You tied!")
                else:
                    print("Boohoo you lost")


g = Game()
g.start()
                

