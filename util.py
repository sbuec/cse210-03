from os import system
from time import sleep

class util:
    '''Input, input validation, and other utilites.'''
    def clear():
        '''Clears the Terminal.'''
        system('cls')

    def wait(amount: int):
        '''Pauses the terminal for "amount" of seconds'''
        sleep(amount)