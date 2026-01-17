'''Escreva um programa que envie uma solicitação GET com parâmetros para uma URL e processe a resposta JSON recebida.'''
import requests

# URL para envio da solicitação GET
url = 'https://api.example.com/data'

# Parâmetros da solicitação
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Envio da solicitação GET
response = requests.get(url, params=params)

# Verificação de sucesso da solicitação
if response.status_code == 200:
    # Processamento da resposta JSON
    data = response.json()
    # Impressão dos dados
    print(data)
else:
    print(f"Solicitação falhou com o código de status: {response.status_code}")

'''Escreva um programa que envie uma solicitação POST com dados JSON para um URL e processe a resposta JSON recebida.'''
import requests
import json

# URL para envio da solicitação POST
url = 'http://example.com/api'

# Dados que serão enviados como JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Envio da solicitação POST com dados JSON
response = requests.post(url, json=data)

# Verificação do sucesso da solicitação
if response.status_code == 200:
    # Processamento da resposta JSON recebida
    response_data = response.json()
    print(json.dumps(response_data, indent=4))  # Impressão dos dados da resposta em formato legível
else:
    print(f"Solicitação POST falhou, código de status: {response.status_code}")