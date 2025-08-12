'''Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples,
como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.'''

nome= input("Qual o seu nome ? ")
print(f'Olá {nome}, gostaria de aprender um pouco de python  ?')

''' Armazene o nome de uma
pessoa em uma variável e então apresente o nome dessa pessoa em letras
minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.'''

pessoa = "marie curie"
print(pessoa.lower())
print(pessoa.upper())
print(pessoa.capitalize())

''' Encontre uma citação de uma pessoa famosa que você
admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência
a seguir, incluindo as aspas: Albert Einstein certa vez disse: “Uma pessoa que
nunca cometeu um erro jamais tentou nada novo.”'''
frase = "Menos é mais "
print(f'Ludwig disse - "{frase}."')

'''
 Repita o Exercício anterior , porém, desta vez, armazene o
nome da pessoa famosa em uma variável chamada famous_person. Em
seguida, componha sua mensagem e armazene-a em uma nova variável
chamada message. Exiba sua mensagem.
'''
famous_person = "Ludwig"
messagem = frase
print(f'{famous_person} - "{messagem}"')

'''
 Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.
'''
print("\t Charles Babage \n")




'''
Exiba o nome uma vez, de modo que os espaços em branco em torno do
nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três
funções de remoção de espaços: lstrip(), rstrip() e strip().
'''
NomePessoa = "\t   Marie Jane   \n"
print(NomePessoa)
print(NomePessoa.lstrip())
print(NomePessoa.rstrip())
print(NomePessoa.strip())