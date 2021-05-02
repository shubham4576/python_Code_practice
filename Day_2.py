""" 9) Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess
 the number, then tell them whether they guessed too low, too high, or exactly right.
 (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

# importing required modules
import random

# generate random number by computer
ranNum = random.randint(1, 9)

while True:
    askUserNum = int(input("Guess the Number >> "))

    if askUserNum > ranNum:
        print("Guessed No. is too high.")
        if str(input("Want to play more Yes or No ?? ")).lower() == "yes":
            continue
        else:
            print("Game Over. ThankYou for Playing.")
            break
    elif askUserNum < ranNum:
        print("Guessed No. is too low.")
        if str(input("Want to play more Yes or No ?? ")).lower() == "yes":
            continue
        else:
            print("Game Over. ThankYou for Playing.")
            break
    else:
        print(f"You guessed the correct number: {askUserNum}")
        if str(input("Want to play more Yes or No ?? ")).lower() == "yes":
            continue
        else:
            print("Game Over. ThankYou for Playing.")
            break

""" **) Addition Game for Abhijeet"""

import random

while True:
    ranNum_1 = random.randint(1, 1000)
    ranNum_2 = random.randint(1, 1000)
    askUserAns = int(input(f"Add the Number {ranNum_1} + {ranNum_2} >> "))
    if askUserAns == (ranNum_1 + ranNum_2):
        print(f"Your Ans {askUserAns} is Correct")
        if str(input("Want to play more Yes or No ?? ")).lower() == "yes":
            continue
        else:
            print("Game Over. ThankYou for Playing.")
            break
    else:
        print(f"Entered Ans {askUserAns} is wrong. Go and learn, How to do addition >> LOL ")
        if str(input("Want to play more Yes or No ?? ")).lower() == "yes":
            continue
        else:
            print("Game Over. ThankYou for Playing.")
            break


""" 10) This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
except require the solution in a
 different way.

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists 
(without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python 
using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python,
but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed 
on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, 
or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

Randomly generate two lists to test this"""

from itertools import chain
import random

list_1 = [random.randrange(1, 100, 5) for i in range(random.randint(1, 15))]
list_2 = [random.randrange(1, 100, 5) for i in range(random.randint(1, 15))]

common_Elements = []

eleWithDuplicates = [i for i in chain(list_1 + list_2)]
remove_Duplicates = [common_Elements.append(k) for k in eleWithDuplicates if k not in common_Elements]
print(common_Elements)

""" 11) Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, 
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below."""


def get_integer():
    return int(input("Enter a Number to check is it Prime or not ? >> "))


def check_prime():
    num = get_integer()
    a = [x for x in range(2, num) if num % x == 0]
    if num > 1:
        if len(a) == 0:
            return print(f"{num} is a Prime number.")
        else:
            return print(f"{num} is not a Prime number.")
    else:
        return print(f"{num} is not a Prime number.")


if __name__ == '__main__':
    check_prime()


""" 12) Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. For practice, write this code inside a function."""


def create_list():
    a_list = input("Enter the numbers for list >> ").split(" ")
    return a_list


def new_list(a_list):
    b = [a_list[0], a_list[len(a_list) - 1]]
    return print(f"List with last and first elements : {b}")


if __name__ == '__main__':
    new_list(create_list())


""" 13) Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter 
the number of numbers in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where 
the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
formula >> xn = xn−1 + xn−2
"""


def fibonnaci_seq(term):
    # First two numbers of fibonnaci series
    if term <= 1:
        return term

    else:
        return fibonnaci_seq(term - 1) + fibonnaci_seq(term - 2)


ask_user_length = int(input("Enter the length of Fibonnaci series you want >>> "))
if ask_user_length < 0:
    print("Please enter a positive integer.")
else:
    seq = [fibonnaci_seq(i) for i in range(ask_user_length)]
    print(f"Fibonnaci Sequence : {seq}")


# End



