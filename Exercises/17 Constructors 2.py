class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
#print(john.name) it is removed after adding formatted string
john.talk()

bob = Person("Bob Smith") #another person object, bob is a new person
bob.talk()
#Each object is a different instance of a person class