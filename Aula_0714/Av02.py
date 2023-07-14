import datetime

class Oferta:
  def __init__(self, loja, data, preco): # 10
    self.__loja  = loja
    self.__data = data
    self.__preco = preco
  def set_loja(self, loja): # 10
    self.__loja = loja
  def set_data(self, data):
    self.__data = data
  def set_preco(self, preco):  
    self.__preco = preco
  def get_loja(self):
    return self.__loja
  def get_data(self):
    return self.__data
  def get_preco(self):
    return self.__preco
  def __str__(self): # 10
    return f"{self.__loja} {self.__data.date()} - {self.__preco:.2f}"

class Produto:
  def __init__(self, nome, fabricante):  # 10
    self.__nome = nome
    self.__fabricante = fabricante
    self.__ofertas = []
  def inserir(self, o): # 10
    self.__ofertas.append(o)
  def listar(self):     # 10
    return self.__ofertas
  def preco_medio(self):    # 10
    if len(self.__ofertas) == 0: return 0
    total = 0
    for oferta in self.__ofertas: # 10
      total += oferta.get_preco()
    return total / len(self.__ofertas) 
  def ofertas_do_dia(self):
    r = []
    for oferta in self.__ofertas:
      if oferta.get_data().date() == datetime.datetime.today().date():
        r.append(oferta)
    return r
    
a = Oferta("Amazon", datetime.datetime.today(), 50)  # 5
b = Oferta("Miranda", datetime.datetime(2023, 6, 14), 55)
c = Oferta("Kabum", datetime.datetime(2023, 5, 14), 45)
m = Produto("Mouse", "Logitech") # 5
m.inserir(a) # 10
m.inserir(b)
m.inserir(c)
print("Ofertas")
for oferta in m.listar():
  print(oferta)
print("\nPreço Médio")
print(m.preco_medio())
print("\nOfertas de Hoje")
for oferta in m.ofertas_do_dia():
  print(oferta)

