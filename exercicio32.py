
'''
Crie um conjunto vazio.
Solicite ao usuário 5 números consecutivamente.
Para cada um deles, crie um conjunto separado e adicione-o ao original.
Exiba o resultado obtido na tela.
'''
initial_set = set()

for _ in range(5):
    number = int(input("Digite um número: "))
    number_set = {number}
    initial_set.update(number_set)

print(initial_set)

'''
Escreva um programa que armazene um conjunto com os 5 nomes mais populares de gatos.

O usuário deve tentar adivinhar os nomes. Quando ele adivinhar o nome de um gato, este deve ser removido do conjunto.

O objetivo do jogo é adivinhar todos os nomes com o menor número possível de tentativas.
'''
popular_cat_names = {"Barcik", "Murka", "Vaska", "Neve", "Murzik"}
attempts = 0
while popular_cat_names:
    guess = input("Adivinhe o nome de um gato: ")
    attempts += 1
    if guess in popular_cat_names:
        popular_cat_names.remove(guess)
        print(f"Certo! Restam {len(popular_cat_names)} nomes para adivinhar.")
    else:
        print("Errado. Tente novamente.")

print(f"Você adivinhou todos os nomes em {attempts} tentativas!")

'''
Escreva um programa que crie um conjunto contendo os nomes de várias frutas.

Depois, o programa deve solicitar ao usuário o nome de uma fruta para remover e removê-la do conjunto usando o método discard().
O programa deve exibir o conjunto atualizado.
Se o elemento não for encontrado, o programa deve continuar sem erro.
'''
# Criamos um conjunto com os nomes das frutas
fruits = {"maçã", "banana", "laranja", "pêra", "pêssego"}

# Solicitamos ao usuário o nome da fruta para remover
fruit_to_remove = input("Digite o nome da fruta para remover: ")

# Removemos a fruta do conjunto, se existir
fruits.discard(fruit_to_remove)

# Exibimos o conjunto atualizado
print("Conjunto atualizado de frutas:", fruits)


'''
Escreva um programa que cria um conjunto de números aleatórios no intervalo de 1 a 50.
Depois, o programa deve imprimir todos os elementos do conjunto junto com seus "índices", usando a função enumerate().
'''
import random

# Criamos um conjunto de números aleatórios no intervalo de 1 a 50
random_set = {random.randint(1, 50) for _ in range(10)}

# Imprimimos os elementos do conjunto junto com seus "índices"
for index, value in enumerate(random_set):
    print(f"{index}: {value}")


'''
Escreva um programa que crie um conjunto contendo os nomes de várias frutas.
O programa deve exibir as frutas na tela.
Em seguida, o programa deve solicitar ao usuário um número e um novo nome de fruta para substituição.
Depois, encontrar a fruta pelo número (número sequencial da exibição na tela), substituí-la pelo novo nome e exibir o conjunto atualizado.
'''
fruits = {"maçã", "banana", "laranja", "pêra"}

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

index = int(input("Digite o número da fruta para substituição: ")) - 1
new_fruit = input("Digite o novo nome da fruta: ")

fruits_list = list(fruits)
fruits_list[index] = new_fruit
fruits = set(fruits_list)

print("Conjunto de frutas atualizado:", fruits)