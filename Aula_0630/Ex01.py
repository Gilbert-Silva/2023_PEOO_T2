lista = []
lista.append(10)
lista.append(5)
lista.append(15)
print(lista)

lista2 = [40, 10, 5]
print(lista2)

matriz = []
print(matriz)
matriz.append(lista)
print(matriz)
matriz.append(lista2)
print(matriz)
print(matriz[0][2])

matriz2 = [ [1,2], [3,4], [5,6] ]
print(matriz2)

prim_linha = [0] * 5
print(prim_linha)
seg_linha = [0] * 5
print(seg_linha)

matriz3 = []
matriz3.append(prim_linha)
matriz3.append(seg_linha)
print(matriz3)

nlinhas = int(input("Informe o nº de linhas: "))
ncolunas = int(input("Informe o nº de colunas: "))

matriz4 = []
for k in range(nlinhas):  # nº linhas
  linha = [0] * ncolunas   # nº colunas
  matriz4.append(linha)
print(matriz4)




