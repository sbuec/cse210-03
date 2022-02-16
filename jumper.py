'''
Authors:
    Daniel Jones = washu-misaki, 
    Steven Buechele = sbuec, 
    Eric Woll = steelheart96, 
    Tebakaro Tione = tebtione, 
    Connor Baltich = canadianbleach
'''

from jumpimg import jumpImg
from playerinput import PlayerInput
from util import util
from wordguess import WordGuess

def main():
    # Create and start a new game
    game = hangman()
    game.start()

class hangman:
    ''' The class to control all classes. The games container.'''
    def __init__(self) -> None:
        self.word = WordGuess()
        self.player = jumpImg()
        self.mistakes = 0
        self.win = False

    def start(self):
        ''' This is the only method that needs to be called to start.'''
        run = True
        while run:

            no_input = True
            while no_input:

                util.clear()
                self.word.display()
                print()
                self.player.picture()
                print(f"Guessed Characters: {self.word.chars_guessed}")

                user_guess = PlayerInput.retrieve('Guess a letter [a-z]: ')
                no_input = PlayerInput.isBadInput(user_guess)
                if no_input:
                    print('That input is not accepted.')
                    util.wait(3)

            if self.word.check_spot(user_guess):

                self.word.add_guessed_char(user_guess)

                if self.word.isCorrect(user_guess):
                    self.word.update(user_guess)
                else:
                    self.mistakes += 1
                    self.player.set_mistakes(self.mistakes)

            run = self.word.isIncomplete()

            if self.mistakes >= 3:
                run = False

            if run == False:
                util.clear()
                self.word.display()
                print()
                self.player.picture()
                print(f"Guessed Characters: {self.word.chars_guessed}")
                print(self.word.hidden_word)
    
                end = self.endGame()

                if not end:
                    self.reset()
    
    def reset(self):
        self.word = WordGuess()
        self.player = jumpImg()
        self.mistakes = 0
        self.win = False
        self.start()
    
    def endGame(self):
        if (self.win):
            print("Great win!")
        else:
            print("Better luck next time!\n")

        usr_response = PlayerInput.retrieve("Would you like to play again? [y/n] ")

        if (usr_response == 'y'): return False
        elif (usr_response == 'n'): return True
        else:
            print("A valid input was not given. Bye.")
            return True

if __name__ == '__main__':
    main()