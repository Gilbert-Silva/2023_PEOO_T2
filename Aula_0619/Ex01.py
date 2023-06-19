import datetime

x = datetime.datetime(2023, 6, 19)
print(x)
y = datetime.timedelta(days=4, hours=9)
print(y)
prox_aula = x + y
print(prox_aula)
print(prox_aula.weekday())

print(prox_aula.strftime("%A, %d. %B %Y %I:%M%p"))

print(prox_aula.strftime("%d/%m/%y"))
print(prox_aula.strftime("%d/%m/%Y"))
print(prox_aula.strftime("%d/%B/%Y"))

hoje = datetime.datetime.today()
print(hoje)

prova = datetime.datetime(2023, 7, 3, hour=13, minute=30)
print(prova)

tempo = prova - hoje
print(tempo)


