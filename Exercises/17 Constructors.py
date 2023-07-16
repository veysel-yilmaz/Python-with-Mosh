"""Person object,
name attribute and talk method( talk())"""
class Person: # first letter should be in capital letter
    def __init__(self, name): #this is new method and called as constructor
        #name above is a parameter, and attribute
        self.name = name #right name is the argument passed to the method
#self references to the current object


    def talk(self):
        print("talk")
#above is the body of our person class


"""john = Person()
john.talk()"""
john = Person("John Smith")
print(john.name)
john.talk()