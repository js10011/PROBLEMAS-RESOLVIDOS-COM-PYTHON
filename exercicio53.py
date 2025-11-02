
'''Escreva uma função safe_division que receba dois números e realize a divisão deles.

Lide com as exceções que podem surgir ao dividir por zero

e ao passar valores incorretos (por exemplo, strings em vez de números).

A função deve retornar uma mensagem de erro ou o resultado da divisão'''
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except TypeError:
        return "Erro: tipo de dado incorreto"
    return result

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Erro: divisão por zero.")
else:
    print(f"Resultado: {result}")
finally:
    print("Este bloco sempre é executado.")
####################################################3
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except IOError:
    print("Erro: erro de entrada/saída.")
else:
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("Arquivo fechado.")

'''Escreva a função process_input, que recebe uma string e tenta transformá-la em um número inteiro.
Se a conversão for bem-sucedida, a função deve retornar o quadrado do número.
Se a string não for um número, capture o ValueError e exiba a mensagem de erro.
Se a string estiver vazia, capture o IndexError e exiba a mensagem correspondente.'''
def process_input(input_string):
    try:
        if input_string == "":
            raise IndexError("String vazia")
        number = int(input_string)
        return number ** 2
    except ValueError:
        print("Erro: a string fornecida não é um número.")
    except IndexError:
        print("Erro: string vazia fornecida.")

# Exemplos de chamada da função
print(process_input("5"))         # Saída: 25
print(process_input("abc"))       # Saída: Erro: a string fornecida não é um número.
print(process_input(""))          # Saída: Erro: string vazia fornecida.

'''Escreva uma função read_integer, que recebe uma string e tenta convertê-la para um número inteiro.
Se ocorrer um ValueError, trate a exceção e exiba os argumentos do erro e o tipo do erro.
Adicionalmente, salve a exceção em uma variável e a exiba fora do bloco except.''' 
def read_integer(input_string):
    exception_instance = None
    try:
        return int(input_string)
    except ValueError as e:
        exception_instance = e
        print(f"Error arguments: {e.args}")
        print(f"Error type: {type(e)}")
    print(f"Exception instance: {exception_instance}")

# Exemplo de chamada da função
read_integer("abc")