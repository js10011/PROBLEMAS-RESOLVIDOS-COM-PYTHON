'''  Escreva um programa que pergunte ao usuário
qual tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse
carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”'''

car =input('Qual tipo de carro voce gostaria de alugar ?')
print(f' Irei verificar se temos um {car} para voce')

''' : Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta  '''

pessoas = int(input('Quantas pessoas vieram para o jantar ?'))

if pessoas >= 8 :
    print('Devam esperar um mesa maior')
else:
    print('Estamos prontos')

''' Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.'''

numero = int(input('Digite um numero : '))

if numero % 10 == 0  :
    print(f' {numero} e multiploo de 10')
else:
    print(f' {numero} nao e multiplo de 10')