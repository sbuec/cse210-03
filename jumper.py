# create image of jumping man
# image gets shorter with each incorrect guess from main

jumpMan = [
" ___ ",
"/___\\",
"\   /",
"  O  ",
" /|\ ",
" / \ ",]

running = True
mistakes = 0
while running:
    # user input, if bad guess mistakes +=1
    if mistakes > 2:
        jumpMan[3] = "  X  "
        for i in range(mistakes, 6, 1):
            print(jumpMan[i])
            running = False
    else:
        for i in range(mistakes, 6, 1):
            print(jumpMan[i])

