''': Crie uma lista com cinco ou mais nomes de usuários, incluindo
o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário:'''

users = ['Maria', 'jose', 'jesus', 'judas', ]
for user in users:
    print(f'Ola {user}')

'''• Se o
nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá
admin, gostaria de ver um relatório de status?'''

'''Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
fazer login novamente.
'''
if  'admin' in users:
    print(' Ola admin, gostaria de ver um relatorio de status?')

elif users  ==[]:
    print('Precisamos encontrar alguns usuarios')
else:
    print('Ja tem uma conta ?')

'''Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida'''
del users
print('excluidos')


''': Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de
usuário único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
que um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de
usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando
que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi
usado, apresente uma mensagem dizendo que o nome do usuário está
disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças
entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
ser aceit'''

current_users = ['Maria', 'joao', 'bia']
new_users = ['bia', 'joao', 'marie']
for user in new_users :
    print('ola')


'''Números ordinais indicam sua posição em uma lista,
por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa
língua termina com th, exceto 1, 2 e 3.
• Armazene os números de 1 a 9 em uma lista.
• Percorra a lista com um laço.
• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th
6th 7th 8th 9th", e cada resultado deve estar em uma linha separada.
'''

numeros = list(range(1, 10))  # Cria lista de 1 a 9

for numero in numeros:
    if numero == 1:
        print(f"{numero}st")
    elif numero == 2:
        print(f"{numero}nd")
    elif numero == 3:
        print(f"{numero}rd")
    else:
        print(f"{numero}th")
