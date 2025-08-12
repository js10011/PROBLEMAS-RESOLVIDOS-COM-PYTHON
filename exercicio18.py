''' Escreva uma função chamada display_message() que mostre
 uma frase informando a todos o que você está aprendendo neste capítulo.
 Chame a função e certifique-se de que a mensagem seja exibida corretamente.'''

def display_message ():
    print("Ola estou aprendendo python")
display_message()

'''Escreva uma função chamada favorite_book() que aceite
 um parâmetro title. A função deve exibir uma mensagem como Um dos meus
 livros favoritos é Alice no país das maravilhas. Chame a função e não se
 esqueça de incluir o título do livro como argumento na chamada da função.'''

def favorite_book(title):
    print(f"Um dos meus livros favoritos eh {title}.")
favorite_book('The Witcher-sangue dos elfos')


'''Escreva uma função chamada make_shirt() que aceite um
 tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
 A função deve exibir uma frase que mostre o tamanho da camiseta e a
 mensagem estampada.
 Chame a função uma vez usando argumentos posicionais para criar uma
 camiseta. Chame a função uma segunda vez usando argumentos nomeados.'''

def make_shirt(tma=7, estam ='LDR'):
    print(f'O tamanho eh {tma}\nEstampa {estam}')
make_shirt(8, 'The wicher')

'''Escreva uma função chamada describe_city() que aceite o
 nome de uma cidade e seu país. A função deve exibir uma frase simples, como
 Reykjavik está localizada na Islândia. Forneça um valor default ao
 parâmetro que representa o país. Chame sua função para três cidades
 diferentes em que pelo menos uma delas não esteja no país default.'''

def describe_city(cidade, país='Brasil'):
    print(f"{cidade} esta localizada em {país}.")

# Chamando a função para três cidades diferentes
describe_city("Belem")            
describe_city("sao luiz") # quando n passado o argumento brasil é passado automaticammente
describe_city('Belo horizonte', "NY") # foi definido o segundo argumento entao brasil sera ignorado default
