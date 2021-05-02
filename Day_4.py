""" 16) Write a password generator in Python. Be creative with how you generate passwords - strong
passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time
the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""


import random
import array
import string


def user_input():
    pass_len = int(input("Enter the length of password you Want >> "))
    return pass_len


def generate_list():
    digits = [str(i) for i in range(10)]
    lowercase_letters = [k for k in string.ascii_lowercase]
    uppercase_letters = [j for j in string.ascii_uppercase]
    symbol = [h for h in list(set(string.punctuation))]

    combined_list = digits + lowercase_letters + uppercase_letters + symbol

    return digits, lowercase_letters, uppercase_letters, symbol, combined_list


def generate_pass(val):
    rand_digit = random.choice(val[0])
    rand_lower = random.choice(val[1])
    rand_upper = random.choice(val[2])
    rand_symbol = random.choice(val[3])

    temp_passwd = rand_digit + rand_lower + rand_symbol + rand_upper
    for x in range(user_input() - 4):
        temp_passwd = temp_passwd + random.choice(val[4])
        temp_passwd_list = array.array('u', temp_passwd)
        random.shuffle(temp_passwd_list)

    password = ''
    for g in temp_passwd_list:
        password += g

    return print(f"Here is Your Password: {password}")


if __name__ == '__main__':
    print("welcome to password generator".upper())
    list_val = generate_list()
    generate_pass(list_val)


# End
