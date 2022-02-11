'''
Hangman Project

Contributors:
    Connor Baltich, add your name once you contribute
'''

from os import system
import random


def main():
    # Create and start a new game
    game = hangman()
    game.start()

class hangman:
    ''' The class to control all classes. The games container.'''
    def __init__(self) -> None:
        self.c = hangman.character()
        self.wb = hangman.wordBank()

    def checkForWin(self):
        count = 0
        for c in self.wb.charsGuessed:
            if (c in self.wb.secretWord):
                count += 1
        return self.wb.correctChars == count

    def start(self):
        ''' This is the only method that needs to be called to start.'''
        playing = True
        win = True
        while playing:
            self.c.display()
            self.wb.displayHiddenWord()
            print()
            print(f"Guessed Characters: {self.wb.charsGuessed}")
            # Get input check for win and loss
            if (not self.wb.guessAndCheck("What character would you like to guess [a-z]: ")):
                if (not self.c.removeSection()):
                    playing = False
                    win = False
            if (self.checkForWin()):
                playing = False
            print()
            input("Press 'Enter' to continue...")
            util.clear()
        
        self.c.display()
        self.wb.displayHiddenWord()
        self.endGame(win)

    def reset(self):
        self.c = hangman.character()
        self.wb = hangman.wordBank()
        self.start()
    
    def endGame(self, win:bool):
        if (win):
            print("Great win!")
        else:
            print("Better luck next time!")

        ans = util.getInput("Would you like to play again? y/n ", 1)
        if (ans == 'y'):
            self.reset()
        elif (ans == 'n'):
            quit()
        else:
            print("A valid input was not given. Smh, bye.")

    class character:
        ''' For drawing character and tracking body parts '''
        def __init__(self):
            self.guess = 0
            self.jumpMan = [
            "   ___   ",
            "  /___\  ",
            "  \   /  ",
            "   \ /   ",
            "    O    ",
            "   /|\   ",
            "   / \   ",
            "         "]

        def display(self):
            ''' Print jumpman to screen '''
            for i in self.jumpMan:
                print(i)

        def removeSection(self):
            if (self.guess == 3):
                self.jumpMan[self.guess] = ""
                self.jumpMan[4] = "    X    "
                return False;
            else:
                self.jumpMan[self.guess] = ""
                self.guess += 1
                return True;

    class wordBank:
        ''' Manages guesses and creating words '''
        def __init__(self):
            self.words = [
                "abyss",
                "galaxy",
                "france",
                "code",
                "python"
            ]
            self.secretWord = self.getWord()
            self.charsGuessed = []
            self.correctChars = self.calcUnique()           

        def calcUnique(self):
            '''Calcs the correct number of unique'''
            chars = []
            numDiff = 0
            for letter in self.secretWord:
                if (letter not in chars):
                    chars.append(letter)
                    numDiff += 1
            return numDiff
        
        def getWord(self):
            '''Returns word from wordlist and removes it'''
            word = random.choice(self.words)
            self.words.remove(word)
            return word

        def displayHiddenWord(self):
            str = ""
            for i in self.secretWord:
                if (i in self.charsGuessed):
                    str += f"{i} "
                else:
                    str += "_ "
            print(str)

        def checkGuess(self, guess):
            '''Check if the parameter is in the secret word'''
            self.charsGuessed.append(guess)
            if (guess in self.secretWord):
                print(f"Great! There was a(n) {guess} in the secret word!")
                return True;
            else:
                print(f"Sorry! There is not a(n) {guess} in the secret word!")
                return False;

        def guessAndCheck(self, prompt):
            '''Get guess and check answer'''
            used = True
            while used:
                guess = util.getInput(prompt, 1)
                if (guess not in self.charsGuessed):
                    used = False
                else:
                    print("You already guessed that! Try another one!")

            return self.checkGuess(guess)

class util:
    '''Input, input validation, and other utilites.'''
    def clear():
        '''Clears the Terminal.'''
        # My linter says rewrite without using the shell but no
        system('cls')
    
    def getInput(prompt, maxLength):
        '''Gets input of a certain length'''
        while True:
            inp = input(prompt)
            if (inp.isalpha() and len(inp) <= maxLength):
                return inp
            else:
                print("That input was not valid. Please try again.")

    
if __name__ == '__main__':
    main()