from datetime import date

def character_input ():
    name = input("What is your name?")
    age = int(input("What is your age?"))
    repeat = int(input("How many times should I sohw the message?"))
    year = date.today().year
    additional_years = 100-age
    hundred_years_old = additional_years + year
    print(repeat * F'{name}, you will turn 100 years old on {hundred_years_old} \n')

character_input()