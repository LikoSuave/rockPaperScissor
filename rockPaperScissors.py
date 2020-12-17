# This is a rock paper scissors game

import random, sys

print('Rock, Paper, Scissors!\n')

# These variables keep track of number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins. losses, ties))
    while True: # Player input loop
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uit\n') 