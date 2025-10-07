
'''
Escreva um programa que cria dois conjuntos a partir de elementos solicitados ao usuário.
O programa deve unir esses conjuntos usando o método union() e encontrar a interseção deles usando o método intersection().
O programa deve exibir ambos os resultados.
'''
# Solicitando ao usuário os elementos para o primeiro conjunto
set1 = set(map(int, input("Digite os elementos do primeiro conjunto separados por espaço: ").split()))

# Solicitando ao usuário os elementos para o segundo conjunto
set2 = set(map(int, input("Digite os elementos do segundo conjunto separados por espaço: ").split()))

# União dos conjuntos
union_set = set1.union(set2)
print("União dos conjuntos:", union_set)

# Interseção dos conjuntos
intersection_set = set1.intersection(set2)
print("Interseção dos conjuntos:", intersection_set)


'''
Escreva um programa que crie dois conjuntos, cada um com 10 números aleatórios.
O primeiro conjunto contém números aleatórios no intervalo de 1 a 20, e o segundo conjunto contém números aleatórios no intervalo de 10 a 30.
O programa deve encontrar a diferença do primeiro conjunto com o segundo usando o método difference().
E a diferença simétrica usando o método symmetric_difference().
O programa deve exibir ambos os resultados
'''
import random

# Criando dois conjuntos de números aleatórios
set1 = set(random.randint(1, 20) for _ in range(10))
set2 = set(random.randint(10, 30) for _ in range(10))

# Encontrando a diferença do primeiro conjunto com o segundo
difference = set1.difference(set2)

# Encontrando a diferença simétrica
symmetric_difference = set1.symmetric_difference(set2)

# Exibindo os resultados
print("Primeiro conjunto:", set1)
print("Segundo conjunto:", set2)
print("Diferença do primeiro conjunto com o segundo:", difference)
print("Diferença simétrica:", symmetric_difference)