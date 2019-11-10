#The goal of this program is to play a game of rock paper scissors against the computer.
#I will input my choice then have the computer choose one randomly and say who won

import random #I am bringing in the built in 'random' module to use for the computers choice

print('Play Rock Paper Scissors with me.')

#THIS IS NOT WORKING. MISSING SOME UNDERSTANDING OF FUNCTIONS. WILL RETURN.
def choices() :
    while True :
        print('Choose rock / paper / scissors')
        player = input() 
        if (player == 'rock') or (player == 'scissors') or (player == 'paper') :
            computerlist = ['rock' , 'paper' , 'scissors']
            computer = random.choice(computerlist)
            break
        else :
            print('Not a valid response')

choices()
print(computer)

if player == computer :
    print('Tie!')
    choices()
elif (player == 'rock') and (computer == 'scissors') :
    print('You Win!')
elif (player == 'scissors') and (computer == 'paper') :
    print('You Win!')
elif (player == 'paper') and (computer == 'rock') :
    print('You Win!')
elif (player == 'rock') and (computer == 'paper') :
    print ('You Lose!')
elif (player == 'scissors') and (computer == 'rock') :
    print ('You Lose!')
elif (player == 'paper') and (computer == 'scissors') :
    print ('You Lose!')
elif (player == 'rock') and (computer == 'paper') :
    print ('You Lose')