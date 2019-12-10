numbers = [2, 6, 8, 9, 12, 3, 100, 45, 50, 1, 0, 120, 1000, -2]
min_number = 0
max_number = 0
for index in numbers:
    if index > max_number:
        max_number = index
    if index < min_number:
        min_number = index
print(f'maximum: {max_number}')
print(f'minimum: {min_number}')
