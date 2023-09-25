from cliente import Cliente, NCliente
from agenda import Agenda, NAgenda
import datetime

class Views:

  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()

  @classmethod
  def agenda_abrir_agenda_do_dia(cls, data, hinicio, hfim, intervalo):
    data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
    delta = datetime.timedelta(minutes=intervalo)
    aux = data_inicio
    while aux <= data_fim:
      NAgenda.inserir(Agenda(0, aux, False, 0, 0))
      aux = aux + delta

