class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width
rect = Rectangle(4,5)
print(rect.area())
print(rect.perimeter())