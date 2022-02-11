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