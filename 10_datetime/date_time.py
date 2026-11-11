# Data e Hora

# O que aprender:
# - módulo datetime
# - date / time / timedelta
# - formatação

# Escreve aqui os teus testes:

from datetime import datetime
agora = datetime.now()
print(agora)

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
