# importing the required modules
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
