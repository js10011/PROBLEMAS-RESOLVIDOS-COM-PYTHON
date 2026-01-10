'''Escreva 2 funções: def foo(bar=[]) e foo_correct(bar=None).

Cada função recebe uma lista e adiciona a ela o elemento "baz".

Se a lista não for fornecida, a função deve usar uma nova lista vazia.

Mostre como o uso de um objeto mutável como valor padrão pode levar a um comportamento inesperado, e corrija isso (na segunda função).'''
# Exemplo de função com objeto mutável como valor padrão
def foo(bar=[]):
    bar.append("baz")
    return bar

# Demonstração de comportamento inesperado
print(foo())  # Imprime: ['baz']
print(foo())  # Imprime: ['baz', 'baz']
print(foo())  # Imprime: ['baz', 'baz', 'baz']

# Função corrigida com None como valor padrão
def foo_correct(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

# Verificação da função corrigida
print(foo_correct())  # Imprime: ['baz']
print(foo_correct())  # Imprime: ['baz']
print(foo_correct())  # Imprime: ['baz']

# Verificação passando uma lista
lst = [1, 2, 3]
print(foo_correct(lst))  # Imprime: [1, 2, 3, "baz"]
print(foo_correct(lst))  # Imprime: [1, 2, 3, "baz", "baz"]

'''O exemplo apresenta um código que captura incorretamente múltiplos tipos de exceções simultaneamente.

Escreva abaixo a versão corrigida'''
# Variante incorreta: várias exceções são capturadas de forma errada
try:
    number = int(input("Digite um número: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Ocorreu um erro: insira apenas números diferentes de zero.")

# Variante corrigida: tratamento correto de exceções
try:
    number = int(input("Digite um número: "))
    result = 10 / number
except ValueError:
    print("Erro: insira um número válido.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é possível.")