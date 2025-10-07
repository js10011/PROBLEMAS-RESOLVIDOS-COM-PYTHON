
'''Escreva um programa que exiba números de 1 a 100, pulando os números pares.
Use um loop while e a instrução continue para pular os números pares.'''
num = 1
while num <= 100:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1

'''Escreva um programa que solicite números ao usuário e os some até que o usuário insira um número negativo.
Use um loop while e o operador break para encerrar a entrada ao encontrar um número negativo.'''
total = 0

while True:
    num = float(input("Digite um numero: "))
    if num < 0:
        break
    total += num

print(f"Soma dos numeros inseridos: {total}")