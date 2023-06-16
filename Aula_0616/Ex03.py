op = input()

num_linhas = 3
num_colunas = 3

matriz = []
for k in range(num_linhas):
  matriz.append([0] * num_colunas)

for linha in range(num_linhas):
  for coluna in range(num_colunas):
    v = float(input())
    matriz[linha][coluna] = v

s = 0
n = 0
for linha in range(num_linhas):
  for coluna in range(num_colunas):
    if coluna > linha:
      s += matriz[linha][coluna]
      n += 1
      
if op == "S": print(f"{s:.1f}")
else: print(f"{s/n:.1f}")
  

for linha in range(num_linhas):
  for coluna in range(num_colunas):
    print(f"{matriz[linha][coluna]:.1f}", end = " ")
  print()
