numbers = [1, 3, 45, 23, 5, 4, 6, 45, 50, 80, 80, 1, 3, 100, 45, 1, 12, 0, 100, 4, 4, 4]
uniques = []
numbers.sort()
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(numbers)
print(uniques)