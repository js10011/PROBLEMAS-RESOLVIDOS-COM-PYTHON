
'''Escreva uma função generate_random_number() que exiba na tela um número aleatório de -200 a 0.'''
import random

def generate_random_number():
    print(random.randint(-200, 0))

generate_random_number()

'''Escreva uma função print_random(a,b,c) que exiba na tela um argumento passado escolhido aleatoriamente.'''
import random

def print_random(a, b, c):
    print(random.choice([a, b, c]))

# Exemplo de chamada da função
print_random(1, 2, 3)

'''Escreva uma função find_max(a, b) que receba dois números como argumentos e retorne o maior deles.
Se os números forem iguais, a função deve retornar qualquer um deles.
Em seguida, escreva um programa que solicite ao usuário dois números, chame essa função e imprima o resultado.'''
def find_max(a, b):
    return a if a >= b else b

# Programa principal
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

max_number = find_max(num1, num2)
print("O maior número é:", max_number)

'''Escreva uma função factorial(n), que recebe um número inteiro n e retorna seu fatorial. Se n for igual a 0, a função deve retornar 1.
O fatorial de um número n é denotado por n! e é o produto de todos os números de 1 até n.
'''
def factorial(n=5):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial())  

'''Escreva uma função calculate_total_cost(price, tax=0.2) que recebe o preço de um produto e um parâmetro opcional de taxa (por padrão 20%).

A função deve calcular e imprimir o custo total do produto considerando o imposto.

Em seguida, escreva um programa que chama essa função com diferentes parâmetros.'''

def calculate_total_cost(price, tax=0.2):
    total_cost = price * (1 + tax)
    print(f"Custo total do produto com imposto: {total_cost:.2f}")

# Exemplos de chamada da função com diferentes parâmetros
calculate_total_cost(100)  # Usando a taxa padrão
calculate_total_cost(100, 0.1)  # Com taxa personalizada de 10%
calculate_total_cost(200, 0.15)  # Com taxa personalizada de 15%
calculate_total_cost(50)  # Usando a taxa padrão


'''Escreva uma função create_cat_profile(name, age, breed="Desconhecido"), que aceita nome, idade e um parâmetro opcional "raça" (por padrão "Desconhecido").
A função deve exibir o perfil do gato no formato "Nome: [name], Idade: [age], Raça: [breed]".
Em seguida, escreva um programa que chama essa função com diferentes parâmetros.'''

def create_cat_profile(name, age, breed="Desconhecido"):
    print(f"Nome: {name}, Idade: {age}, Raça: {breed}")

# Exemplos de chamada da função com diferentes parâmetros
create_cat_profile("Boris", 3, "Siamês")
create_cat_profile("Murray", 5)
create_cat_profile("Vasco", 2, "Persa")