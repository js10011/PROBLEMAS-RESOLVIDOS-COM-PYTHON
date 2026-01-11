'''Escreva um programa que abra o arquivo example.txt no modo de adição, escreva nele a linha "Nova linha.".

É necessário tratar corretamente a exceção FileNotFoundError, fechando o arquivo em qualquer caso.

O operador with não pode ser usado.'''
file = None 
try:
    file = open('example.txt', 'a')
    file.write("Nova linha.")
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    if file:
        file.close()


'''Escreva um programa que abra o arquivo example.txt no modo de adição e escreva nele a linha "Nova linha.".
É necessário tratar corretamente a exceção FileNotFoundError, fechando o arquivo em qualquer caso.
É necessário usar o operador with para o fechamento automático do arquivo.'''

try:
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write('Nova linha.')
except FileNotFoundError:
    print("Arquivo não encontrado.")

'''Escreva um programa que lê um arquivo binário example.bin e exibe seu conteúdo no console na forma de bytes.'''
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

'''Escreva um programa que lê a imagem input_image.jpg e a grava em outro arquivo chamado output_image.jpg'''
# Leitura da imagem input_image.jpg em modo binário
with open('input_image.jpg', 'rb') as input_file:
    image_data = input_file.read()

# Gravação dos dados em um novo arquivo output_image.jpg
with open('output_image.jpg', 'wb') as output_file:
    output_file.write(image_data)