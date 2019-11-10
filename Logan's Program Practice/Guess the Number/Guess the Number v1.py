#The goal of creating this is to create a program that will...
#...randomly generate a number, then tell you higher or lower after a guess until you guess it.


#I looked online on how to generate random numbers and it sent me to the "import random"
#After researching the import command for more info i found that it will call in another module...
#...python has modules built into it for basic uses such as the "sys" i have seen, as well as "random"
import random

#I believe "randint" is a function in the module and "random.randint()" searches for that spcific function in it
#"random.randint(x,y)" will choose a random number between two values x and y 
randomint = random.randint(1,21)
print('Guess a number between 1 and 20.')

#This is a loop to see if the users input is the same, and to say if it is higher or lower, then guess again
while True : # this sets the loop to run forever because "while" runs as long as it evaluates to true, and by saying "True" it means it will evaluate to true
    guess = int(input()) #the variable "guess" is being set equal to the users input, then being turned into an integer
    if guess == randomint : #when the users input is equal to the random number 
        print('You guessed it!') # then print this
        break # and stop the loop
    elif guess < randomint : #if the user input is less than the random number
        print('Higher!') #then tell me to guess higher and return me to the top of the loop
    elif guess > randomint : # if guess is greater than the number 
        print('Lower!') #then tell me to guess lower and return to the top


    

