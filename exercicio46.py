'''Crie uma classe Car com atributos make, model e year.
Adicione um método display_info(), que exibe informações sobre o carro.
Em seguida, crie um objeto dessa classe e chame o método display_info().'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

#  objeto da classe Car
my_car = Car("Toyota", "Camry", 2020)


my_car.display_info()

'''Crie uma classe Library com um atributo books, que representa uma lista de livros.
Adicione métodos add_book(book) para adicionar um livro à biblioteca
e display_books() para exibir a lista de todos os livros.
Crie um objeto da classe Library, adicione alguns livros e exiba a lista de livros usando os métodos do objeto.
'''
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            print(book)

# Criação de um objeto da classe Library
library = Library()
# Adição de alguns livros
library.add_book("War and Peace")
library.add_book("1984")
library.add_book("The Great Gatsby")
# Exibição da lista de todos os livros
library.display_books()

'''Crie uma classe Rectangle com um construtor que aceita os parâmetros width e height.

Adicione o método area(), que retorna a área do retângulo.
Crie um objeto desta classe e calcule sua área.'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Criação de um objeto da classe Rectangle
rect = Rectangle(5, 10)

# Cálculo da área do retângulo
print(rect.area())

'''Crie uma classe BankAccount com um construtor que aceita os parâmetros account_number e initial_balance.
Adicione o método deposit(amount), que credita a conta, e o método withdraw(amount), que debita a conta.
Crie um objeto dessa classe e realize algumas operações de depósito e saque.'''
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and not exceed the current balance.")

# Criação da conta e operações
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(300)
account.withdraw(700)
account.withdraw(1000)