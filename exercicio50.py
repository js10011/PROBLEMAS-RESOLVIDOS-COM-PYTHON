'''Crie uma classe base Shape com o método area, que irá retornar a área da figura.
Em seguida, crie classes filhas Circle e Rectangle, que irão sobrescrever o método area para calcular a área das suas figuras.'''

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)

'''Crie uma classe base Animal com o método make_sound, que retornará a string "Uuuuuuu!".
Em seguida, crie classes filhas Dog e Cat, que irão sobrescrever o método make_sound
e usar super() para chamar o método da classe pai.'''
class Animal:
    def make_sound(self):
        return "Uuuuuuu!"

class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " Au-au!"

class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " Miau-miau!"


dog = Dog()
cat = Cat()

print(dog.make_sound())  # Uuuuuuu! Au-au!
print(cat.make_sound())  # Uuuuuuu! Miau-miau!