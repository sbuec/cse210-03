"""
Program: Jumpman

Authors: Daniel Jones(Lead), Steven Buechele, Eric Woll, Tebakaro Tione
"""


class PlayerInput:
    '''Retrieves user input and returns a single character'''

    def retrieve(display_message:str) -> str:
        '''Retrieves user input'''
        return input(display_message)
    
    def isBadInput(user_input:str) -> bool:
        '''Checks for incorrect user input'''
        if len(user_input) > 1 or len(user_input) == 0:
            return True
        else:
            if user_input.isnumeric(): return True
            else: return False
    
    def isCorrect(characters:list, user_guess:str) -> bool:
        '''Check to see if user guess is correct'''
        new_list = [char[0] for char in characters]

        if user_guess.lower() in new_list: return True
        else: return False
    
    def check_spot(user_guess, word) -> bool:
        '''Checks to see if letter has already been guessed'''
        for letter in word:
            if letter[0] == user_guess.lower():
                if letter[1] != '_':
                    return False
        return True
