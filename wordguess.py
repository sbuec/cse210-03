from random import choice

class WordGuess:
    '''Displays and manages the word to guess'''

    def __init__(self) -> None:
        self.chars_guessed = []
        self.list_of_words = self.WordList('words.txt')
        self.hidden_word = self.list_of_words.find_one()
        self.break_word()
        self.fill()

    def break_word(self):
        '''Breaks word into a list of characters'''
        self._characters = [char for char in self.hidden_word]
        
    def fill(self) -> list:
        '''Fills guessed character list with '_' '''
        self.filled_charList = []
        for letter in self._characters:
            self.filled_charList.append([letter, '_'])

    def display(self) -> None:
        '''Displays guessed character list'''
        for letter in range(len(self._characters)):
            print(self.filled_charList[letter][1], end=' ')

    def update(self, user_guess: str) -> list:
        '''Updates guessed character list'''
        for letter in self.filled_charList:
            if letter[0] == user_guess.lower():
                letter[1] = letter[0]
    
    def isIncomplete(self) -> bool:
        '''Checks for '_' in guesse list'''
        check = []
        for letter in self.filled_charList:
            if letter[1] == '_': check.append('True')
        else: check.append('False')

        if 'True' in check: return True
        else: return False
    
    def add_guessed_char(self, character: str):
        self.chars_guessed.append(character)
    
    def isCorrect(self, user_guess:str) -> bool:
            '''Check to see if user guess is correct'''

            if user_guess.lower() in self._characters: return True
            else: return False

    def check_spot(self, user_guess):
        for letter in self.filled_charList:
            if letter[0] == user_guess.lower():
                if letter[1] != '_':
                    return False
        return True

    class WordList:
        '''Reads a text file and returns it as a list'''

        def __init__(self, text_file) -> str:
            self.file = text_file
            self.read_file()
            self.strip_list()
        
        def read_file(self):
            with open(self.file) as file:
                self.hidden_word = file.readlines()
            
        def strip_list(self):
            self.striped_list = [item.strip() for item in self.hidden_word]

        def find_one(self):
            return choice(self.striped_list)