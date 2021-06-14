import math

def ask_number(question="Give me a number:"):
    answer = int(input(question))
    return answer

def calc_divisors(number):
    possible = range(2,math.floor(number/2))
    divisors = [x for x in possible if number%x==0]
    return divisors

def prime():
    number = ask_number()
    if len(calc_divisors(number))==0:
        return True
    else:
        return False

prime()
