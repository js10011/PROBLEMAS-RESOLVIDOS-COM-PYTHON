
'''Escreva um programa que crie um novo diretório new_directory.

Em seguida, crie um diretório aninhado parent_directory/child_directory.

E então exclua os diretórios criados.'''
import os
import shutil

# Criação do diretório new_directory
os.makedirs('new_directory')

# Criação do diretório aninhado parent_directory/child_directory
os.makedirs('parent_directory/child_directory')

# Exclusão do diretório new_directory
shutil.rmtree('new_directory')

# Exclusão do diretório aninhado parent_directory/child_directory
shutil.rmtree('parent_directory')

'''Escreva um programa que exiba o conteúdo do diretório de trabalho atual e
para cada arquivo ou diretório, indique se é um arquivo ou um diretório.
Requisitos:'''

import os

# Obtém a lista de arquivos e diretórios no diretório de trabalho atual
items = os.listdir('.')

# Percorre cada elemento e verifica seu tipo
for item in items:
    if os.path.isdir(item):
        print(f'{item} - Diretório')
    elif os.path.isfile(item):
        print(f'{item} - Arquivo')
    else:
        print(f'{item} - Tipo desconhecido')