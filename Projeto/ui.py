#from cliente import Cliente, NCliente
#from servico import Servico, NServico
#from agenda import Agenda, NAgenda
from views import Views
import datetime

class UI:

  @classmethod
  def Main(cls):
    op = 0
    while (op != 99):
      op = UI.Menu()
      if op == 1: UI.Cliente_Inserir()
      if op == 2: UI.Cliente_Listar()
      if op == 3: UI.Cliente_Atualizar()
      if op == 4: UI.Cliente_Excluir()
      if op == 5: UI.Servico_Inserir()
      if op == 6: UI.Servico_Listar()
      if op == 7: UI.Servico_Atualizar()
      if op == 8: UI.Servico_Excluir()
      if op == 9: UI.Agenda_Inserir()
      if op == 10: UI.Agenda_Listar()
      if op == 11: UI.Agenda_Atualizar()
      if op == 12: UI.Agenda_Excluir()
      if op == 13: UI.Agenda_Abrir_Agenda_do_Dia()

  @classmethod
  def Menu(cls):
    print("\nClientes: ")
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
    print("\nServiços: ")
    print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
    print("\nAgenda: ")
    print(
      "9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir, 13 - Abrir Agenda do Dia"
    )
    print("\nOutras Opções: ")
    print("99 - Sair")
    return int(input())

  @classmethod
  def Cliente_Inserir(cls):
    # id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("fone: ")
    Views.cliente_inserir(nome, email, fone)
    #cliente = Cliente(0, nome, email, fone)
    #NCliente.inserir(cliente)

  @classmethod
  def Cliente_Listar(cls):
    #for cliente in NCliente.listar():
    for cliente in Views.cliente_listar():
      print(cliente)

  @classmethod
  def Cliente_Atualizar(cls):
    UI.Cliente_Listar()
    id = int(input("Id do cliente a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    fone = input("Novo fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  @classmethod
  def Cliente_Excluir(cls):
    UI.Cliente_Listar()
    id = int(input("Id do cliente a ser excluído: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)

  @classmethod
  def Servico_Inserir(cls):
    # id = int(input("Id: "))
    desc = input("Descrição: ")
    valor = input("Valor (R$): ")
    duracao = input("Duração (min): ")
    servico = Servico(0, desc, valor, duracao)
    NServico.inserir(servico)

  @classmethod
  def Servico_Listar(cls):
    for servico in NServico.listar():
      print(servico)

  @classmethod
  def Servico_Atualizar(cls):
    UI.Servico_Listar()
    id = int(input("Id do serviço a ser atualizado: "))
    desc = input("Nova Descrição: ")
    valor = input("Novo Valor (R$): ")
    duracao = input("Nova Duração (min): ")
    servico = Servico(id, desc, valor, duracao)
    NServico.atualizar(servico)

  @classmethod
  def Servico_Excluir(cls):
    UI.Servico_Listar()
    id = int(input("Id do serviço a ser excluído: "))
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)

  @classmethod
  def Agenda_Inserir(cls):
    data = input("Data dd/mm/aaaa HH:MM:")
    confirmado = True
    UI.Cliente_Listar()
    id_cliente = int(input("Id do cliente: "))
    UI.Servico_Listar()
    id_servico = int(input("Id do serviço: "))
    agenda = Agenda(0, datetime.datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    confirmado, id_cliente, id_servico)
    NAgenda.inserir(agenda)

  @classmethod
  def Agenda_Listar(cls):
    for agenda in NAgenda.listar():
      id_cliente = agenda.get_id_cliente()
      id_servico = agenda.get_id_servico()
      nome_cliente = ""
      desc_servico = ""
      if id_cliente != 0:
        nome_cliente = NCliente.listar_id(id_cliente).get_nome()
      if id_servico != 0:
        desc_servico = NServico.listar_id(id_servico).get_descricao()
      print(agenda, end="")
      print(" - " + nome_cliente + " - " + desc_servico)

  @classmethod
  def Agenda_Atualizar(cls):
    UI.Agenda_Listar()
    id = int(input("Id da agenda a ser atualizada: "))
    data = input("Data dd/mm/aaaa HH:MM: ")
    confirmado = True
    UI.Cliente_Listar()
    id_cliente = int(input("Id do cliente: "))
    UI.Servico_Listar()
    id_servico = int(input("Id do serviço: "))
    agenda = Agenda(id, datetime.datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    confirmado, id_cliente, id_servico)
    NAgenda.atualizar(agenda)

  @classmethod
  def Agenda_Excluir(cls):
    UI.Agenda_Listar()
    id = int(input("Id da agenda a ser excluída: "))
    agenda = Agenda(id, "", "", "", "")
    NAgenda.excluir(agenda)

  @classmethod
  def Agenda_Abrir_Agenda_do_Dia(cls):
    data = input("Data dd/mm/aaaa: ")
    hinicio = input("Horário início HH:MM: ")
    hfim = input("Horário fim HH:MM: ")
    intervalo = int(input("Intervalo (min): "))
    Views.agenda_abrir_agenda_do_dia(data, hinicio, hfim, intervalo)

UI.Main()
