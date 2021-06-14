def divisors():
    number = int(input("Pick a number"))
    test_range = range(2,number)
    divisor = [x for x in test_range if number%x == 0]
    print(divisor)

divisors()