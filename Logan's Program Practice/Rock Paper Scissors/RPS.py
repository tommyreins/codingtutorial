import random 

print('Play Rock Paper Scissors with me.')

def choices() :
    while True :
        print('Choose rock / paper / scissors')
        player = input() 
        if (player == 'rock') or (player == 'scissors') or (player == 'paper') :
            computerlist = ['rock' , 'paper' , 'scissors']
            computer = random.choice(computerlist)
            print(computer)
            return player, computer
        else :
            print('Not a valid response')

def outcomes(player, computer) :
    if (player == 'rock') and (computer == 'scissors') :
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
    else :
        print('You Tied!')
        player , computer = choices()
        outcomes(player, computer)

player , computer = choices()
outcomes(player, computer)

