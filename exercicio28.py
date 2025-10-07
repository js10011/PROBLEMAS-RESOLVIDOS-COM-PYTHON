
'''Escreva um programa que tenha uma variável global counter, igual a 0.

Escreva uma função increment_counter(), que aumenta o valor dessa variável em 1 toda vez que é chamada.

Em seguida, chame essa função várias vezes e exiba o valor da variável global counter.'''

counter = 0

def increment_counter():
    global counter
    counter += 1

# Chamaremos a função várias vezes
increment_counter()
increment_counter()
increment_counter()

# Exibição do valor da variável global counter
print(counter)

'''Escreva um programa que tenha uma função aninhada.

A função externa outer_function() deve declarar uma variável x e atribuir a ela o valor 10.
A função interna inner_function() deve aumentar o valor da variável x em 5, utilizando o operador nonlocal.
Em seguida, chame a função interna e exiba o valor da variável x na função externa.'''

def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
    
    inner_function()
    print(x)

outer_function()

'''Escreva uma função sum_numbers(*args: int) -> int, que aceita uma quantidade arbitrária de números inteiros como argumentos e retorna a soma deles.
Então, escreva um programa que chama essa função com diferentes conjuntos de argumentos e exibe o resultado.'''
def sum_numbers(*args: int) -> int:
    return sum(args)

# Exemplos de chamada da função com diferentes conjuntos de argumentos
print(sum_numbers(1, 2, 3))           # 6
print(sum_numbers(10, 20, 30, 40))    # 100
print(sum_numbers(5))                 # 5
print(sum_numbers())                  # 0
print(sum_numbers(-1, -2, -3, -4))    # -10
print(sum_numbers(100, 200, -300))    # 0

'''Escreva uma função create_cat_profile(name: str, age: int, **kwargs: str) -> None, que aceita o nome e a idade do gato como parâmetros obrigatórios,
bem como um número arbitrário de parâmetros nomeados (por exemplo, raça, cor, etc.).
A função deve exibir o perfil do gato, incluindo todos os parâmetros passados.'''
def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    profile = {
        "Nome": name,
        "Idade": age
    }
    profile.update(kwargs)
    
    for key, value in profile.items():
        print(f"{key}: {value}")

# Exemplo de uso da função
create_cat_profile("Murzick", 3, raça="Siamês", cor="Preto")
create_cat_profile("Caramelo", 5, país="Brasil", hobby="brincar o dia todo")