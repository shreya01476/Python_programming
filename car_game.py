command=""
while command!="quit":
    command=input(">:").lower()
    if command == "start":
        print("The car has been started")
        break
    elif command=="stop":
        print("The car has been stopped")
    elif command =="help":
        print("""
         start - insert and rotate a key and leave the clutch slowly
         stop - push a clutch and put a break
         """)
    else:
        print("Sorry!!! I can't understand what you are trying to say")
