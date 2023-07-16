#upper or lower is specific to a string, so it is referred a method.
#but len and print are general purpose functions
course = 'Python for Beginners'
print(len(course))
print(course.upper())#does not change the original string.
print(course)
print(course.lower())
print(course.find('P'))
print(course.find('o')) #finds the first o in the string
print(course.find('0')) #we get -1 coz there is no zero.
print(course.find('Beginners'))
print(course.replace('Beginners','Absolute Beginners')) #if we write beginners instead, there will be no change
print(course.replace('P','J'))
#existence of a string
print('Python' in course) # with 'python', it returns false



