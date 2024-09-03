import random

low=1
high=100

number=random.randint(low,high)

guesses=0#initially the guess will be 0

while True:
    guess=int(input(f"Enter a number between {low} to {high}:"))
    guesses+=1#we append the number of guesses it takes to guess the right number
    
    if guess<number:
        print(f"{guess} is too low")
    elif guess>number:#here number is the var which we initialised outside the loop
        print(f"{guess} is too high")
    else:
        print(f"-----{guess }------ is the Correct Match")
        
        print(f"This time it took you {guesses} of guesses to guess the correct guess")

