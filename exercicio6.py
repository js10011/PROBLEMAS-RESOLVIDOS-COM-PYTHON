''': Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
'''
pizzas = ['Calabresa', '4 queijos', 'Carne de sol', 'Marguerita']
for pizza in pizzas :
    print(pizza)

'''Modifique seu laço for para mostrar uma frase usando o nome da pizza em
vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
na saída contendo uma frase simples como Gosto de pizza de pepperoni.
'''

pizzas = ['Calabresa', '4 queijos', 'Carne de sol', 'Marguerita']
for pizza in pizzas :
    print(f'Gosto de pizza de {pizza}\nEu realmente adoro esse sabor!')


''': Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
'''
fofos = ["Coala", "gato", "urso panda", "leao"]
for bebes in fofos: print(bebes)

'''Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
'''
fofos = ["Coala", "gato", "urso panda", "leao"]
for bebes in fofos: print(f'Um {bebes} seria um otimo animalzinho')
