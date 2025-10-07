
'''Escreva um programa que recebe uma string e uma substring do usuário.
O programa deve verificar se a substring está contida na string usando o operador in,
encontrar a primeira ocorrência da substring usando o método find() e
contar o número de ocorrências da substring usando o método count().'''
# Entrada de string e substring do usuário
string = input("Digite uma string: ")
substring = input("Digite uma substring: ")
# Verificação da presença da substring na string usando o operador in
is_in = substring in string
# Encontrando a primeira ocorrência da substring usando o método find()
first_occurrence = string.find(substring)
#  ando o método count()
count_occurrences = string.count(substring)
# Exibição dos resultados
print(f"A substring está contida na string: {is_in}")
print(f"Primeira ocorrência da substring na string: {first_occurrence}")
print(f"Número de ocorrências da substring na string: {count_occurrences}")

'''
Escreva um programa que receba uma string do usuário, exiba seu comprimento
e, em seguida, solicite um índice ao usuário.
O programa deve exibir o caractere da string nesse índice.
Se o índice estiver fora dos limites da string, o programa deve exibir uma mensagem correspondente.
'''
string = input("Digite uma string: ")
length = len(string)
print(f"Comprimento da string: {length}")

index = int(input("Digite um índice: "))
if index < 0 or index >= length:
    print("Índice fora dos limites da string")
else:
    print(f"Caractere no índice {index}: {string[index]}")


'''
Escreva um programa que receba uma string do usuário e extraia substrings dela usando slices.
O programa deve:
Extrair a substring do 3º ao 8º caractere (índice) inclusive.
Extrair a substring do 5º caractere (índice) até o final da string.
Exibir ambas as substrings
'''
# Recebemos uma string do usuário
input_string = input("Digite uma string: ")
# Extração da substring do 3º ao 8º caractere (índice) inclusive
substring1 = input_string[3:9]
# Extração da substring do 5º caractere (índice) até o final da string
substring2 = input_string[5:]
# Exibição de ambas as substrings
print("Substring do 3º ao 8º caractere inclusive:", substring1)
print("Substring do 5º caractere até o final da string:", substring2)

'''
Escreva um programa que receba uma string do usuário e
realize as seguintes operações usando índices negativos e fatias:
Extraia os últimos três caracteres da string.
Extraia a string, excluindo o último caractere.
Inverta a string.
'''
# Entrada da string pelo usuário
s = input("Digite uma string: ")
# Extrai os últimos três caracteres da string
last_three = s[-3:]
# Extrai a string, excluindo o último caractere
excluding_last = s[:-1]
# Inverte a string
reversed_s = s[::-1]
# Imprime todos os três resultados
print(last_three)
print(excluding_last)
print(reversed_s)
