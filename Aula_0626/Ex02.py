import datetime

texto = input()
inteiro = int(input())
real = float(input())
#data = datetime(input())
data = datetime.datetime.strptime(input(), "%d/%m/%Y")
