import math

def guess_number(number):
    return input(F"Is the number {number}? Please answer 'yes', 'too high', or 'too low'.").lower()

def guessing_game_reverse():
    
    # set up tracking variables
    keep_going = True
    guess_range = list(range(101))
    guess_index = 50
    feedback = guess_number(guess_index)
    guess_count = 1
    
    # check base case
    if feedback == 'yes':
        print('I win!')
        keep_going = False
    
    # create guessing loop
    while keep_going == True:
        if feedback=='too high':
            guess_range = guess_range[:guess_index]
        if feedback=='too low':
            guess_range = guess_range[guess_index:]
        guess_index = math.floor(len(guess_range)/2)
        guess_count = guess_count+1
        feedback = guess_number(guess_range[guess_index])
        if feedback == 'yes':
            print(F'I win using {guess_count} guesses!')
            keep_going = False

guessing_game_reverse()