'''Use pandas para criar uma tabela dinâmica a partir de um conjunto de dados de vendas. Você tem os seguintes dados:

```
data = {

'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],

'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],

'Vendas': [150, 200, 250, 130, 180, 210]

}

```
Crie um DataFrame e monte uma tabela dinâmica para mostrar o total de vendas de cada produto em cada mês.'''
import pandas as pd

# Dados originais
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

# Criação do DataFrame a partir dos dados
df = pd.DataFrame(data)

# Criação da tabela dinâmica
pivot_table = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='sum', fill_value=0)

# Exibição da tabela dinâmica
print(pivot_table)

'''Usando a biblioteca pandas, crie um DataFrame para analisar os dados de vendas. Você tem os seguintes dados:

```

data = {

'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],

'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],

'Vendas': [150, 200, 250, 130, 180, 210]

}

```

Crie um DataFrame e forme duas tabelas pivot:

1. Tabela com a média das vendas para cada produto em cada mês.

2. Tabela com a quantidade de unidades vendidas para cada produto em cada mês.

Use as funções de agregação mean e count para os cálculos.'''

import pandas as pd

# Criação do DataFrame a partir do dicionário fornecido
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

df = pd.DataFrame(data)

# Criação da tabela pivot com a média das vendas para cada produto em cada mês
mean_sales = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='mean')

# Criação da tabela pivot com a quantidade de unidades vendidas para cada produto em cada mês
count_sales = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='count')

# Exibição dos resultados
print("Média das vendas para cada produto em cada mês:")
print(mean_sales)
print("\nQuantidade de unidades vendidas para cada produto em cada mês:")
print(count_sales)

'''Usando a biblioteca pandas, crie um DataFrame com base nos seguintes dados de vendas:

```

data = {

'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],

'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],

'Vendas': [150, 200, 250, 130, 180, 210]

}

```

Usando o método crosstab, crie uma tabela que mostre o total de vendas para cada produto por mês. Na tabela, as linhas devem representar produtos e as colunas devem representar meses. Exiba o resultado em forma de tabela, onde as células contêm o total de vendas para cada produto em cada mê'''
import pandas as pd

# Criamos o DataFrame com base nos dados de vendas
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

df = pd.DataFrame(data)

# Usamos o crosstab para calcular o total de vendas por produtos e meses
result = pd.crosstab(index=df['Produto'], columns=df['Mês'], values=df['Vendas'], aggfunc='sum')

# Exibimos a tabela na tela
print(result)

'''Você tem dados de vendas que incluem a coluna "Ano". Usando a biblioteca pandas, crie um DataFrame com base nos seguintes dados:

```

data = {

'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],

'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],

'Vendas': [150, 200, 250, 130, 180, 210],

'Ano': [2023, 2023, 2023, 2024, 2024, 2024]

}

```

Crie uma tabela dinâmica que mostre o número total de vendas para cada produto em cada mês e ano. Adicione uma linha "Total" para mostrar o valor total das vendas. Use índices multidimensionais e a opção de margens.'''
import pandas as pd

# Criando DataFrame a partir do dicionário fornecido data
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210],
    'Ano': [2023, 2023, 2023, 2024, 2024, 2024]
}
df = pd.DataFrame(data)

# Usando pivot_table para criar a tabela dinâmica
pivot_table = pd.pivot_table(
    df, 
    values='Vendas', 
    index=['Produto', 'Ano'], 
    columns='Mês', 
    aggfunc='sum',
    margins=True,  # Adicionando a linha "Total" para o valor total das vendas
    margins_name='Total'  # Nomeando a linha de totais
)

# Exibindo a tabela dinâmica resultante
print(pivot_table)