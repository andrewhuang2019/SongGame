# menu.py

from api import API
from userinput import UserInput

class Menu:
    def __init__(self):
        self.api = API()
    
    def run(self):
        self.api.client_credentials_flow()