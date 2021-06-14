def odd_even ():
    number = int(input("What number should I check?"))
    divisor = int(input("What number should I divide by?"))
    if number%4 == 0:
        print("The number is divisible by four")
    if number%2 == 1:
        print("The number is odd")
    else: 
        print("The number is even")
    if number%divisor == 0:
        print("The 2nd number divides evenly into the 1st number")
    else:
        print("There is a remainder")

odd_even()