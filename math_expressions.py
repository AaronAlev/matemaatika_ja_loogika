"""Practice different math expressions and calculations."""
import math

# declare num_a and num_b
num_a = 10
num_b = 5
radius = 7
side_length = 5


# Sum and difference
sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

print("______________________________________________")

# Float division
division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")

print("______________________________________________")

# Integer division
division = num_a // num_b
print(f"{num_a} / {num_b} = {division}")

print("______________________________________________")

# Powerful operations
multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")
power = num_a ** num_b
print(f"{num_a} ** {num_b} = {power}")
remainder = num_a % num_b
print(f"{num_a} % {num_b} = {remainder}")

print("______________________________________________")

# Find average
average = (num_a + num_b) / 2
print(f"The average of {num_a} and {num_b} is {average}")

print("______________________________________________")

# Area of a circle
circle_area = round(math.pi * (radius ** 2), 2)
print(f"Area of a circle with a radius of {radius} units is {circle_area} units squared")

print("______________________________________________")

# Area of an equilateral triangle

triangle_area = round((math.sqrt(3) / 4) * (side_length ** 2))
print(f"Area of a triangle with a side length of {side_length} units is about {triangle_area} units squared")

print("______________________________________________")

# Calculate discriminant
a = 2
b = 3
c = 4

discriminant = (b ** 2) - (4 * a * c)
print(f"Discriminant of {a}, {b} and {c} is {discriminant}")

print("______________________________________________")

# Calculate hypotenuse length

a = 5
b = 7
c = round(math.sqrt((a ** 2) + (b ** 2)), 5)
print(f"Hypotenuse length with cathetus lengths of {a} and {b} is {c}")

print("______________________________________________")

# Calculate cathetus length

a = 4
c = 18
b = round(math.sqrt((c ** 2) - (a ** 2)), 5)
print(f"{b}")

print("______________________________________________")

# Time converter

seconds = 35782
minutes = seconds // 60
seconds_left = seconds % 60
hours = (minutes // 60)
minutes_left = minutes % 60
print(f"{seconds} seconds is equal to {minutes} minutes with {seconds_left} seconds left or {hours} hours with {minutes_left} minutes left ")

print("______________________________________________")

# Student helper

angle = 74
sine = round(math.sin(angle), 10)
cosine = round(math.cos(angle), 10)
print(f"sine of {angle}° is {sine} and the cosine of {angle}° is {cosine}")

print("______________________________________________")

# Greetings

n = 5
lots_of_heys = n * "Hey"
print(f"{n} times Hey is {lots_of_heys}")

print("______________________________________________")

# Adding numbers

num_a = 8
num_b = 3
string_numbers = str(num_a) + str(num_b)
print(f"'{num_a}' + '{num_b}' is equal to '{string_numbers}'")