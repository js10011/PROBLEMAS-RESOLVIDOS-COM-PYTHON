'''
Crie uma lista de nomes de mágicos. Passe a lista para uma
 função chamada show_magicians() que exiba o nome de cada mágico da
 lista
'''
lista=['bob o maluco', 'os gemeos retardado e lesado', 'cachorra rapujenta','leprosa']
def show_magicians(nomes=lista):
    print(nomes)
show_magicians()

'''
Comece com uma cópia de seu programa do
 Exercício 8.9. Escreva uma função chamada make_great() que modifique a
 lista de mágicos acrescentando a expressão o Grande ao nome de cada
 mágico. Chame show_magicians() para ver se a lista foi realmente modificada.
'''


'''
Comece com uma cópia de seu programa do
 Exercício 8.9. Escreva uma função chamada make_great() que modifique a
 lista de mágicos acrescentando a expressão o Grande ao nome de cada
 mágico. Chame show_magicians() para ver se a lista foi realmente modificada
'''
lista_copiada=lista.copy()
lista_copiada.append('o grande bundao')
def make_great():
    print(lista_copiada)
make_great()
