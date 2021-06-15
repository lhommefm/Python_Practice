with open('happynumbers.txt', "r") as happy_numbers:   
    text = happy_numbers.readlines()
    happy_numbers = [int(x.strip()) for x in text]

with open('primenumbers.txt', "r") as prime_numbers:   
    text = prime_numbers.readlines()
    prime_numbers = [int(x.strip()) for x in text]

overlap = [x for x in prime_numbers if x in happy_numbers]

print(overlap)