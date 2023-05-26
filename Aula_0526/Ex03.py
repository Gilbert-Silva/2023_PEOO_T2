import math
class Circulo:
  def __init__(self):
    self.__raio = 0
  def set_raio(self, valor):
    if valor > 0: self.__raio = valor
  def get_raio(self):
    return self.__raio
  def area(self):
    return math.pi * self.__raio ** 2
  def __gt__(self, outro):
    return self.__raio > outro.__raio
    

a = Circulo()
b = Circulo()

print(a)
#a.raio = -10
#print(a.raio)
x = int(input())
a.set_raio(x)      # a.raio = 10 --- set_raio(a, 10)
print(a.get_raio())
print(a.area())   # area(a)

#b.raio = 5
b.set_raio(5)    # set_raio(b, 5)
print(b)
#print(b.raio)
print(b.area())    # area(b)

print(a == b)
print(a > b)



x = 10
#print(x.area())  
