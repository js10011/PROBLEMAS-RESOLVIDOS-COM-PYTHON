'''Escreva um programa que copie o arquivo source.txt para o arquivo destination.txt'''
# Abre o arquivo de origem para leitura em modo binário
with open('source.txt', 'rb') as source_file:
    # Lê o conteúdo do arquivo de origem
    content = source_file.read()

# Abre o arquivo de destino para escrita em modo binário
with open('destination.txt', 'wb') as destination_file:
    # Escreve o conteúdo no arquivo de destino
    destination_file.write(content)

'''Escreva um programa que verifica se o arquivo example.txt existe e, se existir, o exclui.

'''
import os

file_path = 'example.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f'Arquivo {file_path} foi excluído.')
else:
    print(f'Arquivo {file_path} não existe.')