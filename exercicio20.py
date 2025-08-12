'''
Crie uma classe chamada Restaurant. O método __init__()
 de Restaurant deve armazenar dois atributos: restaurant_name e
 cuisine_type. Crie um método chamado describe_restaurant() que mostre
 essas duas informações, e um método de nome open_restaurant() que exiba
 uma mensagem informando que o restaurante está aberto.
 Crie uma instância chamada restaurant a partir de sua classe. Mostre os
 dois atributos individualmente e, em seguida, chame os dois métodos.
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Tipo de cozinha: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name} está agora aberto!")

# instância 
restaurant = Restaurant("Mix de Sabor", "Brasileira")

# Mostrando os atributos individualmente
#print("Nome do restaurante:", restaurant.restaurant_name)
#print("Tipo de cozinha:", restaurant.cuisine_type)

# Chamando os métodos
restaurant.describe_restaurant()
restaurant.open_restaurant()


'''
Comece com a classe do Exercício 9.1. Crie três
 instâncias diferentes da classe e chame describe_restaurant() para cada
 instância.,
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Tipo de cozinha: {self.cuisine_type}")
        print("-" * 30)

# Criando três instâncias diferentes
restaurante1 = Restaurant("Cantina do Sabor", "Italiana")
restaurante2 = Restaurant("Sabor Oriental", "Japonesa")
restaurante3 = Restaurant("Delícias do Brasil", "Brasileira")

# Chamando describe_restaurant() para cada instância
restaurante1.describe_restaurant()
restaurante2.describe_restaurant()
restaurante3.describe_restaurant()

'''
Crie uma classe chamada User. Crie dois atributos de nomes
 first_name e last_name e, então, crie vários outros atributos normalmente
 armazenados em um perfil de usuário. Escreva um método de nome
 describe_user() que apresente um resumo das informações do usuário. Escreva
 outro método chamado greet_user() que mostre uma saudação personalizada
 ao usuário.
'''
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("\n--- Informacoes do Usuario ---")
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Idade: {self.age}")
        print(f"E-mail: {self.email}")
        print(f"Localizacao: {self.location}")

    def greet_user(self):
        print(f"\nOla, {self.first_name}! Seja bem-vindo(a)!")


usuario1 = User("Carlos", "Silva", 30, "carlos.silva@email.com", "Sao Paulo")
usuario1.describe_user()
usuario1.greet_user()

usuario2 = User("Paula", "Oliveira", 32, "pa34.silva@email.com", "Belo Horizonte")
usuario2.describe_user()
usuario2.greet_user()
