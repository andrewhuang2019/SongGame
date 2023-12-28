# menu.py

from api import API
from userinput import UserInput

class Menu:
    def __init__(self):
        self.api = API()
    
    def run(self):
        #self.api.authorization_code_flow()
        print(self.api.get_urls())
        

    def menu(self):
        pass

    # ratings will be in .1 decimal form out of 10. 
    # closer to rating = higher score
    def point_calculator(self):
        pass

    def win_calculator(self):
        pass

