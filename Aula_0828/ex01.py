class Mesa:

  def __init__(self, id, numero):
    self.__id = id
    self.__numero = numero
    self.__disponivel = True

  def get_id(self):
    return self.__id

  def set_numero(self, numero):
    self.__numero = numero

  def get_numero(self):
    return self.__numero

  def set_disponivel(self, disponivel):
    self.__disponivel = disponivel

  def get_disponivel(self):
    return self.__disponivel

  def __str__(self):
    return f"{self.__id} - {self.__numero} - {self.__disponivel}"


class NMesa:

  def __init__(self):
    self.__mesas = []

  def inserir(self, mesa):
    self.__mesas.append(mesa)

  def listar(self):
    return self.__mesas


class Assunto:

  def __init__(self, id, descricao):
    self.__id = id
    self.__descricao = descricao

  def get_id(self):
    return self.__id

  def set_descricao(self, descricao):
    self.__descricao = descricao

  def get_descricao(self):
    return self.__descricao

  def __str__(self):
    return f"{self.__id}: {self.__descricao}"


"""
class NAssunto:
  def __init__(self):
    self.__assuntos = []
  def inserir(self, assunto):
    self.__assuntos.append(assunto)
  def listar(self):
    return self.__assuntos
"""


class NAssunto:
  __assuntos = []
  @classmethod
  def inserir(cls, assunto):
    cls.__assuntos.append(assunto)
  @classmethod
  def listar(cls):
    return cls.__assuntos


a = Assunto(1, "Instalação de software")
b = Assunto(2, "Reposição de avaliação")
"""
x = NAssunto()
y = NAssunto()
x.inserir(a)
x.inserir(b)
for assunto in x.listar():
  print(assunto)
"""
NAssunto.inserir(a)
NAssunto.inserir(b)
for assunto in NAssunto.listar():
  print(assunto)
