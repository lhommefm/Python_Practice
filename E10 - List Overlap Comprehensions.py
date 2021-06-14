import random

# range creates a sequence of numbers from start (default 0) to the defined length, non-inclusive
# assign "a" and "b" to be a list of numbers from range 0-99
# have the list length be randomly selected from 1-14
a = random.sample( range(100), random.sample(range(1,15),1)[0] )
b = random.sample( range(100), random.sample(range(1,15),1)[0] )

print (a)
print (b)

def common (a,b):
    doubles = [x for x in a if x in b]
    return doubles

common(a,b)