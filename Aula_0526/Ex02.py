class Aluno:
  def __init__(self):
    self.nome = "sem nome"
    self.matricula = "1234"
  # programa uma nova comparação entre os objetos  
  def __eq__(self, outro):
    return self.matricula == outro.matricula

a = Aluno() # novo objeto da classe Aluno
b = Aluno() # novo objeto da classe Aluno
c = a       # c é o mesmo objeto que a
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print(a == b) # a.__eq__(b)

if a == b: print("a e b são iguais")
else: print("a e b são diferentes")
if a == c: print("a e c são iguais")
else: print("a e c são diferentes")
print(a.nome)
print(b.nome)
print(c.nome)
a.matricula = "4321"
if a == b: print("a e b são iguais")
else: print("a e b são diferentes")
  

  
  

