def birthday_dictionary():
    birthday_list = {
        "Albert Einstein" : "01/01/1901",
        "Benjamin Franklin" : "02/01/1901",
        "Ada Lovelace" : "03/01/1901"
    }
    
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