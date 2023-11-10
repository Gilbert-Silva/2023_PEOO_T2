import json
from datetime import datetime


class Aluno:

  def __init__(self, id, nome, matricula, nasc):
    self.__id = id
    self.__nome = nome
    self.__matricula = matricula
    self.__nasc = nasc

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_matricula(self):
    return self.__matricula

  def get_nasc(self):
    return self.__nasc

  def set_id(self, id):
    self.__id = id

  def set_nome(self, nome):
    self.__nome = nome

  def set_matricula(self, matricula):
    self.__matricula = matricula

  def set_nasc(self, nasc):
    self.__nasc = nasc

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__matricula} - {self.__nasc}"

  def Aluno(self):
    return {
      "id": self.__id,
      "nome": self.__nome,
      "matricula": self.__matricula,
      "nasc": self.__nasc.strftime("%d/%m/%Y")
    }


class NAluno:
  __alunos = []

  @classmethod
  def inserir(cls, obj):
    NAluno.abrir()
    id = 0
    for aluno in cls.__alunos:
      if aluno.get_id() > id: id = aluno.get_id()
    obj.set_id(id + 1)
    cls.__alunos.append(obj)
    NAluno.salvar()

  @classmethod
  def listar(cls):
    NAluno.abrir()
    return cls.__alunos

  @classmethod
  def listar_id(cls, id):
    NAluno.abrir()
    for aluno in cls.__alunos:
      if aluno.get_id() == id: return aluno
    return None

  @classmethod
  def atualizar(cls, obj):
    NAluno.abrir()
    aluno = cls.listar_id(obj.get_id())
    if aluno is not None:
      aluno.set_nome(obj.get_nome())
      aluno.set_matricula(obj.get_matricula())
      aluno.set_nasc(obj.get_nasc())
      NAluno.salvar()

  @classmethod
  def excluir(cls, obj):
    NAluno.abrir()
    aluno = cls.listar_id(obj.get_id())
    if aluno is not None:
      cls.__alunos.remove(aluno)
      NAluno.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__alunos = []
      with open("alunos.json", mode="r") as f:
        s = json.load(f)
        for aluno in s:
          a = Aluno(aluno["id"], aluno["nome"],
                    aluno["matricula"],
                    datetime.strptime(aluno["nasc"], "%d/%m/%Y"))
          cls.__alunos.append(a)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("alunos.json", mode="w") as f:
      json.dump(cls.__alunos, f, default=Aluno.Aluno)

  @classmethod
  def Aniversariantes(cls, mes):
    result = []
    NAluno.abrir()
    for aluno in cls.__alunos:
      if aluno.get_nasc().month == mes:
        result.append(aluno)
    return result

class UI:

  @classmethod
  def Main(cls):
    op = 99
    while (op != 0):
      op = UI.Menu()
      if op == 1: UI.inserir()
      if op == 2: UI.listar()
      if op == 3: UI.atualizar()
      if op == 4: UI.excluir()
      if op == 5: UI.aniversariantes()

  @classmethod
  def Menu(cls):
    print(
      "1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Aniversariantes, 0 - Fim"
    )
    return int(input())

  @classmethod
  def inserir(cls):
    nome = input("Digite o nome: \n")
    matricula = input("Digite a matrícula: \n")
    nasc = datetime.strptime(input("Nascimento: "), "%d/%m/%Y")
    aluno = Aluno(0, nome, matricula, nasc)
    NAluno.inserir(aluno)

  @classmethod
  def listar(cls):
    for aluno in NAluno.listar():
      print(aluno)

  @classmethod
  def atualizar(cls):
    UI.listar()
    id = int(input("Id a ser atualizado: "))
    nome = input("Digite o nome: \n")
    matricula = input("Digite a matrícula: \n")
    nasc = datetime.strptime(input("Nascimento: "), "%d/%m/%Y")
    aluno = Aluno(id, nome, matricula, nasc)
    NAluno.atualizar(aluno)

  @classmethod
  def excluir(cls):
    UI.listar()
    id = int(input("Id a ser excluído: "))
    aluno = Aluno(id, "", "", "", "")
    NAluno.excluir(aluno)

  @classmethod
  def aniversariantes(cls):
    mes = int(input("Informe o mês para a lista de aniversariantes: "))
    for aluno in NAluno.Aniversariantes(mes):
      print(aluno)

UI.Main()
