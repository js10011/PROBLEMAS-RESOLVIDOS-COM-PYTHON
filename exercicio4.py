# Pense em pelo menos cinco lugares do mundo quevocê gostaria de visitar.

'''Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
em ordem alfabética.'''
paises = ['Russia', 'Grecia', 'Egito', 'Inglaterra', 'Noruega', 'Japao']
paises.sort()
print(paises)
'''Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
lista propriamente dita'''
print(sorted(paises))
''' Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
a ordem da lista original.
'''
paisesInverso =sorted(paises,reverse=True)
print(f'Ordem inversa {paisesInverso}')
'''Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.'''
paises.reverse()
print(paises)

''' Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.'''
paises.sort(reverse= True)
print(paises)

''' Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser.'''

pais = ["America do Sul", "Brasil", "portugues", "real"]
print(f' Lista original : {pais}')
pais.sort(reverse=True)
print(f'Lista inversa  : {pais}')
print(f'Lista voltando a orinnal : {sorted(pais)}')
