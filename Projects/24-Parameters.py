def greet_user(name):
    print(f'Hi {name}!')
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user("John") # if we remove John, we get typeerror, argument is a value that we supply to a function
greet_user("Mary") # mary is an argument we pass to the name parameter!!!
print("Finish")
#parameters are the placeholders that we define in our function for receiving info
#arguments are actual info that we supply to these functionns.
