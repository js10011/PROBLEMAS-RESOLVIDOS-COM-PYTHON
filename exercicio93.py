'''Crie um DataFrame 
contendo 5 linhas com dados de funcionários, incluindo valores ausentes e registros duplicados. Escreva um programa que remova todas as linhas que contêm pelo menos um valor vazio e mantenha apenas registros únicos. O programa deve 
exibir o DataFrame após a limpeza.'''
import pandas as pd

# Criamos um DataFrame com 5 linhas, incluindo valores ausentes e duplicatas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob'],
    'Age': [25, 30, None, 45, 30],
    'Department': ['HR', 'IT', 'Finance', None, 'IT']
}

df = pd.DataFrame(data)

# Removemos as linhas com valores vazios
df = df.dropna()

# Removemos duplicatas
df = df.drop_duplicates()

# Exibimos o DataFrame limpo
print(df)

'''Crie um DataFrame com dados de vendas de 
produtos, contendo 7 linhas, onde alguns valores na coluna "Quantidade" estão ausentes. Escreva um programa que substitua os valores ausentes pela média da coluna "Quantidade". 
O programa deve exibir o DataFrame formatado.'''
import pandas as pd
import numpy as np

# Criamos o DataFrame com valores ausentes na coluna "Quantidade"
data = {
    'Produto': ['Produto1', 'Produto2', 'Produto3', 'Produto4', 'Produto5', 'Produto6', 'Produto7'],
    'Quantidade': [10, np.nan, 15, np.nan, 20, np.nan, 25]
}

df = pd.DataFrame(data)

# Calculamos a média da coluna "Quantidade"
average_quantity = df['Quantidade'].mean()

# Substituímos os valores ausentes pela média
df['Quantidade'].fillna(average_quantity, inplace=True)

# Exibimos o DataFrame formatado
print(df)

'''Crie um DataFrame contendo 
datas no formato de string e dados numéricos gravados como texto. Escreva um programa que converta strings no formato 'dd-mm-yyyy' em um objeto do tipo datetime, e números em texto para formato numérico. O programa deve exibir o DataFrame 
atualizado com os tipos de dados corretos.
'''
import pandas as pd

# Criamos DataFrame com datas no formato string e valores numéricos como texto
data = {
    'dates': ['01-01-2020', '15-08-2021', '23-11-2022'],
    'numbers': ['10', '20', '30']
}
df = pd.DataFrame(data)

# Convertendo a coluna de datas para o formato datetime
df['dates'] = pd.to_datetime(df['dates'], format='%d-%m-%Y')

# Convertendo a coluna de números em texto para formato numérico
df['numbers'] = pd.to_numeric(df['numbers'])

# Exibindo o DataFrame atualizado
print(df)