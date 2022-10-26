"""Convert binary number to decimal number."""


number_as_string = input("Enter a binary number:")  # Takes input in binary
numbers = [int(x) for x in str(number_as_string)]  # Creates list from binary input
numbers.reverse()  # Reverses the list

# Gives error if non-binary characters were inserted
for number in numbers:
    if number != 1 and number != 0:
        print("Error! You inserted non-binary characters.")
        exit()

exponent = 0
total = 0
# Calculates the binary number to decimal
for number in numbers:
    if number == 1:
        total += 1 * 2 ** exponent
    exponent += 1

print(number_as_string, "in binary is equal to", total, "in decimal.")
