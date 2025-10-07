
'''
Escreva um programa que use uma lambda função para ordenar uma lista de strings pelo seu comprimento
usando a função sorted(). O programa deve:
Criar uma lista de strings.
Usar sorted() e uma lambda função para ordenar as strings pelo comprimento.
'''
# Criamos uma lista de strings
strings = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Usamos sorted() e uma lambda função para ordenar as strings pelo comprimento
sorted_strings = sorted(strings, key=lambda x: len(x))

# Exibimos o resultado
print(sorted_strings)

'''Escreva um programa que crie uma função-geradora de contador usando closures.
O programa deve:
Definir uma função externa make_counter(), que cria e retorna uma função interna counter().
A função interna counter() deve incrementar o valor do contador e retorná-lo.
Crie vários contadores independentes e chame-os várias vezes'''
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# Criação de contadores independentes
counter1 = make_counter()
counter2 = make_counter()

# Chamadas aos contadores e exibição do resultado na tela
print(counter1())  #
print(counter1())  
print(counter2())  
print(counter1())  
print(counter2()) 

'''Escreva um programa que cria uma função de filtro utilizando closures.

O programa deve:

Definir uma função externa make_filter(threshold) que cria e retorna uma função interna filter_func(value).
A função interna filter_func(value) deve retornar True se value for maior que threshold.
Criar várias funções de filtro com diferentes valores de limite e'''
def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func

# Criamos várias funções de filtro com diferentes valores de limite
filter_10 = make_filter(10)
filter_20 = make_filter(20)
filter_30 = make_filter(30)

# Lista de dados para filtrar
data = [5, 15, 25, 35, 45]

# Filtramos os dados e exibimos os resultados
print(list(filter(filter_10, data)))  # Deve exibir [15, 25, 35, 45]
print(list(filter(filter_20, data)))  # Deve exibir [25, 35, 45]
print(list(filter(filter_30, data)))  # Deve exibir [35, 45]