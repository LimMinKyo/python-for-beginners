"""
from random import randint

user_choice = int(input("Choose number.\n"))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)
"""

distance = 0

while distance < 20:
    distance += 1
    print("I'm running:", distance, "km")
