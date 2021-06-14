import random

a = random.sample( range(100), random.sample(range(1,11),1)[0] )

def list_ends(list):
    print(list)
    return [list[0], list[len(list)-1] ]

list_ends(a)