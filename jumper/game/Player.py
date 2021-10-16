"""
This class handles the player interation with the program
"""

class player():
    def __init__(self):
        self.guesses = []
        self.player_letter = str
        
    def player_input(self):
        # This will get input from the user and send it back to director. 
        # args (self) an instance of player.
            return input("Please enter a letter: ")


