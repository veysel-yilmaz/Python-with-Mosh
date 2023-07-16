"""numbers = [5, 2, 5, 2, 2]
for x in range(numbers): # referred to 14-while loops
    print(x)"""
#answer:  (Couldnt get 'wow' from Mosh :(
"""numbers = [5, 2, 5, 2, 2]
for x_count in numbers #number of x in each line(x_count)
    print('x' * x_count)"""
#########
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)