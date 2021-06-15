def max_of_three(one,two,three):
    max = 0
    if one > two:
        max = one
    else:
        max = two
    if max > three:
        return max
    else:
        return three