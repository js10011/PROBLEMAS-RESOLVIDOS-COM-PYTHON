
'''Utilize o pacote requests para realizar uma solicitação GET a uma API.

Execute os seguintes passos:

Instale o pacote requests usando o pip.

Utilize o pacote requests para realizar uma solicitação GET a uma API, por exemplo, para https://jsonplaceholder.typicode.com.

Exiba o resultado da solicitação na tela.'''

import requests

# Execução da solicitação GET a uma API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Exibição do resultado da solicitação
print(response.json())