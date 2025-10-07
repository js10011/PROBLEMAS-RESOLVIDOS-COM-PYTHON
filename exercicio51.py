
'''Escreva uma função check_type para verificar se o objeto passado é uma instância da classe Animal ou de suas subclasses.
Use a função isinstance() para realizar a verificação.
Em seguida, crie as classes Animal, Dog, Cat e verifique alguns objetos.'''
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_type(obj):
    return isinstance(obj, Animal)

# Exemplos de uso:
dog = Dog()
cat = Cat()
not_animal = "Not an animal"

print(check_type(dog))  # True
print(check_type(cat))  # True
print(check_type(not_animal))  # False

'''Escreva uma função check_subclass para verificar se uma classe é uma subclasse de outra.

Use a função issubclass() para realizar a verificação.

Em seguida, crie as classes Vehicle, Car, Bicycle e verifique se Car e Bicycle são subclasses de Vehicle.'''
def check_subclass(class1, class2):
    return issubclass(class1, class2)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

# Verificação
print(check_subclass(Car, Vehicle))  # Deve retornar True
print(check_subclass(Bicycle, Vehicle))