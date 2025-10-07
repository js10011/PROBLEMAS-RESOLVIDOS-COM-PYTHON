
'''A entrada de elementos deve continuar até que o usuário insira a palavra "pare". Em seguida, o programa deve exibir a lista final.'''
result = []
while True:
    element = input("Digite um elemento (ou 'pare' para terminar a entrada): ")
    if element.lower() == 'pare':
        break
    result.append(element)
print("Lista final:", result)

