from game.Player import player
from game.Jumper import jumper
from game.Controller import controller


class director():
    """
    A code template for a person who directs the game. The responsibility
    of this class is to control the game.
    """
    def __init__(self):
        self.player = player()
        self.jumper = jumper()
        self.controller = controller()
        self.keep_Playing = True

    def Play_game(self):
        """
        Starts the game loop to control and goes through the sequence of play.

        Args self(director): an instance of Director
        """
        while self.keep_Playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        """
        Gets the inputs each round of play. In this case,
        getting a letter from the player for the mystery word.

        args: (Director): An instance of Director.
        """
        guess_letter = self.player.player_input()
        self.controller.write_letter(guess_letter)
        
        
        


    def do_updates(self):
        """
        perfroms changes based on the player input. in this case,
        if the player was right it will display the letter for the word.
        if the player was wrong it will cut a rope from the parachute.

        args: (Director) an instance of Director.
        """
        if self.player.player_input() == True:
            answer = self.jumper.get_jumper_word()
        else:
            answer = self.jumper.get_hidden_word()

        return answer
            

    def do_outputs(self):
        """
        displays importent game information each round of play. In this case,
        That means printing the updated given letters of the word and
        how many ropes you have left.

        args: (Director): An instacne of Direcyor.
        """
        letter = self.player.player_input()
        self.controller.write_letter(letter)

        

