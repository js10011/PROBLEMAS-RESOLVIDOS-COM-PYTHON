'''Crie um DataFrame com informações sobre produtos, contendo as colunas: 'Categoria', 'Preço' e 'Quantidade'. Usando o método groupby, agrupe os dados por categoria e calcule o preço total dos produtos em cada categoria. O programa deve exibir o preço total dos produtos para cada categoria.'''
import pandas as pd  

# Criamos o DataFrame com informações sobre os produtos  
data = {  
    'Categoria': ['Produtos', 'Limpeza', 'Produtos', 'Roupas', 'Roupas'],  
    'Preço': [120, 300, 150, 500, 400],  
    'Quantidade': [1, 2, 3, 1, 2]  
}  

df = pd.DataFrame(data)  

# Agrupamos os dados por categoria e calculamos o preço total dos produtos  
total_price_per_category = df.groupby('Categoria')['Preço'].sum()  

# Exibimos os resultados  
print(total_price_per_category)

'''Usando pandas, crie um DataFrame com dados sobre transações, 
contendo as colunas: 'Categoria', 'Valor da Transação' e 'Número de Transações'. Agrupe os dados por 
categoria e calcule cada uma das seguintes funções agregadas: soma, média e valor máximo do valor da transação para cada categoria. O programa deve exibir 
os resultados das funções agregadas para cada categoria.'''

import pandas as pd

# Criamos um DataFrame com dados sobre transações
data = {
    'Categoria': ['Alimentos', 'Alimentos', 'Roupas', 'Roupas', 'Eletrônicos', 'Eletrônicos'],
    'Valor da Transação': [150, 200, 500, 250, 400, 600],
    'Número de Transações': [1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Agrupamos os dados por 'Categoria' e calculamos as funções agregadas
grouped = df.groupby('Categoria').agg({
    'Valor da Transação': ['sum', 'mean', 'max']
})

# Exibimos os resultados
for category, row in grouped.iterrows():
    print(f"Categoria: {category}")
    print(f"  Soma: {row[('Valor da Transação', 'sum')]}")
    print(f"  Média: {row[('Valor da Transação', 'mean')]}")
    print(f"  Máximo: {row[('Valor da Transação', 'max')]}")
    print()

'''Prepare um DataFrame contendo dados de vendas com as colunas: 'Loja', 'Categoria', 'Receita'. Realize o agrupamento por duas colunas: 'Loja' e 'Categoria', e calcule a receita total e média para cada combinação. Exiba os resultados do agrupamento na tela para ver os totais para cada loja e cada categoria.'''
import pandas as pd

# Criando DataFrame com dados de vendas
data = {
    'Loja': ['Loja A', 'Loja A', 'Loja B', 'Loja C', 'Loja C', 'Loja B', 'Loja A'],
    'Categoria': ['Eletrônicos', 'Roupas', 'Roupas', 'Eletrônicos', 'Roupas', 'Eletrônicos', 'Roupas'],
    'Receita': [200, 150, 300, 400, 200, 500, 100]
}

df = pd.DataFrame(data)

# Agrupando dados pelas colunas 'Loja' e 'Categoria'
grouped = df.groupby(['Loja', 'Categoria']).agg({
    'Receita': ['sum', 'mean']
}).reset_index()

# Renomeando colunas para melhor leitura
grouped.columns = ['Loja', 'Categoria', 'Receita Total', 'Receita Média']

# Exibindo resultados do agrupamento na tela
print(grouped)

'''Usando os dados de vendas de produtos em um DataFrame contendo as colunas: 'Produto', 'Região', 'Vendas', realize a agregação dos dados por região e produto. Calcule as vendas totais para cada produto em cada região. Em seguida, crie uma visualização do resultado usando o Matplotlib (por exemplo, um gráfico de barras) para representar de maneira visual as vendas dos produtos por região. O programa deve exibir um gráfico de barras com as vendas totais de produtos em várias regiões.'''
import pandas as pd  
import matplotlib.pyplot as plt  

# Exemplo de dados de vendas  
data = {  
    'Produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C', 'Produto B', 'Produto C'],  
    'Região': ['Região 1', 'Região 2', 'Região 1', 'Região 2', 'Região 1', 'Região 2'],  
    'Vendas': [150, 200, 100, 300, 250, 400]  
}  

# Criando o DataFrame  
df = pd.DataFrame(data)  

# Agrupando os dados por 'Região' e 'Produto', calculando as vendas totais  
grouped_data = df.groupby(['Região', 'Produto'])['Vendas'].sum().unstack()  

# Criando o gráfico de barras  
grouped_data.plot(kind='bar', stacked=True)  

# Configurações do gráfico  
plt.title('Vendas totais de produtos por região')  
plt.xlabel('Região')  
plt.ylabel('Vendas totais')  
plt.legend(title='Produtos')  
plt.tight_layout()  

# Exibindo o gráfico na tela  
plt.show()