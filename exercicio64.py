
'''Escreva um programa que abra um arquivo example.txt para leitura, leia seu conteúdo e o exiba na tela.
Depois disso, feche o arquivo.'''
# Abertura do arquivo
file = open("\exercicio58.txt", 'r')

# Leitura do conteúdo do arquivo
content = file.read()
print(content)

# Fechamento do arquivo
file.close()

'''Escreva um programa que cria ou abre um arquivo example.txt no modo de escrita e escreve nele a string "Hello, World!".
Depois, abra o arquivo no modo de adição e adicione a string "Appended text.'''
# Abrindo o arquivo no modo de escrita e escrevendo a string "Hello, World!"
file = open('example.txt', 'w')
file.write("Hello, World!")
file.close()

# Abrindo o arquivo no modo de adição e adicionando a string "Appended text."
file = open('example.txt', 'a')
file.write("Appended text.")
file.close()