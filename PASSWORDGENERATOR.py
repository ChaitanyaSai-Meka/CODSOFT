import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))

length = int(input("Enter password length: "))
print("Your generated password is:", generate_password(length))
