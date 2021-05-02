""" 1) Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the
year that they will turn 100 years old."""

from datetime import date
from itertools import chain

userName = input("Enter Your name >> ")
userAge = int(input("Enter Your age >> "))
currentDate = date.today()
type(userName)
year = (currentDate.year-userAge) + 100

print(f"Hi {userName}, You will turn 100 in year {year}")

# End of program

""" 2) Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2 ?"""

askUserNum = int(input("Enter the number of your choice >> "))

if askUserNum % 2 == 0:
    print(f"Entered number {askUserNum} is even.")
    if askUserNum % 4 == 0:
        print(f"Entered number {askUserNum} is a multiple of 4")
else:
    print(f"Entered number {askUserNum} is odd.")

num = int(input("Enter the number to check >> "))
check = int(input("Enter the number by which above number will be tested if\nit "
                  "is divisible or not by this number ?? >> "))

if num % check == 0:
    print(f"\n{num} is evenly divisible by {check}.")
else:
    print("\nPlease enter the appropriate numbers. Thank You")

""" 3) Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5."""

askUserNum = int(input("Enter the number >> "))
ranList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# numLess = []
# for num in ranList:
#     if num <= 5:
#         numLess.append(num)

numLess = [num for num in ranList if num <= askUserNum]

print(f"List of numbers less than 5 is {numLess}")

""" 4) Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

askUserNum = int(input("Enter a number between 1 to 100 to find it's divisors >> "))
divisor_List = [num if askUserNum in range(1, 101) else print("Enter the number in range.")
                for num in range(1, 101) if askUserNum % num == 0]

print(f"List of divisors of {askUserNum} is {divisor_List}")

""" 5) Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)"""


list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ele_List_With_Duplicate = [elements for elements in chain(list_1, list_2) if elements in list_1
                           if elements in list_2]
common_Elements = []
for i in ele_List_With_Duplicate:
    if i not in common_Elements:
        common_Elements.append(i)

print(common_Elements)

""" 6) Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

string = input("Enter the string to check whether it is or not a Palindrome >> ").lower()

if string[:] == string[::-1]:
    print(f"Given word i.e. {string} is a Palindrome.")
else:
    print(f"Given word i.e. {string} is not a Palindrome.")

# End

""" 7) Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
 Write one line of Python that takes this list a and makes 
 a new list that has only the even elements of this list in it."""

elements = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_Elements = [i for i in elements if i % 2 == 0]

print(even_Elements)
# End

""" 8) Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player A: "))
    player_b = str(input("Player B: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('Player A wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('Game Over.')
            break
    elif dif in [-2, 1]:
        print('Player B wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('Game Over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
        break



