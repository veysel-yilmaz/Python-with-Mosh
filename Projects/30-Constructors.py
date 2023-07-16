class Point: #every method in our class should have self parameter
    def __init__(self, x, y): #this method is a constructor, to create/construct an object
        #short for initialise, it is the function/method called when creating a new point object
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 11 # x can be updated here
print(point.x)
print(point.y)


