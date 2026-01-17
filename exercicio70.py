'''Escreva um programa que serialize uma lista em um arquivo usando o módulo pickle,
e depois desserialize essa lista a partir do arquivo.'''
import pickle

# Exemplo de lista para serialização
data = [1, 2, 3, 'a', 'b', 'c']

# Serialização da lista em um arquivo
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Desserialização da lista do arquivo
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Verificação do resultado
print(loaded_data)

'''Escreva um programa que serializa um dicionário em uma string usando o módulo pickle,
e depois desserializa esse dicionário da string.'''
import pickle

# Exemplo de dicionário para serialização
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Serialização do dicionário para string
serialized_data = pickle.dumps(data)

# Desserialização do dicionário da string
deserialized_data = pickle.loads(serialized_data)

# Imprime o resultado para verificação
print("Serialized data:", serialized_data)
print("Deserialized data:", deserialized_data)