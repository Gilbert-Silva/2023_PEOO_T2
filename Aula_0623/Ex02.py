import enum

class Estacao(enum.Enum):
  OUTONO = 1
  INVERNO = 2
  PRIMAVERA = 3
  VERAO = 4

a = Estacao.VERAO
print(a)

class Dia(enum.IntFlag):
  Domingo = 1   # 0000.0001
  Segunda = 2   # 0000.0010
  Terca = 4     # 0000.0100
  Quarta = 8    # 0000.1000
  Quinta = 16   # 0001.0000
  Sexta = 32    # 0010.0000
  Sabado = 64   # 0100.0000

x = Dia.Segunda
print(x)
aulas = Dia.Segunda | Dia.Sexta # 0010.0010
print(aulas)


