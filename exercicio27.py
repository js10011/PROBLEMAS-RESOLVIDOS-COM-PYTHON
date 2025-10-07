'''Os anos bissextos ocorrem a cada 4 anos, por exemplo, os anos 2004, 2008, 2012, 2016 , 2020...
Escreva um programa que peça ao usuário um ano e verifique se ele é bissexto.

Use operadores lógicos para verificar as condições de um ano bissexto.

Um ano bissexto é divisível por 4, mas não é divisível por 100, exceto nos anos que são divisíveis por 400. '''
year = int(input("Digite o ano: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

'''Escreva um programa que solicita dois números do usuário.
Se o usuário não inserir um valor (string vazia), utilize o valor padrão None para esse número.
Calcule e exiba a soma desses números.'''

a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

a = None if a == "" else float(a)
b = None if b == "" else float(b)

if a is None or b is None:
    print("A soma dos números é desconhecida")
else:
    sum_result = a + b
    print("A soma dos números:", sum_result)