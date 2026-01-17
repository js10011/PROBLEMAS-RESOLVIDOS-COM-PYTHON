'''Escreva um programa que envia uma solicitação GET para o servidor e processa a resposta, incluindo o status code, headers e o corpo da resposta.'''

import requests

# URL para enviar a solicitação GET
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Envio da solicitação GET
response = requests.get(url)

# Processamento da resposta
status_code = response.status_code
headers = response.headers
body = response.text

# Exibição dos resultados
print(f'Status Code: {status_code}')
print('Headers:')
for key, value in headers.items():
    print(f'  {key}: {value}')
print('Body:')
print(body)

'''Escreva um programa que envia uma requisição GET para o servidor e trata possíveis erros usando exceções.'''
import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança HTTPError para respostas ruins (4xx e 5xx)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"Ocorreu um erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Ocorreu um erro de conexão: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Ocorreu um erro de timeout: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ocorreu um erro: {req_err}")

url = "http://example.com"
content = fetch_url(url)
if content:
    print(content)