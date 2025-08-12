''' Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte'''
''' • Exiba a
mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
exibir os três primeiros itens da lista desse programa.'''
pais = ["America do Sul", "Brasil", "portugues", "real","Amazonia", "carnaval", "futebol"]
print(f'Os tres primeiros itens da lista sao:\n{pais[:3]}')

'''Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista.'''
print(f'Os tres ultimos itens da lista sao:\n{pais[4:]}')

'''Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte: • Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.'''

friend_pizzas = ['Calabresa', '4 queijos', 'Carne de sol', 'Marguerita']
friend_pizzas.append('Pizza doce')
print(friend_pizzas)
for minhasPizz in friend_pizzas:
    print(minhasPizz)