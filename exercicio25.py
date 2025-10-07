
'''Escreva um programa que calcula e exibe a soma de todos os números de 1 a 100 inclusive, usando o loop for e a função range().'''
total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)

'''Escreva um programa que calcule quantos grãos estarão em cada casa do tabuleiro de xadrez,

se na primeira casa colocar 1 grão, na segunda — 2 grãos, na terceira — 4 grãos e assim por diante.

No total, o tabuleiro de xadrez tem 64 casas.

Use o loop for e a função range() para iterar pelas casas e a função print() para exibir o resultado.

Exemplo:'''
for i in range(64):
    grains = 2 ** i
    print(f"Casa {i + 1}: {grains} grãos")