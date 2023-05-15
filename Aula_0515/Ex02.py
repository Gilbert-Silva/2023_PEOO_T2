class Cinema:
  def __init__(self):
    self.__dia = "dom"
    self.__horario = 17
  def set_dia(self, dia):
    dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
    if dia in dias: self.__dia = dia
    else: raise ValueError()  
  def get_dia(self):
    return self.__dia
  def set_horario(self, horario):
    if horario >= 0 and horario <= 23: self.__horario = horario
    else: raise ValueError()    
  def get_horario(self):
    return self.__horario
  def inteira(self): # Regra de negócio
    if self.__dia == "qua": return 8
    valor = 20
    if self.__dia == "seg" or self.__dia == "ter" or self.__dia == "qui": valor = 16
    if self.__horario >= 17 or self.__horario == 0: valor = 1.5 * valor
    return valor  
  def meia_entrada(self):
    if self.__dia == "qua": return 8
    return self.inteira()/2  

class UI:
  @staticmethod
  def main():
    x = Cinema()
    #x.__dia = "seg"
    x.set_dia("seg")          #set_dia(x, "seg")
    x.set_horario(13)
    print(x.get_dia())
    print(x.get_horario())
    print(f"Inteira = {x.inteira()} Meia-entrada = {x.meia_entrada()}")
    y = Cinema()
    y.set_dia("qua")          #set_dia(y, "qua")
    print(y.get_dia())
    print(y.get_horario())
    print(f"Inteira = {y.inteira()} Meia-entrada = {y.meia_entrada()}")
    d = input("Informe o dia da sessão: ")
    h = int(input("Informe o horário da sessão: "))
    z = Cinema()
    z.set_dia(d)
    z.set_horario(h)
    print(f"Inteira = {z.inteira()} Meia-entrada = {z.meia_entrada()}")
    
    
UI.main()