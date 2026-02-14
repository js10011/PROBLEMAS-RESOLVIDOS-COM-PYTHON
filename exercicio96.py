'''Crie um DataFrame que contenha informações sobre os funcionários da empresa: nome, cargo e departamento. Exporte este DataFrame para um arquivo Excel com o nome 'employees.xlsx', sem índices.'''
import pandas as pd

# Criamos dados sobre os funcionários
data = {
    'Nome': ['Ivan', 'Maria', 'Pedro', 'Ana'],
    'Cargo': ['Engenheiro', 'Marketing', 'Analista', 'Gerente'],
    'Departamento': ['Desenvolvimento', 'Marketing', 'Análise', 'Gestão']
}

# Criamos o DataFrame
df = pd.DataFrame(data)

# Exportamos o DataFrame para um arquivo Excel sem índices
df.to_excel('employees.xlsx', index=False)

'''Crie um DataFrame contendo dados de produtos: nome, preço e quantidade em estoque. Exporte o DataFrame para o Excel com a largura das colunas ajustada automaticamente ao conteúdo dos dados. Nomeie o arquivo como 'products.xlsx'.'''
import pandas as pd

# Dados dos produtos
products_data = {
    "nome": ["Produto A", "Produto B", "Produto C"],
    "preço": [23.5, 45.2, 12.0],
    "quantidade em estoque": [10, 5, 20]
}

# Criação do DataFrame
df = pd.DataFrame(products_data)

# Gravação do DataFrame no Excel com ajuste automático da largura das colunas
with pd.ExcelWriter('products.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    
    # Ajuste da largura das colunas de acordo com o conteúdo dos dados
    for column in df:
        max_len = max(
            df[column].astype(str).map(len).max(),  # comprimento do valor mais longo na coluna
            len(column)  # comprimento do cabeçalho da coluna
        )
        col_idx = df.columns.get_loc(column)  # índice da coluna atual
        worksheet.set_column(col_idx, col_idx, max_len + 2)  # ajusta a largura da coluna

'''Crie dois DataFrames com dados de vendas para os anos de 2022 e 2023: mês, valor das vendas. Exporte os dados para um arquivo Excel com duas planilhas diferentes, nomeadas 'Sales_2022' e 'Sales_2023'. Nomeie o arquivo como 'annual_sales.xlsx'. Os índices não devem ser incluídos na exportação.'''
import pandas as pd

# Criando dados de vendas para o ano de 2022
data_2022 = {
    'mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'valor das vendas': [10000, 15000, 20000, 25000, 30000, 35000, 
                         40000, 45000, 50000, 55000, 60000, 65000]
}

# Criando dados de vendas para o ano de 2023
data_2023 = {
    'mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'valor das vendas': [11000, 16000, 21000, 26000, 31000, 36000, 
                         41000, 46000, 51000, 56000, 61000, 66000]
}

# Criando DataFrame a partir dos dados de vendas
df_2022 = pd.DataFrame(data_2022)
df_2023 = pd.DataFrame(data_2023)

# Exportando dados para um arquivo Excel com duas planilhas
with pd.ExcelWriter('annual_sales.xlsx', engine='xlsxwriter') as writer:
    df_2022.to_excel(writer, sheet_name='Sales_2022', index=False)
    df_2023.to_excel(writer, sheet_name='Sales_2023', index=False)

'''Crie um DataFrame contendo os seguintes dados sobre os resultados dos alunos: nome do aluno, disciplina, nota. Exporte os dados para um arquivo Excel com a largura das colunas correspondendo ao conteúdo. Adicione uma folha adicional no arquivo com o título 'Summary', onde você deve registrar o total de alunos, a nota média e a quantidade de disciplinas. Nomeie o arquivo como 'student_report.xlsx'. '''

import pandas as pd
from pandas import ExcelWriter

# Dados sobre os resultados dos alunos
data = {
    'nome do aluno': ['Alexey', 'Maria', 'Ivan', 'Olga', 'Svetlana'],
    'disciplina': ['Matemática', 'Física', 'Química', 'Literatura', 'Biologia'],
    'nota': [5, 4, 3, 5, 4]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Cálculo das estatísticas necessárias
total_students = df['nome do aluno'].nunique()
average_grade = df['nota'].mean()
unique_subjects = df['disciplina'].nunique()

# Criação da folha adicional 'Summary'
summary_data = {
    'Total de alunos': [total_students],
    'Nota média': [average_grade],
    'Quantidade de disciplinas': [unique_subjects]
}

summary_df = pd.DataFrame(summary_data)

# Exportação para Excel
with ExcelWriter('student_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Students', index=False)
    summary_df.to_excel(writer, sheet_name='Summary', index=False)

    # Ajuste automático da largura das colunas
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        for column in worksheet.columns:
            max_length = 0
            column = [cell for cell in column]
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column[0].column_letter].width = adjusted_width