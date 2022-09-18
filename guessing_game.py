import math
import random
secret_number=22
guess_count = 0
guess_limit = 3
while guess_count<=guess_limit:
    guessing_number=int(input("Enter the number:"))
    guess_count+=1
    if guessing_number==secret_number:
        print("Yaay!You Won")
        break
    elif guessing_number < secret_number:
        print("A Big No!!!")
    elif guessing_number > secret_number:
        print("Tooooo Bigg!!")
    else:
        print("Better luck next time")

