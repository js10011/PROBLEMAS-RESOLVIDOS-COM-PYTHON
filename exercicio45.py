
'''Escreva um programa que solicite ao usuário a data de seu nascimento (ano, mês e dia),

e então exiba a quantidade de dias que passaram desde essa data até o dia de hoje.

O programa deve:

Solicitar ao usuário o ano, mês e dia de seu nascimento.

Criar um objeto de data de nascimento usando a classe datetime.date.

Obter a data atual usando o método today().

Calcular a diferença entre a data atual e a data de nascimento.'''
from datetime import date

# Solicitamos ao usuário o ano, mês e dia de nascimento
year = int(input("Digite o ano do seu nascimento: "))
month = int(input("Digite o mês do seu nascimento: "))
day = int(input("Digite o dia do seu nascimento: "))

# Criamos um objeto de data de nascimento
birth_date = date(year, month, day)

# Obtemos a data atual
current_date = date.today()

# Calculamos a diferença entre a data atual e a data de nascimento
days_difference = (current_date - birth_date).days

'''Escreva um programa que converta o horário atual do fuso horário UTC para um fuso horário especificado pelo usuário.

O programa deve:

Obter a hora atual no fuso horário UTC.

Solicitar ao usuário o deslocamento em horas em relação ao UTC.

Criar um objeto de fuso horário com o deslocamento especificado.

Converter a hora atual para o fuso horário especificado.

Exibir a hora atual no UTC e no fuso horário especificado.'''
from datetime import datetime, timedelta, timezone

# Obter a hora atual no fuso horário UTC
current_utc_time = datetime.now(timezone.utc)

# Solicitar ao usuário o deslocamento em horas em relação ao UTC
offset_hours = int(input("Digite o deslocamento em relação ao UTC em horas: "))

# Criar um objeto de fuso horário com o deslocamento especificado
user_timezone = timezone(timedelta(hours=offset_hours))

# Converter a hora atual para o fuso horário especificado
current_user_time = current_utc_time.astimezone(user_timezone)

# Exibir a hora atual no UTC e no fuso horário especificado pelo usuário
print("Hora atual no UTC:", current_utc_time)
print(f"Hora atual no fuso horário com deslocamento de {offset_hours} hora(s):", current_user_time)