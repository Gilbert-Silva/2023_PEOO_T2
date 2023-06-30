matriz1 = []
matriz1.append([0,0,1,1]) # input
matriz1.append([0,1,0,1]) # input
matriz1.append([0,0,1,0]) # input
matriz1.append([1,1,0,1]) # input
print(matriz1)

matriz2 = []
for k in range(4):
  linha = list(map(int, input().split()))
  matriz2.append(linha)
print(matriz2)



