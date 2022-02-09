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


class WordGuess:
    '''Displays and manages the word to guess'''

    def break_word(word:str) -> list:
        '''Breaks word into a list of characters'''
        return [char for char in word]
        
    def fill(characters:list) -> list:
        '''Fills guessed character list with '_' '''
        word = []
        for letter in characters:
            word.append([letter, '_'])
        return word

    def display(characters: list) -> None:
        '''Displays guessed character list'''
        for letter in range(len(characters)):
            print(characters[letter][1], end=' ')

    def update(user_guess: str, word: list) -> list:
        '''Updates guessed character list'''
        for letter in word:
            if letter[0] == user_guess.lower():
                letter[1] = letter[0]
        return word
    
    def isIncomplete(word: str) -> bool:
        '''Checks for '_' in guesse list'''
        check = []
        for letter in word:
            if letter[1] == '_': check.append('True')
        else: check.append('False')

        if 'True' in check: return True
        else: return False

    def show_word(characters:list) -> None:
        '''Shows the word player had to guess for current round'''
        new_list = [char[0] for char in characters]
        print('Your word was: ', end='')
        for item in new_list:
            print(item, end='')
        print()
