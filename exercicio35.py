'''
Escreva um programa que cria vários objetos do tipo frozenset a partir de diferentes objetos iteráveis (lista, string).
O programa deve:
Criar um frozenset a partir de uma lista.
Criar um frozenset a partir de uma string.
Realizar a união, interseção, diferença e diferença simétrica de dois conjuntos frozenset.
'''
# Criamos frozenset a partir de uma lista
list_frozen = frozenset([1, 2, 3, 4, 5])

# Criamos frozenset a partir de uma string
string_frozen = frozenset("abcde")

# União
union_result = list_frozen | string_frozen

# Interseção
intersection_result = list_frozen & string_frozen

# Diferença
difference_result = list_frozen - string_frozen

# Diferença simétrica
symmetric_difference_result = list_frozen ^ string_frozen

# Exibir resultados
print(f"União: {union_result}")
print(f"Interseção: {intersection_result}")
print(f"Diferença: {difference_result}")
print(f"Diferença simétrica: {symmetric_difference_result}")

'''
Escreva um programa que cria vários objetos do tipo frozenset e os usa como chaves em um dicionário.
O programa deve:
Criar dois frozenset a partir de listas.
Criar um dicionário, onde as chaves são frozenset, e os valores são strings.
'''
# Criamos dois frozenset a partir de listas
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([4, 5, 6])
# Criamos um dicionário, onde as chaves são frozenset e os valores são strings
dictionary = {
    frozenset1: "Primeiro conjunto de números",
    frozenset2: "Segundo conjunto de números"
}
# Exibimos o dicionário
print(dictionary)

