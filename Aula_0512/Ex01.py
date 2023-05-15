x = 5
a = x == 5
if a: print("ok")
else: print("teste")
# Questão 3
print("Digite um número inteiro")
n = int(input())
for k in range(1, n+1):
  if k % 3 == 0: print(-k, end=" ")
  else: print(k, end = " ")  
print()

# Questão 4
def ultimo_dia_mes(mes, ano): 
  dia = 31
  if mes == 2: 
    dia = 28
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      dia = 29
  if mes == 4 or mes == 6 or mes == 9 or mes == 11: dia = 30
  return str(dia) + "/" + str(mes) + "/" + str(ano)  
  return f"{dia}/{mes}/{ano}"  

print(ultimo_dia_mes(2, 1900))
print(ultimo_dia_mes(2, 2000))


