'''Escreva um programa que envia uma requisição GET através de um servidor proxy utilizando a biblioteca requests.'''
import requests

# Servidor proxy e porta
proxy = {
    'http': 'http://your_proxy_server:port',
    'https': 'https://your_proxy_server:port'
}

# URL para enviar a requisição GET
url = 'http://example.com'

try:
    response = requests.get(url, proxies=proxy)
    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")



'''Escreva um programa que envie uma solicitação GET através de um proxy server usando a biblioteca http.client.'''
import http.client

# Proxy server
proxy_host = "proxy.example.com"
proxy_port = 8080

# Servidor de destino e solicitação
target_host = "www.example.com"
target_path = "/"

# Estabelecendo conexão com o proxy server
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Enviando solicitação GET através do proxy server
conn.request("GET", target_path, headers={"Host": target_host})

# Obtendo resposta
response = conn.getresponse()

# Imprimindo status e dados da resposta
print(response.status, response.reason)
data = response.read()
print(data.decode('utf-8'))

# Fechando conexão
conn.close()