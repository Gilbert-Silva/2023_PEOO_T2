class Agua:
  def __init__(self, mes, ano, consumo):
    self.__mes = 1              # init - 5
    self.__ano = 2023           # set  - 5
    self.__consumo = 10         # validação - 5
    self.set_mes(mes)           # get - 5
    self.set_ano(ano)           # valor - 5
    self.set_consumo(consumo)   # str - 5
  def set_mes(self, mes):       # atributos - 5
    if 1 <= mes <= 12: self.__mes = mes
    else: raise ValueError()
  def set_ano(self, ano):
    if ano >= 2000: self.__ano = ano
    else: raise ValueError()
  def set_consumo(self, consumo):
    if consumo >= 0: self.__consumo = consumo
    else: raise ValueError()
  def get_mes(self):
    return self.__mes
  def get_ano(self):
    return self.__ano
  def get_consumo(self):
    return self.__consumo
  def valor(self):
    if self.__consumo <= 10: return 38
    if self.__consumo <= 20: return 38 + (self.__consumo - 10) * 5
    return 38 + 50 + (self.__consumo - 10) * 6
  def __str__(self):
    return f"Conta de água {self.__mes}/{self.__ano} - consumo: {self.__consumo}"

class UI:
  def main():
    m = int(input("Informe o mês da conta: "))      # input - 5
    a = int(input("Informe o ano da conta: "))
    c = int(input("Informe o consumo da conta: "))
    x = Agua(m, a, c)                               # objeto - 5
    print(x.valor())                                # valor - 5 
    print(x)
    
   


UI.main() 
 
      
    