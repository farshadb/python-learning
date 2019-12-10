matrix = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numbers = [1, 34, 56, 2, 4, 5]
print(matrix)
print(matrix[2][0])
matrix.append(6)
print(matrix)
matrix.insert([0][0], 5)
print(matrix)
print(numbers.pop(5))
print(numbers)
numbers.append(12)
print(numbers)
numbers.sort()
print(numbers)
numbers.insert(1, 3)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)
numbers = [1, 2, 4, 12, 34, 56, 1, 4]
numbers.pop(0)
print(numbers)
print(numbers.index(56))
print(50 in numbers)
print(numbers.count(4))
print(numbers.index(1))
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
