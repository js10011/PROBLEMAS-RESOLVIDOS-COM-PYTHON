'''
Escreva um programa que crie uma lista de 10 elementos solicitados ao usuário.

Em seguida, o programa deve criar um conjunto a partir dos elementos da lista para manter apenas os elementos únicos e exibir esse conjunto.

'''
elements = []
for _ in range(10):
    element = input("Digite um elemento: ")
    elements.append(element)

unique_elements = set(elements)
print(unique_elements)


'''
Escreva a função set_detector, que percorre a lista (tupla) de seus argumentos e determina - se há um conjunto entre eles ou não.
Chame a função set_detector com diferentes opções de parâmetros (com e sem conjunto).
'''

def set_detector(*args):
    for arg in args:
        if type(arg) == set:
            return True
    return False

print(set_detector(1, [2, 3], (4, 5), {6, 7}))  # Conjunto presente
print(set_detector(1, [2, 3], (4, 5)))  # Conjunto ausente
print(set_detector("hello", 10, {1, 2, 3}))  # Conjunto presente
print(set_detector("world", 42, 3.14))  # Conjunto ausente