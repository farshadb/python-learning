digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

phone = input("Enter your phone number: ")
out_put_string = ''
for digit in phone:
    out_put_string += " " + digits_mapping.get(digit, "!")
print(out_put_string)
