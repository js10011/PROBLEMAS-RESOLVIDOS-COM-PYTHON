
palavra = input("Digite uma palavra: ").lower()
vogais = 'aeiou'
contador_total = 0
contagem_vogais = {vogal: 0 for vogal in vogais}  # dicionário pra contar cada vogal

for letra in palavra:
    if letra in vogais:
        contador_total += 1
        contagem_vogais[letra] += 1

print(f"A palavra '{palavra}' tem {contador_total} vogais.")

# Mostra a contagem de cada vogal
for vogal, qtd in contagem_vogais.items():
    if qtd > 0:
        print(f"'{vogal}' aparece {qtd} vez(es).")
