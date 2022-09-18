import random
moves = ["rock","scissor","paper"]
keep_playing = 3
while keep_playing!=0:
    cmove = random.choice(moves)
    print("The computer choses:",cmove)
    user = input("Your chance:")
    if cmove==user:
        print("Tie")
    elif cmove == "rock" and user=="paper":
        print("You won!!")
    elif cmove == "paper" and user=="rock":
        print("Pooor!!!")
    elif cmove == "scissor" and user=="rock":
        print("YAAAAYYYYYY")
    elif cmove == "rock" and user=="scissor":
        print("OHHHNOOO")
    elif cmove=="paper" and user=="scissor":
        print("Yipeeeee!!!")
    else:
        print("Better luck next time....")
