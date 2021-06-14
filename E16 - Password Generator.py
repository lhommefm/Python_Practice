import random
import string

weak_password_list = ['password', 'pass', 'abc123', 'mypassword']
options = "".join(string.ascii_letters + string.digits + string.punctuation)

def create_password():
    strength = input("How strong do you want your password to be?")
    if strength == "strong":
        length = random.choice(range(15,20))
        password = ""
        count = 0
        while count < length:
            password += random.choice(options)
            count = count+1
        return password
    if strength == "weak":
        password = random.choice(weak_password_list)+random.choice(weak_password_list)
        return password

create_password()