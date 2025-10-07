'''– Erro proposital: Se você ainda não recebeu um erro de índice em um de
seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em
um de seus programas de modo a gerar um erro de índice. Não se esqueça de
corrigir o erro antes de fechar o programa.'''

#lista= [1,3,8 ,9,2] #erro de index
#print(lista[7])
#print(29/0) # erro de ZeroDivisionError
#print 'hello' #SyntaxError
#print('olla'+ 5) #TypeError

'''Escreva um programa que solicite um número ao usuário e use a biblioteca math para calcular e imprimir a raiz quadrada e o fatorial desse número.'''
import math
num = int(input("Digite um numero: "))
sqrt_num = math.sqrt(num)
print(f"A raiz quadrada de {num} é igual a {sqrt_num}")
factorial_num = math.factorial(num)
print(f"O fatorial de {num} é igual a {factorial_num}")

'''Escreva um programa que gera 10 números aleatórios no intervalo de 1 a 100, utilizando a biblioteca random.
Depois, calcule a média deles e exiba na tela.'''
import random
numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(numbers) / len(numbers)
print("Numeros aleatorios:", numbers)
print("Valor medio:", average)