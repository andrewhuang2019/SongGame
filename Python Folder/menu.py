# menu.py

from api import API
from userinput import UserInput
import math
class Menu:
    def __init__(self):
        self.api = API()
    
    def run(self):
        #self.api.authorization_code_flow()
        self.api.quick_start()

    def menu(self):
        pass

    # ratings will be in .1 decimal form out of 10. 
    # closer to rating = higher score
    def point_calculator(self, rater_rating, guesser_rating):
        
        #calculation that gives score based on how close from 10 to 1
        score = 10 - math.abs(rater_rating - guesser_rating)
        
        return score

    def win_calculator(self):
        pass

