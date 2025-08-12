''': Use um laço for para exibir os números de 1 a 20,
incluindo-os.'''
for numeros in range(1, 21):
    print(numeros)

''': Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números.'''
for numeros in range(1, 21, 2):
    print(numeros)

'''Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista'''

for num in range(3, 31, 3):
    print(num)

''': Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
para exibir o valor de cada cubo'''
num_lista = [1, 2, 3,4, 5, 6, 7, 8, 9, 10] 
for cubo in num_lista:
    print(cubo**3)


''' Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
'''
num_lista= [value**3 for value in range(1,11)]
print(num_lista)
 