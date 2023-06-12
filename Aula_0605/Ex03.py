x = [5, 6, 3, 2, 1, 8]
print(x)
print(sorted(x))
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
print(x[2:])
print(x[:4])
print(x[2:4])

class Aluno:
  def __init__(self, nome, mat):
    self.nome = nome
    self.mat = mat
  def __str__(self):
    return f"{self.nome} - {self.mat}"

a = Aluno("Rita", "8888")
b = Aluno("Lucas", "4321")
c = Aluno("Vinicius", "5555")
w = [a, b, c]
print(type(a))
print(type(a.nome))
print(type(w))
print(*w)
for aluno in w: print(aluno)
#w.sort()
for aluno in w: print(aluno)

print(1 < 5)
print(a < b)












