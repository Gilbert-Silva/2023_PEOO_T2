import datetime

class Amigo:
  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc
  def get_nasc(self):
    return self.__nasc
  def get_nome(self):
    return self.__nome
  def __str__(self):
    return f"{self.__nome} - {self.__nasc}"

# Ler dados de 10 amigos e mostrar o mais novo
# Para ler uma data do usuário
# data = datetime.datetime.strptime(input(), "%d/%m/%Y")
class UI:
  def main():
    amigos = []
    for k in range(1, 3):
      print(f"Informe o nome do {k}º amigo")
      nome = input()
      print("Informe o nascimento")
      nasc = datetime.datetime.strptime(input(), "%d/%m/%Y")
      a = Amigo(nome, nasc)
      amigos.append(a)
    print(*amigos)
    maior = amigos[0]
    for amigo in amigos:
      if amigo.get_nasc() > maior.get_nasc():
        maior = amigo
    print(f"Amigo(a) mais novo(a): {maior.get_nome()}")    

UI.main()    