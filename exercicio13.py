'''Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário'''

dicInf ={'first_name' : 'Lana',
         'last_name' : 'Del Rey',
         'age' : 39}
print(dicInf)

'''Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada
um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
número favorito'''
numero_fav ={
    'lili' : 632,
    'lucy':923,
    'rory':236,
    'lilim':326

}
print(numero_fav)


'''Pense em cinco palavras relacionadas à programação que você conheceu
nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores'''

dict_programacao = {
    'Algoritmo': 'Conjunto de instruções que resolvem um problema ou realizam uma tarefa',
    'API': 'Interface que permite a comunicação entre sistemas e serviços.',
    'CRUD': '(Create, Read, Update, Delete) As operações básicas de manipulação de dados em um banco de dados.',
    'Polimorfismo' : 'apacidade de uma função ou método de se comportar de maneiras diferentes, dependendo do contexto ou tipo de dados.',
    'Deploy':'Processo de colocar um aplicativo em produção, tornando-o disponível para os usuários finais.'

}
for chave, valor in dict_programacao.items():
    print(f'Palavra :{chave}, \nsignificado {valor}\n')

''': Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'''

rios ={'Amazonas': 'Brasil',
       'Ganges' : 'India',
       'Nilo' : 'Egito'}
'''Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito'''
for chav, valo in rios.items():
    print(f' O rio {chav} corre pelo {valo}')

'''Use um laço para exibir o nome de cada rio incluído no dicionário.'''
for ri in rios.values():
    print(ri)

for ri2 in rios.keys():
    print(ri2)

