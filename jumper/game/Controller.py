class controller():
    """
    A code template for checking inputs from user to make sure that the input is always 1 letter
    not a number or multi letterspygame.examples.mask.main()

    stereotype: service provider
    """
    def check_letter(self, letter, word_list):
        """
        takes in the letter input from user and checks to see if it is only 1 letter and not a number
        or a letter that was already used.
        """
        if len(str(letter)) != 1:
            print("Please enter one letter.\n")
            return False

        elif letter in word_list :
            print("Please enter a letter that has not been entered yet.\n")
            return False

        elif letter in ["1","2","3","4","5","6","7","8","9","0"]:
            print("Please dont enter number.\n")
            return False

        else:
            return True

    