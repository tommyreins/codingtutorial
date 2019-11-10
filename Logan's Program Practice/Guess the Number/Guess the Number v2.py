#The first version works, but it breaks if you enter in something other than an integer
#This version is the same but checks to see if the input is an integer, and if its not, makes them try again
import random

randomint = random.randint(1,21)
print('Guess a number between 1 and 21.')

while True:
    while True : #I am setting up a loop within a loop so that it checks if the number is an integer
        try : #See if this condition is True
            guess = int(input()) #Is the input an integer?
            break # If it is break this loop and go onto the next loop, the rest of the program
        except : #If it is not True
            print('Please enter a number between 1 and 20') #Tell them to enter an integer and return to the top of the loop to try again
    if guess == randomint :
            print('You guessed it!')
            break
    elif guess < randomint :
            print('Higher')
    elif guess > randomint : 
            print('Lower')
