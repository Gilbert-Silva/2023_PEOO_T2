class Medicamento:
  def __init__(self, id, nome, indicacao):  
    self.__id = id
    self.__nome = nome
    self.__indicacao = indicacao

class NMedicamento:
  def __init__(self):
    self.__medicamentos = []
  def inserir(self, m):
    self.__medicamentos.append(m)
  def listar(self):
    return self.__medicamentos

class UI:

  @staticmethod        
  def main(self):
    op = 10
    while op != 0:
      op = self.menu()
      if op == 1: self.inserir_medicamento()
      if op == 2: self.listar_medicamento()

  @staticmethod        
  def menu(self):
    print("1 - Inserir, 2 - Listar")
    return int(input())    

  @staticmethod        
  def inserir_medicamento(self):
    id = int(input("Id: "))
    nome = input("Nome: ")
    ind = input("Indicação: ")
    m = Medicamento(id, nome, ind)
