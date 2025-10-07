
'''
Escreva um programa que crie vários objetos de diferentes tipos e
use as funções id(), hash() e dir() para realizar as seguintes operações:
Determine e exiba identificadores únicos de objetos usando id().
Exiba valores de hash de objetos que podem ser hashados usando hash().
Exiba uma lista de atributos e métodos do objeto usando dir().
'''

int_obj = 42
str_obj = "hello"
list_obj = [1, 2, 3]
tuple_obj = (4, 5, 6)
set_obj = {7, 8, 9}
dict_obj = {'a': 1, 'b': 2}


print("Identificadores unicos:")
print(f"id(int_obj): {id(int_obj)}")
print(f"id(str_obj): {id(str_obj)}")
print(f"id(list_obj): {id(list_obj)}")
print(f"id(tuple_obj): {id(tuple_obj)}")
print(f"id(set_obj): {id(set_obj)}")
print(f"id(dict_obj): {id(dict_obj)}")


print("\nValores de Hash:")
print(f"hash(int_obj): {hash(int_obj)}")
print(f"hash(str_obj): {hash(str_obj)}")
print(f"hash(tuple_obj): {hash(tuple_obj)}")

print("\nAtributos e Metodos:")
print(f"dir(int_obj): {dir(int_obj)}")
print(f"dir(str_obj): {dir(str_obj)}")
print(f"dir(list_obj): {dir(list_obj)}")
print(f"dir(tuple_obj): {dir(tuple_obj)}")
print(f"dir(set_obj): {dir(set_obj)}")
print(f"dir(dict_obj): {dir(dict_obj)}")

'''
Escreva um programa que utilize as funções zip(), min(), max() e sum() para trabalhar com coleções de dados:
Unir duas listas em uma lista de tuplas usando zip().
Encontrar o menor e o maior elemento em uma lista de números usando min() e max().
Calcular a soma de todos os elementos em uma lista de números usando sum()
'''
# Duas listas para unir
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# União das listas em uma lista de tuplas
zipped_list = list(zip(list1, list2))
print("Lista unida:", zipped_list)

# Lista de números para encontrar min, max e sum
numbers = [10, 20, 30, 40, 50]

# Encontrar o menor e o maior elemento
min_element = min(numbers)
max_element = max(numbers)
print("Menor elemento:", min_element)
print("Maior elemento:", max_element)

# Calcular a soma de todos os elementos
sum_elements = sum(numbers)
print("Soma de todos os elementos:", sum_elements)