''''
Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista
de pessoas com um laço

'''
peoples = [

    {'pessoa1': 'Marie',
     'idade' : 65,
     'ocupacao' : 'cientista'},
    {'pessoa2' : 'Newton',
     'idade' : 89,
     'ocupacao': 'cientista'}
]

for pessoa in peoples :
    print(pessoa)


'''Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
'''


dicio1 ={'animal' :' gato', 'idade' :5, 'dono' : 'bia'}

dicio2 ={'animal': 'cachorro', 'idade' : 9, 'dono' : 'caio'}

pets = [dicio1, dicio2]
#print(pets)
for pet in pets:
    print(pet)

''' Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três
lugares favoritos para cada pessoa.  '''

favorite_places = {
    "Ana": ["Praia de Copacabana", "Parque Ibirapuera"],
    "Carlos": ["Montanhas Rochosas", "Londres"],
    "Mariana": ["Ilha de Santorini"]
}

print(favorite_places)
for pesssoas in favorite_places.items(): print(f'O lugar favorito de {pesssoas}')


'''  para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.
 '''

dictNum = {
    'Bia': [1, 3],
    'Caio' : [3, 5],
    'Ana': [5,9]
}
for nome, num in dictNum.items():
    print(nome, num)

'''Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações
sobre cada cidade e inclua o país em que a cidade está localizada, a
população aproximada e um fato sobre essa cidade. As chaves do dicionário
de cada cidade devem ser algo como country, population e fact. Apresente o
nome de cada cidade e todas as informações que você armazenou sobre ela.
'''

cities ={
    'Brasilia':['capital do brasil','america do sul'],
    'Moscou' : ['capital da russia', 'asia'],
    'Tokyo' : ['capital do japao', 'asia']
 }
for cid, cara in cities.items():
    print(cid, cara)
