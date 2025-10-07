''': Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'''

''' Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos'''
alien = 'verde', 'amarelo', 'vermelho'
if 'preto' in alien:
    print(' voce ganhou 10 pontos')
elif 'roxo'  != alien:
    print("Seu burro ...")


else:
    print('parabens voce eh muito burro')


''' Escolha uma cor para um alienígena, como foi feito no
Exercício anterior, e escreva uma cadeia if-else.
'''
cor = input("Qual a cor do Alienigena ? ")
if cor  == "preto" :
    print('7 pontos')

elif cor == "azul" :
    print('5 pontos')
elif cor == "verde":
    print("3 pontos")
else:
    print("0 pontos")



'''Escreva uma cadeia if-elif-else que determine o
123
estágio da vida de uma pessoa. Defina um valor para a variável age e então: •
Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma
mensagem dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma
mensagem dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso.'''
# Definir a variável age
age = 25  

if age < 2:
    print("Você é um bebê.")
elif age >= 2 and age < 4:
    print("Você é uma criança.")
elif age >= 4 and age < 13:
    print("Você é um(a) garoto(a).")
elif age >= 13 and age < 20:
    print("Você é um(a) adolescente.")
elif age >= 20 and age < 65:
    print("Você é um adulto.")
else:
    print("Você é idoso.")


'''Faça uma lista de suas frutas favoritas e, então, escreva uma
série de instruções if independentes que verifiquem se determinadas frutas
estão em sua lista.
• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
• Escreva cinco instruções if. Cada instrução deve verificar se uma
determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
frase, por exemplo, Você realmente gosta de bananas!'''

favorite_fruits= ['Banana', 'uva','abacate', 'acai', 'pitaia']

if 'abacaxi' in favorite_fruits :
    print('Eu nao gosta dessa fruta')


'''Escreva um programa que solicite ao usuário um nome de usuário e uma senha.
Se o nome de usuário for "admin" e a senha for "1234", o programa deve exibir a mensagem "Acesso permitido".
Caso contrário, o programa deve exibir a mensagem "Acesso negado".'''


username = input("Digite o nome de usuario: ")
password = input("Digite a senha: ")

if username == "admin" and password == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")