# print("Hello from lesson 14_15_16")

def is_valid_plate(plate):

    import re
    match = re.fullmatch(r'([A-Z]{2,3})(\d{1,4})([A-Z])', plate)
    if not match:
        return False

    letters_part, number_part, final_letter = match.groups()

    two_letters = letters_part[-2:]

    letter_values = [ord(char) - ord('A') + 1 for char in two_letters]

    full_number = number_part.zfill(4)
    number_digits = [int(digit) for digit in full_number]

    values_to_multiply = letter_values + number_digits
    weights = [9, 4, 5, 4, 3, 2]

    total = sum(value * weight for value, weight in zip(values_to_multiply, weights))

    remainder = total % 19

    checksum_lookup = [
        'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M',
        'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'
    ]
    expected_letter = checksum_lookup[remainder]

    return expected_letter == final_letter

plate = input("Registration Plate: ").strip().upper()

if is_valid_plate(plate):
    print("Output: Valid")
else:
    print("Output: Invalid")
