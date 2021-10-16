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

    def start_game(self):
        """
        Starts the game loop to control and goes through the sequence of play.

        Args self(director): an instance of Director
        """
        self.jumper.get_jumper_word()
        #print(self.jumper.jumper_word)
        print(*self.jumper.hidden_word, sep = " ")
        self.jumper.jumper_Image(self.jumper.jumper_health)
        self.jumper.jumper_health -= 1
        
        while self.keep_Playing  == True:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        """
        Gets the inputs each round of play. In this case,
        getting a letter from the player for the mystery word.

        args: (Director): An instance of Director.
        """
        letter_clear =  False
        while letter_clear == False:
            letter = self.player.player_input()
            letter_clear = self.controller.check_letter(letter,self.player.guesses)
        self.player.player_letter = letter
        self.player.guesses.append(letter)
        
        


    def do_updates(self):
        """
        perfroms changes based on the player input. in this case,
        if the player was right it will display the letter for the word.
        if the player was wrong it will cut a rope from the parachute.

        args: (Director) an instance of Director.
        """
    
        self.jumper.add_letter(self.player.player_letter)
            

    def do_outputs(self):
        """
        displays importent game information each round of play. In this case,
        That means printing the updated given letters of the word and
        how many ropes you have left.

        args: (Director): An instacne of Direcyor.
        """
        print(*self.jumper.hidden_word, sep=" ")
        self.jumper.jumper_Image(self.jumper.jumper_health)
        print("Used letters:")
        print(*self.player.guesses, sep= " ")
        print("")


        if self.jumper.jumper_health == 0:
            print(f"\nYou have ran out of lives the word was {self.jumper.jumper_word}")
            print("Thanks for playing")
            self.keep_Playing = False
        
        if "_" not in self.jumper.hidden_word:
            print("you got the word right!")
            self.keep_Playing = False
        
        pass

        

