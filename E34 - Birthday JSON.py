import json

birthday_seed = {
    "Albert Einstein" : "01/01/1901",
    "Benjamin Franklin" : "02/01/1901",
    "Ada Lovelace" : "03/01/1901"
}

# function to write the birthday_list to a JSON file
def create_birthday_json(data):
    with open("birthday.json", "w") as b:
        json.dump(birthday_seed, b)

# function to add to the JSON file
def add_birthday_json():
    with open("birthday.json", "r") as b:
        birthday_seed = json.load(b)
        name = input("Who's birthday do you want to add?").strip().title()
        birthday = input("What is their birthday?").strip()
        if name not in birthday_seed.keys():
            birthday_seed[name] = birthday
            print(F"{name}, with birthday {birthday} was added to the database.")
        else:
            print("That person is already in the database.")
    with open("birthday.json", "w") as b:
        json.dump(birthday_seed, b)

# function to read birthdays
def birthday_dictionary():
    
    with open("birthday.json", "r") as b:
        birthday_list = json.load(b)
    
    def birthday_list_text(birthday_list):
        for x in birthday_list.keys():
            print(x)
    
    def birthday_search(name):
        return birthday_list.get(name, None)

    print(F"Welcome to the birthday dictionary. We know the birthday's of:")
    birthday_list_text(birthday_list)
    
    request = input("Who's birthday do you want to look up?").title()
    birthday = birthday_search(request)
    if birthday == None:
        print(F"We can't find {request.title()}'s birthday.")
    else:
        print (F"{request.title()}'s birthday is {birthday_search(request)}.")

birthday_dictionary()