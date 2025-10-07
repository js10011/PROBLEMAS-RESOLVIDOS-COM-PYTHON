
'''Escreva um programa que crie um gerador baseado em uma função para gerar números de Fibonacci.
O programa deve:
Definir a função fibonacci(), que usa a palavra-chave yield para gerar números de Fibonacci.'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(10):
    print(next(gen))

'''Escreva um programa que use uma expressão geradora para criar
uma sequência de quadrados de números de 1 a 10. O programa deve:
Criar uma expressão geradora para gerar quadrados de números.
Usar esse gerador para exibir todos os valores da sequência.'''

# Expressão geradora para quadrados de números de 1 a 10
squares = (x**2 for x in range(1, 11))

# Exibe todos os valores da sequência
for square in squares:
    print(square)

'''Escreva um programa que crie um decorador simples para logar chamadas de função.
O programa deve:
Definir o decorador log_decorator, que imprime uma mensagem antes e depois da chamada da função.
Aplicar o decorador à função greet(), que imprime uma mensagem de boas-vindas.
Chamar a função greet().'''

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função")
        result = func(*args, **kwargs)
        print("Depois de chamar a função")
        return result
    return wrapper

@log_decorator
def greet():
    print("Olá!")

greet()

'''Escreva um programa que crie um decorador para chamar uma função repetidamente um número específico de vezes.

O programa deve:

Definir o decorador repeat(num_times), que aceita o número de repetições como argumento.
Aplicar o decorador à função say_hello(name), que exibe uma mensagem de saudação.
Chamar a função say_hello(name).'''
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
