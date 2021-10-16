class controller():
    
    def check_letter(self, letter, word_list):
    
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

    