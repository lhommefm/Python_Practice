def guess_letters(word):
    
    # helper function to print the current state of the word
    def print_word():
        counter = 0
        word_to_print = ""
        while counter < len(word):
            if word[counter] in past_guesses:
                word_to_print = word_to_print + " " + word[counter]
            else:
                word_to_print = word_to_print + " _"
            counter = counter + 1
        print(word_to_print)

    # helper function to request a letter
    def letter_input():
        guess = input("Guess your letter or enter 'quit' to quit:")
        if guess in past_guesses:
            print("You've guessed that letter already. Please try again.")
        else: 
            past_guesses.append(guess)
            return guess

    # helper function to check if game won
    def check_game_won():
        missing_letters = [x for x in word if x not in past_guesses]
        return len(missing_letters) == 0
 
    # set up variables
    past_guesses = []
    game_won = check_game_won()
    
    # kick off game
    print("Welcome to Hangman!")
    
    # run game loop
    while game_won == False:
        print("\n")
        print_word()
        print(F'Past guesses: {past_guesses}')
        guess = letter_input()
        if guess == 'quit':
            game_won = "Quit"
            break
        else:
            print(F'You guessed: {guess}')
        game_won = check_game_won()
    if game_won == True:
        print("\n")
        print(print_word())
        print("You win!")
    

guess_letters("evaporate")
