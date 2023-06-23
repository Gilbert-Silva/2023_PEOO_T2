import datetime
import math
#import aluno
from aluno import Aluno

print(datetime.datetime.today())
print(math.sqrt(16))
a = datetime.datetime(2023, 6, 1)
b = datetime.datetime(2023, 6, 1, 9, 30, 15)
print(a)
print(b)
print(type(a))
x = 20
print(type(x))

#y = aluno.Aluno("Rafael")
y = Aluno("Rafael")
print(y)

e = datetime.datetime.fromisoformat("2023-06-23T09:30")
print(e)

t1 = datetime.timedelta(days=1, hours=10)
print(t1)

hoje = datetime.datetime.today()
nasc = datetime.datetime(2006, 12, 18)
dias = hoje - nasc
print(dias)



