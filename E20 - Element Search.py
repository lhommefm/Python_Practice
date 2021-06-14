import math
import random
import copy

# test array is an ordered list of numbers
# '*' behaves like '...' in JS to unpack
test_array_range = [*range(100)]
test_array = [x for x in test_array_range if random.uniform(0,1) > .6]
test_number = math.floor(random.uniform(0,100))
print(test_array, test_number)

# check if number is in the list
def check_in_list(array, number):
    array_dup = copy.deepcopy(array)

    result = False
    keep_going = True
    while keep_going == True:
        midpoint_pointer = math.floor(len(array_dup)/2)
        midpoint_value = array_dup[midpoint_pointer]
        print(F'midpoint_pointer: {midpoint_pointer}, midpoint_value: {midpoint_value}')
        print(F'array: {array_dup}')
        
        # condition where number is in the list and midpoint: result is true
        if number == midpoint_value:
            result = True
            keep_going = False
        
        # if it is the only number left in the list or is between the left and right numbers: result stays false
        elif len(array_dup) == 1 or (number > array_dup[midpoint_pointer-1] and number < array_dup[midpoint_pointer+1]):
            result = False
            keep_going = False
        
        # otherwise cut the list in half
        elif number > midpoint_value:
            array_dup = array_dup[midpoint_pointer:]
        else:
            array_dup = array_dup[:midpoint_pointer]

    return result

check_in_list(test_array,test_number)