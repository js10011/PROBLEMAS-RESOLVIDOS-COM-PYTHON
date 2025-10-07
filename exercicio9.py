'''Um restaurante do tipo buffet oferece apenas cinco tipos básicos
de comida. Pense em cinco pratos simples e armazene-os em uma tupla.'''

comidas = ('Farofa', 'carne assada', 'calabresa frita', 'caldo de ovos')

'''Use um laço for para exibir cada prato oferecido pelo restaurante.
'''
for comida in comidas :
    print(f'No restaurante "Bom Sabor" tem {comida}')



'''Escreva um programa que solicita ao usuário dois números de ponto flutuante e os compare usando uma margem de erro aceitável epsilon.
Imprima o resultado da comparação na tela.'''# Solicitar dois números de ponto flutuante do usuário
num1 = float(input("Digite um  numero flutuante: "))
num2 = float(input("Digite outro numero  flutuante: "))

# Definir a margem de erro aceitável
epsilon = 1e-9

# Comparar os números com a margem de erro
if abs(num1 - num2) < epsilon:
    print("Os numeros sao iguais")
else:
    print("Os numeros nao sao iguais")