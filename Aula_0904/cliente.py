import json


class Cliente:

  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_email(self):
    return self.__email

  def get_fone(self):
    return self.__fone

  def set_id(self, id):
    self.__id = id

  def set_nome(self, nome):
    self.__nome = nome

  def set_email(self, email):
    self.__email = email

  def set_fone(self, fone):
    self.__fone = fone

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


"""
class NCliente:
  def __init__(self):
    self.__clientes = []
  def inserir(self, obj):
    self.__clientes.append(obj)
  def listar(self):
    return self.__clientes
"""


class NCliente:
  __clientes = []

  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)
    NCliente.salvar()

  @classmethod
  def listar(cls):
    NCliente.abrir()
    return cls.__clientes

  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None

  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()

  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)
    NCliente.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", "r") as f2:
        clientes_json = json.load(f2)  # lista de dicts
        for obj in clientes_json:
          c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"],
                      obj["_Cliente__email"], obj["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      #print("Nenhum arquivo encontrado")
      pass
      
  @classmethod
  def salvar(cls):
    with open("clientes.json", "w") as f1:
      json.dump(cls.__clientes, f1, default=vars)


"""
a = Cliente(1, "Matheus", "matheus@email.com", "987654321")
b = Cliente(2, "Samia", "samia@email.com", "912345678")
print(a)
print(a.get_email())
a.set_email("matheus@ifrn.edu.br")
print(a)
print(b)
x = NCliente()
x.inserir(a)
x.inserir(b)
for cliente in x.listar(): print(cliente)
"""


class UI:

  @classmethod
  def Main(cls):
    op = 0
    while (op != 99):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()

  @classmethod
  def Menu(cls):
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 99-Sair")
    return int(input())

  @classmethod
  def ClienteInserir(cls):
    #id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("Email: ")
    fone = input("Fone: ")
    #cliente = Cliente(id, nome, email, fone)
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)

  @classmethod
  def ClienteAtualizar(cls):
    print("Clientes cadastrados")
    UI.ClienteListar()
    id = int(input("Informe o id para atualizar: "))
    nome = input("Nome: ")
    email = input("Email: ")
    fone = input("Fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  @classmethod
  def ClienteExcluir(cls):
    print("Clientes cadastrados")
    UI.ClienteListar()
    id = int(input("Informe o id para excluir: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)


UI.Main()
"""

a = Cliente(1, "Matheus", "matheus@email.com", "987654321")
b = Cliente(2, "Samia", "samia@email.com", "912345678")
NCliente.inserir(a)
NCliente.inserir(b)

print(NCliente.listar_id(1))

for cliente in NCliente.listar(): print(cliente)
c = Cliente(2, "Samia", "samia@ifrn.edu.br", "912345678")
NCliente.atualizar(c)
d = Cliente(1, "", "", "")
NCliente.excluir(d)
for cliente in NCliente.listar(): print(cliente)

"""
