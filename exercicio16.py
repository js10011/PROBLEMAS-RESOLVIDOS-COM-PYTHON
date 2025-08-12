''': Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza'''

client = input('Digite seus ingredientes favoritos:')
client +='\nDigite s para sair '

while True :
    ingre = input(client)
    if ingre  == 's':
        break
    else :
        print(f'Ingrediente adicionado {ingre}')

'''   : Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema.'''

while True:
    
    idade = int(input("Digite a sua idade: "))
    
    
    if idade < 3:
        print("O ingresso eh gratuito.")
    elif 3 <= idade <= 12:
        print("O ingresso custa 10 reias.")
    else:
        print("O ingresso custa 15 reais.")
    
    
    continuar = input("Gostaria de verificar outro ingresso? (s/n): ").lower()
    if continuar != 's':
        break

''' use um teste condicional na
instrução while para encerrar o laço; • use uma variável active para controlar
o tempo que o laço executará; • use uma instrução break para sair do laço
quando o usuário fornecer o valor 'quit'.
'''
while True:
  ativo = input('Digite 1 ou 0 | S para sair ')
  if ativo  == '1':
      print('Positivo')
  elif ativo == '0':
       print('Negativo')
  elif ativo == 's' : break

'''  Escreva um laço que nunca termine e execute-o. (Para encerrar o
laço, pressione CTRL-C ou feche a janela que está exibindo a saída.)
'''

countt= 1
while True:
    if countt >= 0:
        
        print((countt * 3) + 7 -2)

   