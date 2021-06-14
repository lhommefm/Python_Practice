import random

a = random.sample(range(1, 30),10)
b = random.sample(range(1, 30),15)

def overlap(list_a, list_b):
  duplicate = [x for x in list(set(list_a)) if x in list_b]
  print (a, b, duplicate)

overlap(a,b)