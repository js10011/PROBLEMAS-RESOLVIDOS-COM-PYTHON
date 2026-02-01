'''Escreva um programa que leia dois arquivos Excel com a mesma estrutura de dados (tendo colunas "Product" e "Sales") e combine seu conteúdo em um único DataFrame. Exiba o resultado na tela.'''
import pandas as pd

# Leitura dos dados de dois arquivos Excel
file1 = 'data1.xlsx'
file2 = 'data2.xlsx'

# Ler arquivos Excel no DataFrame
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Combinação de DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Exibição do DataFrame combinado
print(combined_df)

'''Escreva um programa que leia dados de todas as folhas de um arquivo Excel e os una em um único DataFrame. Cada folha contém dados de vendas, incluindo as colunas "Product", "Sales" e "Month". Mostre os resultados na tela.'''
import pandas as pd

# Leitura de dados de todas as folhas do arquivo Excel
file_path = 'sales_data.xlsx'  # Especifique o caminho para o seu arquivo Excel
all_sheets_data = pd.read_excel(file_path, sheet_name=None)

# Unindo dados de todas as folhas em um único DataFrame
combined_data = pd.concat(all_sheets_data.values(), ignore_index=True)

# Exibição do DataFrame unido na tela
print(combined_data)

'''Escreva um programa que une dados de dois arquivos Excel distintos. Um arquivo contém informações de vendas ("Product", "Sales"), e o outro contém informações de preços ("Product", "Price"). Una os dados pela coluna "Product" e exiba o DataFrame final na tela, utilizando o tipo de união "inner".'''
import pandas as pd

# Leitura de dados de arquivos Excel
sales_data = pd.read_excel('sales.xlsx')
price_data = pd.read_excel('prices.xlsx')

# União de dados pela coluna "Product" usando o método "inner"
merged_data = pd.merge(sales_data, price_data, on='Product', how='inner')

# Exibição do DataFrame final na tela
print(merged_data)

'''Escreva um programa que localize automaticamente todos os arquivos Excel no diretório especificado com o padrão de nome "sales_data_*.xlsx". O programa deve unificar todos os arquivos em um único DataFrame e adicionar a coluna "Source File", indicando o nome do arquivo de origem para cada linha de dados. Exiba o resultado na tela'''
import pandas as pd
import os
from glob import glob

# Caminho para o diretório com arquivos Excel
directory_path = 'path_to_directory' # Substitua pelo seu caminho

# Padrão para localização de arquivos
file_pattern = os.path.join(directory_path, 'sales_data_*.xlsx')

# Encontramos todos os arquivos que correspondem ao padrão
excel_files = glob(file_pattern)

# Lista para armazenar dados de todos os arquivos
dataframes = []

# Processamos cada arquivo encontrado
for file_path in excel_files:
    # Lemos dados do arquivo Excel atual
    df = pd.read_excel(file_path)
    # Adicionamos a coluna com o nome do arquivo
    df['Source File'] = os.path.basename(file_path)
    # Adicionamos o DataFrame na lista
    dataframes.append(df)

# Unificamos todos os DataFrames em um só
combined_df = pd.concat(dataframes, ignore_index=True)

# Exibimos o resultado
print(combined_df)