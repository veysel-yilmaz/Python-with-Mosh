# Classes are used to model new and real concepts
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#an object is an instance of a class
point1 = Point() #an object
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point() # a new object.
#print(point2.x) #it generates Attribute error
# because each object is a different instance of our point class
point2.x = 1
print(point2.x)
