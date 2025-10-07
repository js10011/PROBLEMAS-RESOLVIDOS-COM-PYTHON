'''Crie uma classe base Vehicle, que terá os atributos brand e model.
Em seguida, crie uma classe filha Car, que herdará de Vehicle e adicionará o atributo fuel_type.
Use o método super() para chamar o construtor da classe base.'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type


car = Car("Toyota", "Corolla", "Petrol")
print(f"Brand: {car.brand}, Model: {car.model}, Fuel Type: {car.fuel_type}")

'''Crie uma classe base Animal com um método speak que retorna a string "Rrrr!".
Depois, crie uma classe filha Dog, que irá herdar de Animal e sobrescrever o método speak,
adicionando ao comportamento da classe pai seu próprio comportamento usando o método super().'''

class Animal:
    def speak(self):
        return "Rrrr!"

class Dog(Animal):
    def speak(self):
        return super().speak() + " Au-au!"

# Exemplo de uso:
dog = Dog()
print(dog.speak())  # Saída: Rrrr! Au-au!