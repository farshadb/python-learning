numbers = [2, 6, 8, 9, 12, 3, 100, 45, 50, 1, 0, 120, 1000, -2]
min_number = 0
max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print(f'maximum: {max_number}')
print(f'minimum: {min_number}')
