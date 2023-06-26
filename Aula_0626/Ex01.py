import datetime

class Amigo:
  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc
  def __str__(self):
    return f"{self.__nome} - {self.__nasc}"

# Ler dados de 10 amigos e mostrar o mais novo
# Para ler uma data do usuário
# data = datetime.datetime.strptime(input(), "%d/%m/%Y")
