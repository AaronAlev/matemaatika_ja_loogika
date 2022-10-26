import time
import random
def age_magic():
    yes_no = input("AGE MAGIC!!! Do you wanna play? (y/n) ")
    if yes_no == "y":
        print("Good >:)")
        time.sleep(1)
    else:
        print("Wrong answer >:[  We'll play anyway")
        time.sleep(1)

    print("Now let's begin")
    time.sleep(0.5)
    age = input("Insert your age: ")
    time.sleep(0.5)
    number = input("Insert a random number: ")

    print("Calculating...")
    time.sleep(3)
    print(f"Your age is {age} and the number you entered is {number}")
def pick_a_card():
    print("Think of a card")
    time.sleep(7)
    print("Got one?")
    print("I hope you did")
    time.sleep(1)
    print(f"Is it {random.randint(1, 10)} of hearts?")
pick_a_card()
