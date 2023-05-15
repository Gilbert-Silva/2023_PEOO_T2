class Triangulo:   # entidade
  def __init__(self):
    self.__b = 10  # encapsulamento
    self.__h = 20
  def set_base(self, b):
    if (b > 0): self.__b = b
    else: raise ValueError()  
  def set_altura(self, h):
    if (h > 0): self.__h = h
    else: raise ValueError() 
  def get_base(self):
    return self.__b
  def get_altura(self):
    return self.__h
  def calc_area(self):
    area = self.__b * self.__h / 2
    return area

class UI:
  @staticmethod
  def main():
    x = Triangulo()
    print(x.get_base())
    print(x.get_altura())
    print(x.calc_area())  # calc_area(x)
    
    y = Triangulo()
    #y.b = 40
    y.set_base(40)        # set_base(y, 40)
    #y.h = 30
    y.set_altura(30)
    #print(y.b)
    #print(y.h)
    print(y.calc_area())  # calc_area(y)

    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    z = Triangulo()
    #z.b = base
    #z.h = altura
    z.set_base(base)
    z.set_altura(altura)
    print(z.calc_area())  # calc_area(z)    
    

UI.main()


