"""def find_max() #this function should take a list of numbers, so we have parameter(numbers)
numbers = [10, 3, 6, 2]
max = number[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)"""
def find_max(numbers):
    maximum = numbers[0] #should be numbers, not number
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


