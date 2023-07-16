"""  see your mistakes
numbers = [2, 4, 7, 3, 9, 0, 5, 15]
for i in numbers:
    print(numbers)"""
"""numbers = [2, 4, 7, 3, 9, 0, 5, 15]
for i in numbers:
    print(numbers[i])"""
#answer
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
