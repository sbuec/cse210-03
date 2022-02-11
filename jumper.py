"""
Program: Jumpman

Authors: Daniel Jones(Lead), Steven Buechele, Eric Woll, Tebakaro Tione
"""

from jumpImg import *
from playerinput import PlayerInput
from wordguess import WordGuess

def main():
    jumpman = jumpImg()
    jumpman.picture()

    '''
    Still needed:
    * Commands in main() to create the word and interact with the player
    * Way to count number of bad guesses from player
    Something like:

    if BAD_GUESS:
        jumpman.mistakes += 1

    if jumpman.mistakes > 2:
        END GAME HERE
    '''

if __name__ == '__main__':
    main()