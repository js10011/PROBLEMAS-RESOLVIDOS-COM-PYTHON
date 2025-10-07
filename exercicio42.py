'''Escreva um programa que use vários decoradores para uma função.
O programa deve:
Definir dois decoradores decorator1 e decorator2, que registrem suas chamadas.
Aplicar ambos os decoradores à função say_hello.
Chamar a função say_hello.'''

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Antes da chamada da função")
        result = func(*args, **kwargs)
        print("Decorator 1: Depois da chamada da função")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Antes da chamada da função")
        result = func(*args, **kwargs)
        print("Decorator 2: Depois da chamada da função")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, world!")

say_hello()

'''Escreva um programa que crie um decorador para medir o tempo de execução de uma função.
O programa deve:
Definir um decorador time_decorator, que mede e exibe o tempo de execução de uma função.
Aplicar o decorador à função compute_square(n), que calcula o quadrado de um número e simula um atraso usando time.sleep().
Chamar a função compute_square(n).'''

import time

def time_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time} segundos")
        return result
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(2)  # simulação de atraso
    return n * n

compute_square(5)