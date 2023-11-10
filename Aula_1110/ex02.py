try:
  a = int(input("Informe o dividendo: "))
  b = int(input("Informe o divisor: "))
  print(a / b)
except ValueError:
  print("Digite valores inteiros váidos")
except ZeroDivisionError:
  print("Divisor não pode ser nulo")
