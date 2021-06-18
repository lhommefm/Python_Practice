import random

def pick_word():

    with open('sowpods.txt', "r") as scrabble_words:
        words = scrabble_words.readlines()
        words = [x.strip() for x in words]
        word = words[random.randint(0,len(words))]
        print(word)

pick_word()