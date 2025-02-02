import string
import random

def generate_name_based_username(full_name):
    full_name = full_name.lower().split()
    if len(full_name) > 1:
        first_letter = full_name[0][0]
        three_letters_surname = full_name[-1][:3].rjust(3, 'x')
        number = '{:03d}'.format(random.randrange(1, 999))
        username = '{}{}{}'.format(first_letter, three_letters_surname, number)
        return username
    else:
        return None

full_name = input("Enter your full name : ").strip()
name_based_username = generate_name_based_username(full_name)

if name_based_username:
    print("Your Username:", name_based_username)
else:
    print("Error: Please enter Full Name !.")