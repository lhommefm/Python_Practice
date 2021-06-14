a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_ten(list):
    max = int(input("What is the max number for the new list?"))
    # less_than = []
    # for x in list:
    #     if x < max:
    #         less_than.append(x)
    less_than = [x for x in list if x < max]
    print(less_than)

less_than_ten(a)