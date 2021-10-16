import random

"""
This class will take care of the jumper information such as the word that is randomly taken from a file
and will keep track of the health of the player and helps the player input get put into the hidden work is it belongs there.
"""
class jumper():
    def __init__(self):
        self.jumper_word = str
        self.jumper_health = 6
        self.hidden_word = []
    def jumper_Image(self,health):

        """
        This will print aski art depending on how much hp the player has

        args (jumper, health): an instence of jumper and the health of the player
        """
        if health == 6:
            print("""
|------|    
|START!|            o/
|------|           /|
|      |           /|
---|_|---------________
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||
|| |-| ||   ||
|| |-| ||   ||
|| |-| ||   ||             
""")
        elif health == 5:
                print("""

---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||        //
|| |-| ||   ||        |
||_|-|_||___||       /o\       __________________
            ||~~~~~~~~~~~~~~~~~|5        
            |                  |4  |Water Level| 
            |                  |3 
            |                  |2
            |                  |1
             ------------------
    """)  
        elif health == 4:
                print("""
         
---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||        
|| |-| ||   ||        //
|| |-| ||   ||        |       __________________
|| |-| ||   ||       /o\      |5        
            |~~~~~~~~~~~~~~~~~|4  |Water Level| 
            |                 |3 
            |                 |2
            |                 |1
             -----------------
""")
        elif health == 3:
                print("""
       
---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||       
|| |-| ||   ||        
|| |-| ||   ||        //      __________________
|| |-| ||   ||        |       |5        
            |        /o\      |4  |Water Level| 
            |~~~~~~~~~~~~~~~~~|3 
            |                 |2
            |                 |1
             -----------------
""")
        elif health == 2:
                print("""
         
---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||       
|| |-| ||   ||        
|| |-| ||   ||                __________________
|| |-| ||   ||        //      |5        
            |         |       |4  |Water Level| 
            |        /o\      |3 
            |~~~~~~~~~~~~~~~~~|2
            |                 |1
             -----------------
""")  
        elif health == 1:
                print("""
       
---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||        
|| |-| ||   ||        
|| |-| ||   ||                __________________
|| |-| ||   ||                |5        
            |      //         |4  |Water Level| 
            |      |          |3 
            |     /o\         |2
            |~~~~~~~~~~~~~~~~~|1
             -----------------
""")  
        elif health == 0:
                print("""
      
---|_|---------_____  
|| |-| ||   || / 
|| |-| ||   ||  
|| |-| ||   ||  
|| |-| ||   ||        
|| |-| ||   ||                      
|| |-| ||   ||                __________________
|| |-| ||   ||                |5       
            |                 |4  |Water Level| 
            |       //        |3 
            |       |         |2
            |      /x\        |1
             -----------------
""")    


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
