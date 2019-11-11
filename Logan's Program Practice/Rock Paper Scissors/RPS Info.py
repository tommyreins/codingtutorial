#The goal of this program is to play a game of rock paper scissors against the computer.
#I will input my choice then have the computer choose one randomly and say who won

import random #I am bringing in the built in 'random' module to use for the computers choice

print('Play Rock Paper Scissors with me.') # Introducing the game

#This function makes sure that the input is one of the three valid options
def choices() : #Define the function choices()
    while True : #Sets up an infinite loop until it sees break
        print('Choose rock / paper / scissors') #gives the options
        player = input() #asks for an input and sets it to the variable 'player'
        if (player == 'rock') or (player == 'scissors') or (player == 'paper') : #will move on if the input is one of the options
            computerlist = ['rock' , 'paper' , 'scissors'] # sets of the list of option and sets the list to the variable 'computerlist'
            computer = random.choice(computerlist) #chooses at random out of the list and sets it to the variable computer
            print(computer) #prints the computers random choice
            return player, computer #this is setting the value of the function temporarily to 'choices(player, computer) so that i may use those values when i set the function equal variables
        else : #if the input is 'rock' or 'paper or 'scissors'
            print('Not a valid response') # then tell them this and return to the top of the loop to try again

def outcomes(player, computer) : #This is defining the function and setting the variables i want to bring into this function
    if (player == 'rock') and (computer == 'scissors') : #This is the list of possible outcomes of the game
        print('You Win!') #This is what to print if the conditions are met
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
    else : #if none of the conditions were met, then it was a tie.
        print('You Tied!') #print that it was a tie
        player , computer = choices() #then run it through the choices function again
        outcomes(player, computer) #then run it back through this function again

player , computer = choices() #run this function and set the users RPS choice and the computers RPS choice to these variables
outcomes(player, computer) #run this functions using the two variables decided above
