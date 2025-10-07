"""Escreva um programa que recebe um número arbitrário de números e imprime sua soma.
O programa deve:
Definir a função sum_numbers(*args), que aceita um número arbitrário de números.
Calcular a soma de todos os números passados."""

def sum_numbers(*args):
    return sum(args)

# Exemplo de uso:
numbers = [1, 2, 3, 4, 5]
print(sum_numbers(*numbers))  # Saída: 15

# Você também pode passar os números diretamente:
print(sum_numbers(1, 2, 3, 4, 5))

'''Escreva um programa que aceite uma quantidade arbitrária de argumentos nomeados e exiba informações sobre uma pessoa.

O programa deve:

Definir a função print_person_info(**kwargs), que aceita uma quantidade arbitrária de argumentos nomeados.

Exibir cada nome de argumento e seu valor.'''

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="John", age=30, city="New York", profession="Engineer")
