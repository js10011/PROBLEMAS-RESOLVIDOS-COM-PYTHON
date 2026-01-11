
'''Escreva um programa que leia e exiba o conteúdo do arquivo example.txt completamente.'''
# Abertura do arquivo em modo de leitura
file = open('example.txt', 'r')

# Leitura do conteúdo do arquivo
content = file.read()

# Exibição do conteúdo na tela
print(content)

# Fechamento do arquivo
file.close()

'''Escreva um programa que leia o arquivo example.txt linha por linha, usando um iterador, e exiba cada linha na tela.'''
# Abertura do arquivo em modo de leitura
file = open('example.txt', 'r')

# Leitura do arquivo linha por linha e exibição do conteúdo
for line in file:
    print(line, end='')

# Fechamento do arquivo
file.close()

'''Escreva um programa que crie um novo arquivo example.txt e grave nele a string "This is a new file."'''
# Abrindo o arquivo em modo de escrita
file = open("example.txt", "w")

# Gravando a string no arquivo
file.write("This is a new file.")

# Fechando o arquivo
file.close()

'''Escreva um programa que abre o arquivo example.txt no modo de adição e
adiciona as linhas "Nós adicionamos esta linha." e "E esta também."'''
# Abrindo o arquivo no modo de adição com codificação UTF-8
file = open('example.txt', 'a', encoding='utf-8')

# Escrevendo linhas no arquivo
file.write('Nós adicionamos esta linha.\n')
file.write('E esta também.\n')

# Fechando o arquivo
file.close()