a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## list comprehension
## the item to append to a new is before the "for"
## the loop is in the middle
## the condition is at the end
evens = [x for x in a if x%2==0]

print (evens)