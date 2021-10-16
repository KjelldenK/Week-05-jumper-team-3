import random
class jumper():
    def __init__(self):
        self.jumper_word = str
        self.jumper_health = 5
        self.hidden_word = []
    def jumper_Image(self,health):
        if health == 5:
            print("you still have 5 hp")
        elif health == 4:
            print("you still have 4 hp")
        elif health == 3:
            print("you still have 3 hp")
        elif health == 2:
            print("you still have 2 hp")
        elif health == 1:
            print("you only have 1 hp")
        elif health == 0:
            print("you are dead")


    def get_jumper_word(self):
        """
        This will go into words.txt and gather 1 random word from the list and 
        create a set a dashes into the hidden word list to represent missing letters
        for the player.

        args (jumper): an instence of jumper
        """

        with open("words.txt", "r") as ranwords:
            read_line = ranwords.readlines()
            self.jumper_word = read_line[random.randint(1,10000)].strip("\n")
        #self.jumper_word = "sandwich"
        i = 0
        while i < int(len(self.jumper_word)):
            self.hidden_word.append("_")
            i += 1

    def add_letter(self,letter):
        """
        this will add a letter to the hidden word list if the letter is in the word.
        If the letter is not in the word it will take away 1 health from the jumper.

        args (jumper, letter) an instance of jumper and a letter from the user.
        """

        j = 0
        changes = 0
        while j < len(self.jumper_word):
            if self.jumper_word[j] == letter:
                self.hidden_word[j] = letter
                j +=  1
                changes += 1
            else:
                j += 1
        if changes == 0:
            self.jumper_health -= 1
