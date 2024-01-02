# menu.py

from api import API
from userinput import UserInput

class Menu:
    def __init__(self):
        self.api = API()
    
    def run(self):
        self.menu()
        

    def menu(self):
        #replay loop 
        while True:

            #players input and play 2 rounds winner is determined by better score
            rating1 = input("Enter rating of song #1: ")

            rating2 = input("Enter rating of song #2: ")

            rating3 = input("Enter rating of song #3: ")

            rating4 = int(input("Enter rating of song #4: "))

            guess = int(input("Enter guess of song #4: "))

            player_one_score = self.point_calculator(rating4, guess)

            rating1 = input("Enter rating of song #1: ")

            rating2 = input("Enter rating of song #2: ")

            rating3 = input("Enter rating of song #3: ")

            rating4 = int(input("Enter rating of song #4: "))

            guess = int(input("Enter guess of song #4: "))

            player_two_score = self.point_calculator(rating4, guess)

            #use win calculator to find winner or tie
            if self.win_calculator(player_one_score, player_two_score) == "0":
                print("Tie!")
            elif self.win_calculator(player_one_score, player_two_score):
                print("Player 1 Wins!")
            else:
                print("Player 2 Wins!")

            #Check if player wants to replay
            choice = input("Play Again?(y/n): ")

            if choice == "y":
                continue
            else:
                break

    # ratings will be in .1 decimal form out of 10. 
    # closer to rating = higher score
    def point_calculator(self, rater_rating, guesser_rating):
        
        # calculation that gives score based on how close from 10 to 1
        score = 10 - abs(rater_rating - guesser_rating)
        
        return score

    #Compares the two games scores and return greater score or 0 for ties
    def win_calculator(self, game_score, other):
        if game_score == other:
            return "0"
        return game_score > other

