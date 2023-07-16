numbers = [5 ,2, 1, 7, 4]
numbers.append(20)#this method adds an item at the end of the list
numbers.insert(2, 10)#add an item to the index written
numbers.remove(5)
numbers.clear() #this method/function doesnt take any value,it empties the list
print(numbers)
numbers = [5 ,2, 1, 5, 7, 4]
numbers.pop()#removes the last item of a list
print(numbers.index(1)) #shows the index of an item if the item exists
#numbers.index(50) #generates an error
print(50 in numbers)#returns a boolean value instead of an error
print(numbers)
print(numbers.count(5))
print(numbers.sort())#this returns none(doenst return a value, but sorts the list), representing the absence of an item
numbers.sort()
print(numbers)
numbers.reverse() # sorts in descending order
print(numbers)
numbers2 = numbers.copy()# any changes in the numbers list wont affect 2nd list
numbers.append(10)
print(numbers2)