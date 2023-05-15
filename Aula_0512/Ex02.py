class Triangulo:
  def __init__(self):
    self.__b = 0
    self.__h = 0
  def get_base(self):
    return self.__b
  def set_base(self, v):
    if v >= 0: self.__b = v
    else: raise ValueError()  

class UI:
  @staticmethod
  def main():
    while UI.menu() != 2:
      x = Triangulo()
      #print(x.__b)
      print(x.get_base())
      x.set_base(10)
      print(x.get_base())
    print("Até logo")
    
  @staticmethod
  def menu():
    print("Digite 1 para novo triangulo")
    print("Digite 2 para sair")
    return int(input())

UI.main()
