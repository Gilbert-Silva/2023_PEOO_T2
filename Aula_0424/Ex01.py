def iniciais(nome):
  palavras = nome.split()
  resultado = ""
  #print(palavras)
  for palavra in palavras:
    #print(palavra[0])
    resultado += palavra[0]
  return resultado  

def iniciais2(nome):
  resultado = nome[0]
  #print(len(nome))
  for k in range(len(nome)):
    #print(k, nome[k])
    if nome[k] == " ":
      resultado += nome[k+1]
  return resultado      

print(iniciais("Gilbert Azevedo da Silva"))
print(iniciais("Leonardo Ataíde Minora"))

print(iniciais2("Gilbert Azevedo da Silva"))
print(iniciais2("Leonardo Ataíde Minora"))

  