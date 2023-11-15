class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def Animal_Details(self):
        print(self.name)
        print(self.sound)

class Dog(Animal):
    def __init__(self,name,sound,family):
        super().__init__(name,sound)
        self.family=family
    def Animal_Details(self):
        super().Animal_Details()
        print(self.family)

class Sheep(Animal):
    def __init__(self,name,sound,color):
        super().__init__(name,sound)
        self.color=color
    def Animal_Details(self):
        super().Animal_Details()
        print(self.color)
d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_Details()

s = Sheep("Billy", "Baa Baa", "White")
s.Animal_Details()