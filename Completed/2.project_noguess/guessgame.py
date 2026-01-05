print("_____GUESS GAME_____")
import random
secret_number = random.randint(1, 100)
print(f"{secret_number}")
print("You have 3 attempts :")

for attempt in range(5) :
    code=int(input("Try Your Luck:"))
    print(f"Your {attempt + 1} st attempt")
    if code == secret_number :
        print ("You got it" )
        break
    elif code > secret_number :
        print("Wrong,Try Again - Try Lower")
    elif code < secret_number :
        print("Wrong,Try Again - Try Higher")
else:
    print("Out of luck")
    print(f"Answer is {secret_number}")
