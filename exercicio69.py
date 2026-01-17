'''Escreva um programa que serialize e deserialize um objeto Python usando o módulo pickle.

O objeto para serialização será um dicionário contendo informações sobre o estudante: nome, idade e status do estudante.'''
import pickle

# Objeto para serialização
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Serialização do objeto
with open('student_info.pkl', 'wb') as f:
    pickle.dump(student_info, f)

# Desserialização do objeto
with open('student_info.pkl', 'rb') as f:
    loaded_student_info = pickle.load(f)

print(loaded_student_info)

'''Escreva um programa que serializa e desserializa um objeto Python utilizando o módulo yaml.
O objeto para serialização será um dicionário contendo informações sobre um filme: título, diretor e ano de lançamento.'''
import yaml

film_info = {
    "título": "Matrix",
    "diretor": "Lana e Lilly Wachowski",
    "ano de lançamento": 1999
}

yaml_str = yaml.dump(film_info, default_flow_style=False)

deserialized_data = yaml.load(yaml_str, Loader=yaml.SafeLoader)

print("String serializada no formato YAML:")
print(yaml_str)

print("Objeto dicionário desserializado:")
print(deserialized_data)