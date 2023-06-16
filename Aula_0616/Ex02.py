x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(x)

for linha in range(3):
  for coluna in range(4):
    print(f"{x[linha][coluna]:3d}", end = " ")
  print()

num_linhas = 2
num_colunas = 8

matriz = []
for k in range(num_linhas):
  matriz.append([0] * num_colunas)
  
for linha in range(num_linhas):
  for coluna in range(num_colunas):
    print(f"{matriz[linha][coluna]:3d}", end = " ")
  print()

