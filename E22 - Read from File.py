from collections import Counter

with open('Training_01.txt', "r") as open_file:
    
    # read the file as a list of strings (with line breaks), and strip out the line breaks
    text = open_file.readlines()
    text = [x.strip() for x in text]

    # pull the 3rd part of the URL to extract the category
    category_list = [x.split("/")[2] for x in text]
    
    # use Counter to count elements in the list
    print(Counter(category_list))
