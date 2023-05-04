lista = [" José", "Gilbert", "  Minora"]
lista.sort()
print(lista)

def formatar_nome(nome):
  s = nome.lower()
  palavras = s.split()
  resultado = ""
  for palavra in palavras:
    match(palavra):
      case "da" | "de" | "do": resultado += palavra
      case "das" | "dos" | "e" : resultado += palavra
      case _: 
        resultado += palavra[0].upper()
        resultado += palavra[1:]
    resultado += " " 
  return resultado  

print("Digite seu nome")
s = input()
print(formatar_nome(s))  


"""print("Digite seu nome")
s = input().lower()
palavras = s.split()
resultado = ""
for palavra in palavras:
  match(palavra):
    case "da" | "de" | "do": resultado += palavra
    case "das" | "dos" | "e" : resultado += palavra
    case _: 
      resultado += palavra[0].upper()
      resultado += palavra[1:]
  resultado += " "
print(resultado)  
"""
#if palavra == "da" or palavra == "de" or palavra ..... == "e":
#else: é o case _:

