import datetime
class Amigo:
  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc
  def get_nasc(self):
    return self.__nasc
  def get_nome(self):
    return self.__nome
  def __gt__(self, outro):
    return self.__nasc > outro.__nasc
  def __str__(self):
    return f"{self.__nome} - {self.__nasc}"

x = [ 5, 4, 2, 1, 3 ]
x.sort()
print(x)

y = []
data1 = datetime.datetime(2006, 4, 17)
y.append(Amigo("Matheus", data1))
data2 = datetime.datetime(2006, 6, 5)
y.append(Amigo("Murillo", data2))

y.sort()
print(*y)


