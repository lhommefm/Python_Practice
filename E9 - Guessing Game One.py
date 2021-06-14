import random 

def guessing_game():
    number = random.randint(1,9)
    guess = 0
    guess_count = 0
    while guess != number:
        guess = input("Guess a number between 1 and 9, or type 'exit' to stop playing")
        if guess == 'exit':
            break
        else:
            if int(guess) > number:
                print("Your guess is too high.")
                guess_count = guess_count+1
            elif int(guess) < number:
                print("Your guess is too low.")
                guess_count = guess_count+1
            elif int(guess) == number:
                guess_count = guess_count+1
                print(F'You are correct! You took {guess_count} guesses.')
                break
            else:
                print("You entered an incorrect guess")
                
guessing_game()