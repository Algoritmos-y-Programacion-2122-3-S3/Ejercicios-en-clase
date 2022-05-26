import random
from horses import Horse

class Race:

    def __init__(self,horses,number):
        self.horses = list(horses)
        self.number = number

    def start(self):
        print("Welcome to race", self.number)
        print("PAAAAAAAAAAAAAAAAAAAAAAAAAAAAARTIDAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def winner(self):
        winner = self.horses[random.randint(0,5)]
        print("The winner is:",winner.name,"With the Joker", winner.joker)