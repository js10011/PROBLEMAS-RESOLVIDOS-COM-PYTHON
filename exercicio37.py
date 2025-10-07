
'''Escreva um programa que cria um dicionário com informações sobre um estudante (nome e idade).

O programa deve:
Adicionar um novo elemento "universidade" no dicionário.
Adicionar o elemento "cidade" apenas se ele ainda não estiver no dicionário.
Adicionar vários novos elementos usando o método update().'''
# Criação do dicionário com informações sobre o estudante  
student = {  
    "name": "Ivan",  
    "age": 20  
}  

# Adição de um novo elemento "universidade"  
student["universidade"] = "MGU"  
print("Após adicionar 'universidade':", student)  

# Adição do elemento "cidade" apenas se ele ainda não estiver no dicionário  
if "cidade" not in student:  
    student["cidade"] = "Moscou"  
print("Após possível adição de 'cidade':", student)  

# Adição de vários novos elementos usando o método update()  
student.update({"faculdade": "Física", "ano": 3})  
print("Após adicionar novos elementos usando update():", student)

'''Escreva um programa que crie um dicionário com informações sobre um livro (título, autor, ano de publicação).

O programa deve:
Alterar o valor da chave "ano de publicação".
Usar o método setdefault() para adicionar uma nova chave "editora", caso ela não exista.
Atualizar os valores de vários elementos usando o método update().'''
# Criamos um dicionário com informações sobre um livro
book = {
    "título": "Guerra e Paz",
    "autor": "Liev Tolstói",
    "ano de publicação": 1869
}

# Alteramos o valor da chave "ano de publicação"
book["ano de publicação"] = 1873
print("Após a alteração do ano de publicação:", book)

# Usamos o método setdefault() para adicionar uma nova chave "editora"
book.setdefault("editora", "Editora AST")
print("Após a adição da editora:", book)

# Atualizamos os valores de vários elementos usando o método update()
book.update({
    "título": "Anna Kariênina",
    "autor": "Liev Tolstói",
    "ano de publicação": 1877
})
print("Após a atualização de vários elementos:", book)

'''Escreva um programa que crie um dicionário com informações sobre um estudante (nome, idade, universidade).
O programa deve:
Iterar sobre os pares chave-valor do dicionário usando a função enumerate().'''
# Criamos um dicionário com informações sobre o estudante
student_info = {
    'name': 'Alice',
    'age': 21,
    'university': 'Harvard'
}

# Iteramos sobre os pares chave-valor do dicionário usando a função enumerate
for index, (key, value) in enumerate(student_info.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

'''Escreva um programa que crie uma lista de tuplas com informações sobre funcionários (por exemplo, nome e cargo).

O programa deve:
Usar dictionary comprehension para criar um dicionário a partir de uma lista de tuplas.'''
# Lista de tuplas com informações sobre funcionários
employees = [("Ivan", "Engenheiro"), ("Maria", "Gerente"), ("Pedro", "Analista")]

# Criação de dicionário usando dictionary comprehension
employee_dict = {name: position for name, position in employees}

# Exibição do dicionário criado
print(employee_dict)

