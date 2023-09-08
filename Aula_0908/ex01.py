import json

x = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"}
print(x)
for item in x.items():
  print(item)
  print(item[0])
  print(item[1])

for key in x:
  print(key)


class Cliente:

  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  def __str__(self):
    return f"{self.id} - {self.nome}"


a = Cliente(1, "Rodrigo")
b = Cliente(2, "Samia")
print(a)
print(vars(a))
print(a.__dict__)
print(a.__dict__["id"])
print(a.__dict__["nome"])
print(b)
print(vars(b))
print(b.__dict__)
print(b.__dict__["id"])
print(b.__dict__["nome"])

x = [a, b]
print(x)

with open("clientes2.json", "w") as f1:
  json.dump(x, f1, default=vars)

clientes = []
with open("clientes2.json", "r") as f2:
  clientes_json = json.load(f2)  # lista de dicts
  for obj in clientes_json:
    print(obj)
    c = Cliente(obj["id"], obj["nome"])
    clientes.append(c)

for c in clientes:
  print(c)
