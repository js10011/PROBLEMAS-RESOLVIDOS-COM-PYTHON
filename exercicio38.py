
''' Escreva um programa que crie um dicionário com informações sobre uma pessoa (por exemplo, nome, idade, endereço e informações de contato).

O programa deve:
Percorrer todos os elementos do dicionário, incluindo dicionários aninhados, usando loops.
Implementar uma função para percorrer todos os níveis de aninhamento e exibir chaves e valores.'''

def print_info(data, indent=0):
    for key, value in data.items():
        print('  ' * indent + f"{key}: ", end="")
        if isinstance(value, dict):
            print()
            print_info(value, indent + 1)
        else:
            print(value)

person_info = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    },
    "contact": {
        "email": "john.doe@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    }
}

print_info(person_info)


'''Escreva um programa que cria um dicionário com informações sobre uma pessoa (por exemplo, nome, idade, endereço e informações de contato).

O programa deve:
Alterar valores no nível superior, no dicionário aninhado e em níveis mais profundos de aninhamento.
Adicionar um novo elemento ao dicionário aninhado.
Excluir elementos tanto do dicionário aninhado quanto do nível superior.'''
# Criamos um dicionário com informações sobre uma pessoa
person = {
    'name': 'Alexey',
    'age': 30,
    'address': {
        'city': 'Moscou',
        'street': 'Tverskaya',
        'house': 10
    },
    'contact_info': {
        'email': 'alexey@example.com',
        'phone': '+7 123 456 7890'
    }
}

# Alteramos valores no nível superior
person['name'] = 'Alexandre'
person['age'] = 31

# Alteramos valores no dicionário aninhado
person['address']['city'] = 'São Petersburgo'
person['address']['street'] = 'Perspectiva Nevsky'

# Alteramos valores em um nível de aninhamento mais profundo
person['contact_info']['email'] = 'alexandre@example.com'

# Adicionamos um novo elemento ao dicionário aninhado
person['address']['apartment'] = 5

# Excluímos um elemento do dicionário aninhado
del person['contact_info']['phone']

# Excluímos um elemento do nível superior
del person['age']

# Exibimos o resultado
print(person)