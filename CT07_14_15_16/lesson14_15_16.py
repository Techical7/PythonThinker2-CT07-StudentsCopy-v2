# print("Hello from lesson 14_15_16")

def is_valid_plate(plate):
    # First, make sure the plate is in the correct format
    import re
    match = re.fullmatch(r'([A-Z]{2,3})(\d{1,4})([A-Z])', plate)
    if not match:
        return False  # Doesn't match expected structure

    letters_part, number_part, final_letter = match.groups()

    # Take the last two letters before the numbers
    two_letters = letters_part[-2:]

    # Convert those letters to numbers: A=1, B=2, ..., Z=26
    letter_values = [ord(char) - ord('A') + 1 for char in two_letters]

    # Pad the number with zeros in front if it's less than 4 digits
    full_number = number_part.zfill(4)
    number_digits = [int(digit) for digit in full_number]

    # Combine everything to apply the weights
    values_to_multiply = letter_values + number_digits
    weights = [9, 4, 5, 4, 3, 2]

    # Multiply each value by its corresponding weight and add them up
    total = sum(value * weight for value, weight in zip(values_to_multiply, weights))

    # Get the remainder when the total is divided by 19
    remainder = total % 19

    # Use the remainder to find the expected checksum letter
    checksum_lookup = [
        'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M',
        'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'
    ]
    expected_letter = checksum_lookup[remainder]

    # Check if it matches the final letter in the plate
    return expected_letter == final_letter

# Ask the user for a registration plate to check
plate = input("Registration Plate: ").strip().upper()

# Check if it's valid and print the result
if is_valid_plate(plate):
    print("Output: Valid")
else:
    print("Output: Invalid")
