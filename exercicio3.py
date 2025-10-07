
'''''Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
exibir uma mensagem para cada pessoa, convidando-a para jantar'''

convidados = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci']

for convidado in convidados:
    print(f"Ola {convidado.upper()}, voce esta convidado para o jantar!")

# 
nao_sera = 'Marie Curie'
print(f"\nInfelizmente, {nao_sera} nao podera comparecer ao jantar.\n")


convidados.remove(nao_sera)
convidados.append('Isaac Newton')

# Novo convite para os convidados restantes
for convidado in convidados:
    print(f"Ola {convidado}, voce esta convidado para o jantar!")


#Nova lista 
convidados = ['Albert Einstein', 'Leonardo da Vinci', 'Isaac Newton']

'''Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.'''
'''• Utilize insert() para adicionar um novo convidado no início de sua lista'''
'''• Utilize insert() para adicionar um novo convidado no meio de sua lista'''
''' Utilize append() para adicionar um novo convidado no final de sua lista'''

print("\nOtima noticia! Encontrei uma mesa maior!")
convidados.insert(0, 'Galileu Galilei')  # Inicio
convidados.insert(2, 'Nikola Tesla')     # Meio 
convidados.append('Charles Darwin')      # Fim

for convidado in convidados:
    print(f"Ola {convidado.upper()}, voce esta convidado para o jantar!")


# Lista de convidados
convidados = ['Galileu Galilei', 'Albert Einstein', 'Leonardo da Vinci', 'Isaac Newton', 'Nikola Tesla', 'Charles Darwin']

''' Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.'''
print("\n Agora posso convidar apenas duas pessoas.")

'''Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.'''
removidos = convidados.copy()
while len(convidados) > 2:
    convidado_removido = convidados.pop()
    print(f"Desculpe, {convidado_removido}, nao poderei convida-lo para o jantar.")

'''Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.'''
for convidado in convidados:
    print(f"Ola {convidado}, voce ainda esta convidado para o jantar!")


''' Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.'''
del convidados[:]
print("\nLista  vazia", convidados)


