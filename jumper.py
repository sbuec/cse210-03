# create image of jump man
# image gets shorter with each incorrect guess from main

class jumpImg:
    jumpMan = [
    " ___ ",
    "/___\\",
    "\   /",
    "  O  ",
    " /|\ ",
    " / \ "]
    
    lineNum = 6
    mistakes = 0
    while mistakes < 3:
        i = mistakes
        while i < lineNum:
            print(jumpMan[i])
            i += 1
        print("\n")
        mistakes += 1
    if mistakes >= 3:
        i = mistakes + 1
        print("  X  ")
        while i < lineNum:
            print(jumpMan[i])
            i += 1
