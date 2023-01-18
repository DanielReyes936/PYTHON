import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

length = int(input("Enter the desired length of the password: "))
print("Generated password: ", generate_password(length))
