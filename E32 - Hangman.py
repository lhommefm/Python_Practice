import random

def hangman():

    # define hangman art
    hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # helper function to pick a word
    def pick_word():
        with open('sowpods.txt', "r") as scrabble_words:
            words = scrabble_words.readlines()
            words = [x.strip() for x in words]
            return words[random.randint(0,len(words))].lower()
    
    # helper function to print the current state of the word
    def print_word(word, past_guesses):
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
    def letter_input(past_guesses, word):
        guess = input("Guess your letter or enter 'quit' to quit:")
        if guess in past_guesses:
            print("You've guessed that letter already. Please try again.")
            return 0
        elif guess == word:
            return 1
        else: 
            return guess

    # helper function to check if game won
    def check_game_won(word, past_guesses):
        missing_letters = [x for x in word if x not in past_guesses]
        return len(missing_letters) == 0
 
    # helper function to play a round
    def play_a_round():
        
        # set up variables
        past_guesses = []
        guess_counter = 0
        word = pick_word()
        game_won = check_game_won(word, past_guesses)
        
        # kick off game
        print("Welcome to Hangman!")
        
        # run game loop
        while game_won == False and guess_counter < 6:
            print("\n")
            print_word(word, past_guesses)
            print(F'Past guesses: {past_guesses}. {hangman_pics[guess_counter]}')
            guess = letter_input(past_guesses, word)
            if guess == 'quit':
                game_won = "Quit"
                break
            elif guess == '1':
                game_won = True
                break
            elif guess != 0:
                print(F'You guessed: {guess}')
                past_guesses.append(guess)
                if guess not in word:
                    guess_counter = guess_counter + 1
            game_won = check_game_won(word, past_guesses)
        
        # end the round
        if game_won == True:
            print("\n")
            print(print_word(word, past_guesses))
            print("You win!")
        if guess_counter == 6:
            print("\n")
            print(F"You lose. The word was '{word}'.")
    
    continue_playing = True
    while continue_playing == True:
        play_a_round()
        continue_playing = input("Play again? Type 'yes' to start a new round") == 'yes'

hangman()