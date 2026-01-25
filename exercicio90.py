'''Escreva um programa que crie um DataFrame com dados de estudantes, incluindo seus nomes, idades e médias de notas. Filtre todos os estudantes com mais de 20 anos e exiba o DataFrame resultante na tela.'''
import pandas as pd

# Criamos dados sobre os estudantes
data = {
    'Nome': ['Alexei', 'Maria', 'Ivan', 'Ana', 'Sergio'],
    'Idade': [19, 22, 21, 20, 23],
    'Média de Notas': [4.5, 4.0, 3.8, 4.2, 3.9]
}

# Criamos o DataFrame
df = pd.DataFrame(data)

# Filtramos os estudantes com mais de 20 anos
filtered_df = df[df['Idade'] > 20]

# Exibimos o DataFrame filtrado
print(filtered_df)

'''Crie um DataFrame com dados sobre produtos em uma loja, incluindo o nome do produto, categoria, quantidade e preço. Filtre todos os produtos que pertencem à categoria "frutas" e têm quantidade maior que 10. Exiba o resultado.'''
import pandas as pd

# Criação do DataFrame
data = {
    'nome do produto': ['maçãs', 'bananas', 'pepinos', 'peras', 'tomates'],
    'categoria': ['frutas', 'frutas', 'vegetais', 'frutas', 'vegetais'],
    'quantidade': [5, 15, 7, 12, 9],
    'preço': [50, 30, 20, 45, 25]
}

df = pd.DataFrame(data)

# Filtragem por categoria "frutas" e quantidade maior que 10
filtered_df = df[(df['categoria'] == 'frutas') & (df['quantidade'] > 10)]

# Exibição dos dados filtrados
print(filtered_df)

'''Crie um DataFrame com dados sobre os funcionários de uma empresa, incluindo seu nome, departamento e salário. Primeiro, ordene os dados pelo departamento e depois pelo salário em ordem decrescente. Exiba o DataFrame ordenado na tela.'''
import pandas as pd

# Criamos o DataFrame com dados sobre os funcionários
data = {
    'Nome': ['Anna', 'Boris', 'Victor', 'Georgiy', 'Dmitriy'],
    'Departamento': ['Vendas', 'Marketing', 'Vendas', 'Desenvolvimento', 'Marketing'],
    'Salário': [70000, 60000, 80000, 75000, 65000]
}

df = pd.DataFrame(data)

# Ordenamos o DataFrame primeiro por departamento, depois por salário em ordem decrescente
sorted_df = df.sort_values(by=['Departamento', 'Salário'], ascending=[True, False])

# Exibimos o DataFrame ordenado na tela
print(sorted_df)

'''Escreva um programa que crie um DataFrame com dados sobre vendas de carros, incluindo a marca, o modelo, o número de unidades vendidas e a receita gerada pelas vendas. Filtre todos os carros cuja quantidade de unidades vendidas seja maior que 50 e ordene-os pela receita em ordem crescente. Exiba o resultado na tela.'''
import pandas as pd

# Criando os dados sobre vendas de carros
data = {
    'Marca': ['Toyota', 'Ford', 'BMW', 'Mercedes', 'Honda'],
    'Modelo': ['Camry', 'Focus', 'X5', 'C-Class', 'Civic'],
    'Unidades Vendidas': [60, 30, 80, 45, 90],
    'Receita Gerada': [24000, 15000, 30000, 35000, 27000]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Filtrando os carros cuja quantidade de unidades vendidas seja maior que 50
filtered_df = df[df['Unidades Vendidas'] > 50]

# Ordenando o DataFrame filtrado pela receita em ordem crescente
sorted_filtered_df = filtered_df.sort_values(by='Receita Gerada')

# Exibindo o resultado na tela
print(sorted_filtered_df)