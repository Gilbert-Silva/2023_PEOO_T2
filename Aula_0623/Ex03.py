import datetime


class Paciente:

  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc

  def __str__(self):
    return f"{self.__nome} - {self.__nasc}"


print("Informe seu nome")
nome = input()
print("Informe sua data de nascimento dd/mm/aaaa")
data = input()
dia, mes, ano = map(int, data.split("/"))
f1 = datetime.datetime(ano, mes, dia)
f2 = datetime.datetime.strptime(data, "%d/%m/%Y")
p1 = Paciente(nome, f1)
p2 = Paciente(nome, f2)
print(p1)
print(p2)
