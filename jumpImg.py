class jumpImg:
    def __init__(self):
        self.image = [
        " ___ ",
        "/___\\",
        "\   /",
        "  O  ",
        " /|\ ",
        " / \ "]
        self._mistakes = 0

    def picture(self):
        if self._mistakes > 2:
            self.image[3] = "  X  "

        for i in range(self._mistakes, len(self.image)):
            print(self.image[i])
        print()
        print(f'Incorrect guesses: {self._mistakes}')
    
    def get_mistakes(self):
        return self._mistakes
    
    def set_mistakes(self, amount: int):
        self._mistakes = amount
        print(self._mistakes)