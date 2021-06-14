import random
import string
import copy

def create_num():
    number = [random.choice(string.digits), random.choice(string.digits), random.choice(string.digits), random.choice(string.digits)]
    return number

def check_num(guess, num):
    cows = 0
    bulls = 0

    # strip correct values from the num to check for bulls that do not duplicate cows  
    num_without_cows = copy.deepcopy(num)

    # loop through guess using enumerate to get index value, checking for cows 
    for idx, val in enumerate(guess):
        if val == num[idx]:
            cows = cows+1
            num_without_cows[idx] = "#"
    
    num_without_cows = ''.join(num_without_cows)

    # loop through guess using enumerate to get index value, checking for bulls
    for idx, val in enumerate(guess):
        if val in num_without_cows:
            bulls = bulls+1
            num_without_cows.replace(val, "#", 1)
    
    print(F'Guess: {guess}: {cows} cows, {bulls} bulls')
    return(cows)

def play_cows_bulls():
    number = create_num()
    count = 0
    won = False
    while won == False:
        guess = input("What is your four digit guess?")
        if check_num(guess, number) == 4:
            count = count+1
            print(F"You win using {count} guesses!")
            won = True
        else:
            count = count+1

play_cows_bulls()