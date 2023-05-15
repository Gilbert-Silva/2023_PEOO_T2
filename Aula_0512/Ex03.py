class Contato:
  def __init__(self):
    self.__nome = "sem nome"
    self.__fone = "sem fone"
  def set_nome(self, n):
    if n != "": self.__nome = n
    else: raise ValueError()  
  def set_fone(self, f):
    self.__fone = f
  def get_nome(self):
    return self.__nome
  def get_fone(self):
    return self.__fone

class UI:  
  contatos = []
  @classmethod
  def main(cls):
    op = UI.menu()
    while op != 0:
      if op == 1: UI.inserir()
      if op == 2: UI.listar()
      op = UI.menu()    
    print("Até logo")

  @classmethod
  def inserir(cls):
    nome = input("Digite o nome: ")
    fone = input("Digite o fone: ")
    c = Contato()
    c.set_nome(nome)
    c.set_fone(fone)
    cls.contatos.append(c)
  
  @classmethod
  def listar(cls):
    for c in cls.contatos:
      print(c.get_nome(), c.get_fone())
    
  @classmethod
  def menu(cls):
    print("1 - Inserir, 2 - Listar, 0 - Fim")
    return int(input())
    
UI.main()    