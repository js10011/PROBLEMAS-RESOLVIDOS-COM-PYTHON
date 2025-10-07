
'''Crie uma classe Car que tenha um atributo público brand e um atributo protegido _model_.
Adicione métodos para obter e definir o valor do atributo protegido _model_.'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model_ = model

    def get_model(self):
        return self._model_

    def set_model(self, model):
        self._model_ = model

# Criação do objeto da classe Car
car = Car("Toyota", "Camry")
# Configurar novos valores para os atributos
car.brand = "Honda"
car.set_model("Civic")
# Exibir os valores dos atributos na tela
print(f"Brand: {car.brand}")
print(f"Model: {car.get_model()}")

'''Crie uma classe Library, que representará uma biblioteca de livros.

Adicione um método __str__, que retornará uma string com informações sobre a biblioteca, e um método __len__,

que retornará o número de livros na biblioteca.
Crie um objeto da classe Library, adicione alguns livros a ele e
exiba informações sobre a biblioteca e a quantidade de livros.'''
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Library with {len(self.books)} books: " + ", ".join(self.books)

    def __len__(self):
        return len(self.books)

# Criando um objeto da biblioteca
library = Library()

# Adicionando livros à biblioteca
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Exibindo informações sobre a biblioteca com a lista de livros e a quantidade de livros
print(library)
print(f"Number of books in library: {len(library)}")

'''Crie uma classe básica Vehicle, que terá o atributo brand.

Depois, crie duas classes filhas Car e Motorcycle, que herdarão de Vehicle

e adicionarão seus atributos e métodos únicos.
Por exemplo, a classe Car pode ter o método drive, e a classe Motorcycle — o método ride.'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} está dirigindo."

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        return f"{self.brand} {self.model} está andando."

# Exemplos de uso das classes:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla está dirigindo.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 está andando.

"""Crie uma classe base Shape, que terá um método area para calcular a área.
Em seguida, crie duas classes filhas Rectangle e Circle, que herdarão de Shape

e sobrescreverão o método area para calcular a área do retângulo e do círculo, respectivamente."""
import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

# Exemplo de uso
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")