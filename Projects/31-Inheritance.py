"""
class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self): #this repetition is against dry(dont repeat yourself)
        print("walk")
"""
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): #Dog and Cat classes inherit methods from Mammal class
    #pass # pass is used to make python happy. no empty class is allowed
    def bark(self):
        print("bark")


class Cat(Mammal):
    #pass
      def be_annoying(self):
          print("annoying")



dog1 = Dog() #dog object
dog1.walk()

cat1 = Cat()
cat1.be_annoying()