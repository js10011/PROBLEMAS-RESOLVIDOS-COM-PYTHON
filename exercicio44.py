'''Escreva um programa que cria um diretório, entra nele, cria um arquivo dentro desse diretório,

escreve texto no arquivo, e em seguida lê e exibe seu conteúdo.
O programa deve:
Criar um diretório chamado test_directory.
Entrar no diretório test_directory.
Criar um arquivo test_file.txt e escrever a linha "Hello, World!" nele.
Ler o conteúdo do arquivo test_file.txt e exibi-lo na tela.
Excluir o arquivo e o diretório.'''

import os

# Criamos o diretório
os.makedirs('test_directory', exist_ok=True)

# Entramos no diretório
os.chdir('test_directory')

# Criamos o arquivo e escrevemos a string nele
with open('test_file.txt', 'w') as file:
    file.write('Hello, World!')

# Lemos o conteúdo do arquivo
with open('test_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Removemos o arquivo
os.remove('test_file.txt')

# Voltamos para o diretório pai
os.chdir('..')

# Removemos o diretório
os.rmdir('test_directory')

'''Escreva um programa que obtem e exibe informações sobre o sistema operacional atual
e a plataforma usando a biblioteca platform. O programa deve:
Obter e exibir o nome do sistema operacional.
Obter e exibir o nome do computador na rede (hostname).
Obter e exibir a versão do sistema operacional.
Obter e exibir a arquitetura do processador.
Obter e exibir a versão do Python.'''

import platform
import socket

print("Nome do sistema operacional:", platform.system())
print("Nome do computador na rede (hostname):", socket.gethostname())
print("Versão do sistema operacional:", platform.version())
print("Arquitetura do processador:", platform.architecture()[0])
print("Versão do Python:", platform.python_version())