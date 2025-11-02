
'''Escreva uma função divide_numbers que recebe dois argumentos e divide o primeiro número pelo segundo.
Se ocorrer a exceção ZeroDivisionError, intercepte-a e exiba o stack trace usando o módulo traceback.'''
import traceback

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        traceback.print_exc()

# Exemplo de chamada da função
divide_numbers(10, 0)

'''Escreva uma função complex_operation que chame várias funções aninhadas e possa gerar uma exceção.

Se ocorrer uma exceção, capture-a e extraia as informações "brutas" do

stack trace usando traceback.extract_tb().

Exiba as informações de cada frame da stack (arquivo, linha, nome da função, texto da linha).'''
import traceback

def complex_operation():
    def inner_function_1():
        def inner_function_2():
            def inner_function_3():
                # Aqui geramos uma exceção
                raise ValueError("An error occurred")
            inner_function_3()
        inner_function_2()
    try:
        inner_function_1()
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        for frame in tb:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}, Code: {frame.line}")

# Exemplo de chamada da função
complex_operation()