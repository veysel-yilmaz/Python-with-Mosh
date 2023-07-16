try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
"""
age = int(input('Age: '))
    print(age)

#exit code 0 means there is no error(if we enter a numerical value)
#if we enter a string in the input, it will return valueerror
#but with a string it return exit code 1
"""