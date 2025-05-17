# print("Hello from lesson 14_15_16")

def is_valid_plate(plate):
    import re

    # Check if the plate even looks right
    match = re.fullmatch(r'([A-Z]{2,3})(\d{1,4})([A-Z])', plate)
    if not match:
        return False  # If it doesn't match the basic shape, it's definitely wrong

    letters_before_numbers, number_part, last_letter = match.groups()

    # Grab the last two letters before the numbers
    last_two_letters = letters_before_numbers[-2:]

    # Turn those letters into numbers (A=1, B=2, ..., Z=26)
    letter_numbers = []
    for letter in last_two_letters:
        number = ord(letter) - ord('A') + 1
        letter_numbers.append(number)

    # Make sure the number part is exactly 4 digits by padding zeros at the front if needed
    number_part = number_part.zfill(4)

    # Break the number into individual digits
    digits = [int(d) for d in number_part]

    # Now, we have 6 numbers: 2 from letters and 4 from digits
    # Multiply each with the special weights
    weights = [9, 4, 5, 4, 3, 2]
    total = 0
    for value, weight in zip(letter_numbers + digits, weights):
        total += value * weight

    # After all that math, divide the total by 19 and get the remainder
    remainder = total % 19

    # Here's the magic table for the checksum
    checksum_table = [
        'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M',
        'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'
    ]

    # Find the expected letter
    expected_letter = checksum_table[remainder]

    # Check if what we expect matches the last letter
    return expected_letter == last_letter

# Let's ask the user nicely
plate = input("Please enter your car registration plate: ").strip().upper()

#Tell them clearly whether it's valid or not
if is_valid_plate(plate):
    print("Output: Valid")
else:
    print("Output: Invalid")

import pygame
 # initialize pygame
pygame.init()

# Set window size 