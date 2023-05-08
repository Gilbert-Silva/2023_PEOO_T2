class Triangulo:
  def __init__(self):
    self.b = 0
    self.h = 0
  def calc_area(self):
    return self.b * self.h / 2

print("Informe a base do triangulo")
base = float(input())
print("Informe a altura do triangulo")
altura = float(input())
x = Triangulo()
y = Triangulo()
x.b = base
x.h = altura
print(x, x.b, x.h)
print(x.b * x.h / 2)
print("Area", x.calc_area())
y.b = 15
y.h = 25
print(y, y.b, y.h)
print(y.b * y.h / 2)
print(y.calc_area())
z = x
print(z)
z.b = 50
print(x.b)

a = 5
b = 5
print(id(a))
print(id(b))
print(type(a))
print(type(x))

import math
print(math.pi)

