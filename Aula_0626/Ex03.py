n, m = map(int, input().split()) # n = linhas, m = colunas
print(n)
print(m)
matriz = []
for k in range(n + 2):
  matriz.append([0] * (m + 2))
print(matriz)
for k in range(n):
  linha = list(map(int, input().split()))
  print(linha)
  for j in range(m):
    matriz[k+1][j+1] = linha[j]
print(matriz)




