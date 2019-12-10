numbers = [1, 3, 45, 23, 5, 4, 6, 45, 50, 80, 80, 1, 3, 100, 45, 1, 12, 0, 100, 4, 4, 4]
number_copy = 0
numbers.sort()
duplicated_numbers_index = []
for number in numbers:

    for j in range(len(numbers)):

        if number == numbers[j]:

            number_copy += 1
            if number_copy > 1:

                duplicated_numbers_index.append(j)

    for i in duplicated_numbers_index:

        numbers.remove(numbers[i])

    duplicated_numbers_index.clear()
    number_copy = 0

print(numbers)