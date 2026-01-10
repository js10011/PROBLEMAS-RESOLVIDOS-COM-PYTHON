
'''Escreva uma classe Person, que represente uma pessoa com os atributos name e age.
Implemente a sobrecarga dos operadores de comparação == e < para comparar pessoas pela idade.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return False


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1 == person2)  # False
print(person1 == person3)  # True
print(person1 < person2)   # False
print(person2 < person1)   # True

'''Escreva uma classe Matrix que representará uma matriz bidimensional e suportará a sobrecarga de operadores de indexação ([]).
Implemente os métodos __getitem__ e __setitem__.'''
class Matrix:
    def __init__(self, rows, cols, fill_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill_value for _ in range(cols)] for _ in range(rows)]
    
    def __getitem__(self, indices):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        return self.data[row][col]
    
    def __setitem__(self, indices, value):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        self.data[row][col] = value


matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Saída: 1