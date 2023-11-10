try:
  n = int(input("Informe um inteiro: "))
  print(2*n)
  s = "Teste"
  print(s[n])
except Exception as erro:
  print("Ocorreu um erro:")
  print(erro)
  print(type(erro))