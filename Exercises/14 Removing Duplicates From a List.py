"""numbers = [5, 2, 1, 7, 4, 5]
for item in numbers:
    if item == item:
        numbers.remove(item)
    print(numbers)"""
#answer
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = [] #if an item is unique, then it is added this list
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

