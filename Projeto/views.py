from cliente import Cliente, NCliente

def cliente_inserir(nome, email, fone):
  cliente = Cliente(0, nome, email, fone)
  NCliente.inserir(cliente)

def cliente_listar():
  return NCliente.listar()
