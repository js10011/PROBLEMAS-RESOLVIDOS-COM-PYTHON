'''Escreva um programa que crie um dicionário com dados de receitas e despesas por semana no formato: {"Segunda-feira": 100, "Terça-feira": 150, ..., "Domingo": 200}. O programa deve calcular o lucro total da semana e o lucro médio diário, exibindo os resultados na tela.'''
# Dicionário com dados de receitas e despesas para cada dia da semana
week_financials = {
    "Segunda-feira": 100,
    "Terça-feira": 150,
    "Quarta-feira": 200,
    "Quinta-feira": 250,
    "Sexta-feira": 300,
    "Sábado": 200,
    "Domingo": 200
}

# Cálculo do lucro total da semana
total_profit = sum(week_financials.values())

# Cálculo do lucro médio diário
average_daily_profit = total_profit / 7

# Exibição dos resultados
print("Lucro total da semana:", total_profit)
print("Lucro médio diário:", average_daily_profit)

'''Você tem um arquivo de texto data.txt que contém linhas com valores numéricos (por exemplo, "120\n 85\n 90\n ..."). Escreva um script em Python que lê os dados deste arquivo, calcula sua soma e média, e em seguida salva os resultados em um novo arquivo report.txt no formato: "Soma: X, Média: Y"'''
def calculate_and_report(input_file, output_file):
    # Abre o arquivo de entrada para leitura
    with open(input_file, 'r') as file:
        # Lê cada linha do arquivo, remove espaços desnecessários e verifica se a linha é um número
        # Se a linha for um número, converte-a para int e adiciona à lista numbers
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

    # Calcula a soma dos números na lista numbers
    total_sum = sum(numbers)
    # Calcula a média; se a lista estiver vazia, define a média como 0
    average = total_sum / len(numbers) if numbers else 0

    # Abre o arquivo de saída para escrever o relatório
    with open(output_file, 'w') as report:
        # Escreve no arquivo a linha com a soma e a média
        report.write(f"Soma: {total_sum}, Média: {average}")

# Executa a função com os nomes especificados do arquivo de entrada e saída
calculate_and_report('data.txt', 'report.txt')