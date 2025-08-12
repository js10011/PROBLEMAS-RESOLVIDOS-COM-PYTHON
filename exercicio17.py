'''

 Crie uma lista chamada sandwich_orders e a preencha com
 os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
 finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
 mostre uma mensagem para cada pedido, por exemplo, Preparei seu
 sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
 para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
 prontos, mostre uma mensagem que liste cada sanduíche preparado
'''
sandwich_orders = ['Presunto', 'queijo', 'calabresa']
finished_sandwiches = []
while sandwich_orders:
    prato = input('Seu prato : ')
    if prato in sandwich_orders:
        print('Seu prato já está preparado')
    else:
     print(f'Apressaremos {prato} pra vc' )
     finished_sandwiches.append(prato)
        
    break
print(finished_sandwiches)


'''
 Escreva um programa que faça uma enquete sobre as
 férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
 pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
 código que apresente os resultados da enquete

'''
listaPais =[]
while True :
   pais = input('Qual pais gostaria de visitar qual  pais ?' )
   print(f'{pais} é  uma boa escolha')
   listaPais.append(pais)
   break
print(listaPais)

