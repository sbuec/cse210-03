# create image of jumping man
# image gets shorter with each incorrect guess from main
class jumpImg:
    def __init__(self):
        # Sets self.image as default picture of man jumping stored 
        self.image = [
        " ___ ",
        "/___\\",
        "\   /",
        "  O  ",
        " /|\ ",
        " / \ "]
        # Creates self.mistakes variable to keep track of number of bad guesses
        self.mistakes = 0

    '''
    Checks number of mistakes
    Prints image line by line, skips 1 line per mistake
    If mistakes > 2, 
        *change image head from 'O' to 'X'
        *display image of jumper
    '''
    def picture(self):
        if self.mistakes > 2:
            self.image[3] = "  X  "
        for i in range(self.mistakes, 6):
            print(self.image[i])
        print()
        print(f'Incorrect guesses: {self.mistakes}')
