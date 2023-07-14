import datetime

class Lote:
  def __init__(self, num, venc, qtd): # 10
    self.__numero = num
    self.__vencimento = venc
    self.__qtd = qtd
  def set_numero(self, num): # 10
    self.__numero = num
  def set_vencimento(self, venc):
    self.__vencimento = venc
  def set_quantidade(self, qtd):  
    self.__qtd = qtd
  def get_numero(self):
    return self.__numero
  def get_vencimento(self):
    return self.__vencimento
  def get_quantidade(self):
    return self.__qtd
  def __str__(self): # 10
    return f"{self.__numero} {self.__vencimento.date()} - {self.__qtd}"

class Medicamento:
  def __init__(self, nome, indicacao):  # 10
    self.__nome = nome
    self.__indicacao = indicacao
    self.__lotes = []
  def inserir(self, l): # 10
    self.__lotes.append(l)
  def listar(self):     # 10
    return self.__lotes
  def estoque(self):    # 10
    total = 0
    for lote in self.__lotes: # 10
      total += lote.get_quantidade()
    return total
  def vencidos(self):
    r = []
    for lote in self.__lotes:
      if lote.get_vencimento().date() < datetime.datetime.today().date():
        r.append(lote)
    return r
    
a = Lote("100", datetime.datetime.today(), 10)  # 5
b = Lote("200", datetime.datetime(2023, 6, 14), 20)
c = Lote("300", datetime.datetime(2023, 5, 14), 5)
m = Medicamento("Dipirona", "Dor e Febre") # 5
m.inserir(a) # 10
m.inserir(b)
m.inserir(c)
print("Lotes")
for lote in m.listar():
  print(lote)
print("\nEstoque")
print(m.estoque())
print("\nVencidos")
for lote in m.vencidos():
  print(lote)

