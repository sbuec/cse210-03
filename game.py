def GameOver():
    # Loop until either the player has won or lost
    GameOver = False
    while not GameOver:
        # If the player has won print a win message or increase attempts
        if (all('_' == char for char in word)):
            print('Congrats, you won!')
            GameOver = True
        # If the player has lost, print failing and stop looping
        if (attempts >= max_attempts):
            print('You lost, try again!')
            GameOver = True
