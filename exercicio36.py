
'''Escreva um programa que crie um dicionário com informações sobre uma pessoa (por exemplo, nome, idade e cidade) de três maneiras diferentes:

Usando chaves {}.
Usando a função dict() com uma sequência de pares chave-valor.
Usando a função dict() com argumentos nomeados.'''
person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Usando a função dict() com uma sequência de pares chave-valor
person2 = dict([("name", "Bob"), ("age", 25), ("city", "Los Angeles")])

# Usando a função dict() com argumentos nomeados
person3 = dict(name="Charlie", age=35, city="Chicago")

# Imprimir todos os três dicionários
print(person1)
print(person2)
print(person3)


'''Escreva um programa que crie vários dicionários com diferentes quantidades de elementos.

O programa deve:
Exibir a quantidade de elementos em cada dicionário.
Verificar se cada dicionário está vazio e exibir uma mensagem correspondente.
Para verificar se o dicionário está vazio, é necessário criar uma função check_empty.'''

def check_empty(d):
    return len(d) == 0

# Criamos vários dicionários com diferentes quantidades de elementos
dict1 = {}
dict2 = {'a': 1, 'b': 2}
dict3 = {'x': 10}
dict4 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

dictionaries = [dict1, dict2, dict3, dict4]

# Exibimos a quantidade de elementos em cada dicionário e verificamos se estão vazios
for i, d in enumerate(dictionaries, 1):
    print(f"Dicionário {i}: {len(d)} elementos")
    if check_empty(d):
        print(f"Dicionário {i} está vazio")
    else:
        print(f"Dicionário {i} não está vazio")

'''Escreva um programa que cria um dicionário com informações sobre uma pessoa.

O programa deve:
Obter um valor por chave usando colchetes.
Obter de forma segura um valor por chave usando o método get().
Usar o método setdefault() para obter um valor por chave e adicionar a chave se ela não existir.'''
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
# Obter um valor por chave usando colchetes
name = person['name']
print(f'Name: {name}')
# Obter de forma segura um valor por chave usando o método get()
age = person.get('age')
print(f'Age: {age}')
# Usar o método setdefault() para obter um valor por chave e adicionar a chave se ela não existir
country = person.setdefault('country', 'USA')
print(f'Country: {country}')
# Exibir todo o dicionário para ver as alterações
print(person)

'''Escreva um programa que crie um dicionário com informações sobre um livro (por exemplo, título, autor, ano de publicação). O programa deve:
Exibir todas as chaves do dicionário usando o método keys().'''
# Criando um dicionário com informações sobre um livro
book_info = {
    "title": "Crime e Castigo",
    "author": "Fiódor Dostoiévski",
    "year": 1866
}
# Exibindo todas as chaves do dicionário usando o método keys()
keys = book_info.keys()
print(keys)

# Iterando por todas as chaves e exibindo-as na tela
for key in keys:
    print(key)

'''Escreva um programa que crie um dicionário com informações sobre um produto (por exemplo, nome, preço, quantidade).
O programa deve:
Exibir todos os pares chave-valor usando o método items().
Iterar sobre todos os pares chave-valor e exibi-los na tela.
Adicionar um novo par chave-valor ao dicionário e novamente exibir todos os pares chave-valo'''
# Criamos um dicionário com informações sobre o produto
product_info = {
    'Nome': 'Tomates',
    'Preço': 50,
    'Quantidade': 100
}

# Exibimos todos os pares chave-valor usando o método items()
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")

# Iteramos sobre todos os pares chave-valor e os exibimos na tela
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")
# Adicionamos um novo par chave-valor ao dicionário
product_info['Cor'] = 'Vermelho'
# Novamente exibimos todos os pares chave-valor
for key, value in product_info.items():
    print(f"{key}: {value}")

'''Escreva um programa que cria um dicionário com informações sobre um livro (por exemplo, título, autor, ano de publicação).

O programa deve:
Verificar a presença da chave "author" usando o operador in.
Verificar a presença da chave "publisher" usando o método get().
Verificar a presença da chave "title" usando o método keys().'''
# Criamos um dicionário com informações sobre o livro
book_info = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
}

# Verificação da presença da chave "author" usando o operador in
if "author" in book_info:
    print("Chave 'author' encontrada")

# Verificação da presença da chave "publisher" usando o método get()
if book_info.get("publisher") is not None:
    print("Chave 'publisher' encontrada")
else:
    print("Chave 'publisher' não encontrada")

# Verificação da presença da chave "title" usando o método keys()
if "title" in book_info.keys():
    print("Chave 'title' encontrada")

'''Escreva um programa que crie um dicionário com informações sobre um estudante (nome, idade, universidade).
O programa deve:
Verificar a presença do valor "MIT" usando o método values().
Verificar a presença do valor "Harvard" usando a função set().
Verificar a presença do valor 22 usando um gerador.'''
# Criação do dicionário com informações sobre o estudante
student_info = {
    "name": "John Doe",
    "age": 22,
    "university": "MIT"
}

# Verificação da presença do valor "MIT" usando o método values()
contains_mit = "MIT" in student_info.values()
print(f"Contains MIT: {contains_mit}")

# Verificação da presença do valor "Harvard" usando a função set()
contains_harvard = "Harvard" in set(student_info.values())
print(f"Contains Harvard: {contains_harvard}")

# Verificação da presença do valor 22 usando um gerador
contains_22 = any(value == 22 for value in student_info.values())
print(f"Contains 22: {contains_22}")