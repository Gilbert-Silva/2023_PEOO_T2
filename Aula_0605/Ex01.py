import math
class Circulo:
  def __init__(self):
    self.__raio = 1
  def set_raio(self, raio):
    if raio > 0: self.__raio = raio   # 7 pontos
    else: raise ValueError()          # 7 pontos
  def get_raio(self):
    return self.__raio                # 7 pontos
  def calc_area(self):
    return math.pi * self.__raio ** 2 # 7 pontos
  def __str__(self):
    return f"Círculo de raio = {self.__raio}" # 7 

class UI:
  def main():
    for k in range(10):
      c = Circulo()   # 5 pontos
      c.set_raio(float(input("Informe o valor do raio: "))) # 5
      print(c.calc_area()) # 5 pontos

      
UI.main()    


    