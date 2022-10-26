import math

def print_hello():
    # Prints Hello
    print("Hello")
def get_hello():
    #Returns Hello
    return "Hello"
def ask_name_and_greet_user():
    '''Takes name as input and prints greetings with the name'''
    name = input("Enter your name: ").capitalize()
    if name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name}. Would you like to have a Hamburger?")
def calculate_hypotenuse_length(cathet1, cathet2):
    # Calculates hypotenuse from cathets
    hypotenuse = math.sqrt((cathet1 ** 2) + (cathet2 ** 2))
    return hypotenuse
def calculate_cathetus_length(cathet, hypotenuse):
    # Calculates cathet a from hypotenuse and cathet b
    cathet_a = math.sqrt((hypotenuse ** 2) - (cathet ** 2))
    return  cathet_a

print_hello()
ask_name_and_greet_user()
print(calculate_hypotenuse_length(15, 20))
print(calculate_cathetus_length(20, 25))