'''Escreva um programa que crie três DataFrames com dados de vendas para diferentes trimestres: o primeiro na planilha "Primeiro trimestre", o segundo - "Segundo trimestre", o terceiro - "Terceiro trimestre". Cada DataFrame deve conter as colunas "Produto", "Quantidade" e "Lucro". Grave todos os três DataFrames em um único arquivo Excel com o nome "quarterly_sales.xlsx".'''
import pandas as pd

# Criamos dados para cada trimestre
data_first_quarter = {
    "Produto": ["Produto A", "Produto B", "Produto C"],
    "Quantidade": [100, 150, 200],
    "Lucro": [1000, 1500, 2000]
}

data_second_quarter = {
    "Produto": ["Produto D", "Produto E", "Produto F"],
    "Quantidade": [110, 160, 210],
    "Lucro": [1100, 1600, 2100]
}

data_third_quarter = {
    "Produto": ["Produto G", "Produto H", "Produto I"],
    "Quantidade": [120, 170, 220],
    "Lucro": [1200, 1700, 2200]
}

# Criamos DataFrame para cada trimestre
df_first_quarter = pd.DataFrame(data_first_quarter)
df_second_quarter = pd.DataFrame(data_second_quarter)
df_third_quarter = pd.DataFrame(data_third_quarter)

# Escrevemos DataFrames no arquivo Excel em diferentes planilhas
with pd.ExcelWriter('quarterly_sales.xlsx') as writer:
    df_first_quarter.to_excel(writer, sheet_name='Primeiro trimestre', index=False)
    df_second_quarter.to_excel(writer, sheet_name='Segundo trimestre', index=False)
    df_third_quarter.to_excel(writer, sheet_name='Terceiro trimestre', index=False)

'''Crie um programa que coleta dados de temperatura e umidade de duas fontes diferentes por uma semana. Em seguida, combine esses dados em um único DataFrame. Grave o DataFrame resultante em um arquivo Excel chamado "climate_reports.xlsx". Estruture o arquivo de forma que os dados sejam apresentados em folhas separadas para cada dia da semana.'''
import pandas as pd
from random import randint

# Geração de dados de teste para temperatura e umidade
def generate_data():
    return {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'temperature_source_1': [randint(20, 30) for _ in range(7)],
        'humidity_source_1': [randint(50, 70) for _ in range(7)],
        'temperature_source_2': [randint(20, 30) for _ in range(7)],
        'humidity_source_2': [randint(50, 70) for _ in range(7)]
    }

# Combinação dos dados
def combine_data():
    data = generate_data()
    df = pd.DataFrame(data)
    return df

# Registro do DataFrame em Excel com folhas separadas por dias
def write_to_excel(df):
    with pd.ExcelWriter('climate_reports.xlsx') as writer:
        for day in df['day']:
            day_data = df[df['day'] == day]
            day_data.to_excel(writer, sheet_name=day, index=False)

# Código principal
df = combine_data()
write_to_excel(df)