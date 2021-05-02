""" 14) Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""

from itertools import chain


def create_list():
    for i in range(2):
        if i != 2:
            ask_user_input_1 = input("Enter the element for list 1 >> ").split(" ")
            ask_user_input_2 = input("Enter the element for list 2 >> ").split(" ")
            combined_list = [elements for elements in chain(ask_user_input_1, ask_user_input_2)]
            return combined_list


def unique_element_list(c_list):
    common_element = set(c_list)
    print(f"Combined list without duplicates : {list(common_element)}")


if __name__ == '__main__':
    print("Give the Input -- ")
    unique_element_list(create_list())

""" 15) Write a program (using functions!) that asks the user for a long 
string containing multiple words. Print back to the user the same string, 
except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My
shown back to me."""


def reverse_sentence():
    user_input = input("Enter the sentence : >> ").split(" ")
    return print(" ".join(user_input[::-1]))


if __name__ == '__main__':
    reverse_sentence()

# End
