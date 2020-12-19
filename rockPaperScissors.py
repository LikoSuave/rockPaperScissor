# This is a rock paper scissors game

import random, sys

print('Rock, Paper, Scissors!\n')

# These variables keep track of number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # Player input loop.
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uit\n')
        playerMove = input()
        if playerMove=='q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r,p,s, or q.\n')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK VERSUS...')
    elif playerMove == 'p':
        print('PAPER VERSUS...')
    elif playerMove == 's':
        print('SCISSORS VERSUS...')

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK\n')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER\n')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS\n')

    # Display and record the win/lose/tie:
    if playerMove == computerMove:
        print('IT IS A TIE!\n')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('YOU WIN!\n')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('YOU WIN!\n')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('YOU WIN!\n')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('YOU LOSE!\n')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('YOU LOSE!\n')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('YOU LOSE!\n')
        losses = losses + 1


