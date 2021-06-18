import json
from datetime import datetime
from collections import Counter

# function to read birthdays and count the frequency of each month
def count_birthday_months():
    
    with open("birthday.json", "r") as b:
        birthday_list = json.load(b)
    
    # strptime to convert from string to a datetime object, and stfttime to pull out the month text
    birthdays_list = birthday_list.values()
    birthdays_list = [datetime.strptime(x,'%m/%d/%Y').strftime("%B") for x in birthdays_list]

    # Counter to summarize into an object with counts of each month
    counts = Counter(birthdays_list)
    print(counts)

count_birthday_months()