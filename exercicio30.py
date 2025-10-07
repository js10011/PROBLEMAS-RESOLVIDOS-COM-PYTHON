
'''Escreva um programa que cria uma lista de elementos aleatórios, exibe o comprimento da lista e, em seguida, o primeiro e o último elemento da lista.'''
import random

# Criamos uma lista de elementos aleatórios
random_list = [random.randint(0, 100) for _ in range(random.randint(5, 15))]

# Exibimos o comprimento da lista
print("Comprimento da lista:", len(random_list))

# Exibimos o primeiro elemento da lista
print("Primeiro elemento da lista:", random_list[0])

# Exibimos o último elemento da lista
print("Último elemento da lista:", random_list[-1])



'''Escreva um programa que crie uma lista de 5 elementos solicitados ao usuário.
O programa deve imprimir a lista, depois solicitar ao usuário o índice de um elemento e exibir o valor do elemento nesse índice'''
# Criamos uma lista vazia
elements = []

# Solicitamos ao usuário 5 elementos e os adicionamos à lista
for _ in range(5):
    element = input("Digite um elemento: ")
    elements.append(element)

# Exibimos a lista resultante
print("Lista de elementos:", elements)

# Solicitamos ao usuário o índice do elemento
index = int(input("Digite o índice do elemento: "))

# Exibimos o valor do elemento no índice especificado
print("Valor do elemento no índice", index, ":", elements[index])


'''Escreva um programa que cria uma lista de 10 elementos.
O programa pede ao usuário para inserir uma string e depois verifica se ela está na lista ou não.'''

# Criamos uma lista de 10 elementos
elements = ["apple", "banana", "orange", "grape", "mango", "cherry", "peach", "plum", "kiwi", "melon"]

# Pedimos ao usuário para inserir uma string
user_input = input("Digite uma string: ")

# Verificamos se a string está na lista
if user_input in elements:
    print("String encontrada na lista!")
else:
    print("String não encontrada na lista.")