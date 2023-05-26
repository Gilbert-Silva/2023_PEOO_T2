x = 5
y = 2.5
z = 5
print(type(x))
print(type(y))
print(type(z))
print(id(x))
print(id(y))
print(id(z))
s = "Teste"
print(type(s))
print(id(s))
print(x + y)
print(s + s)
print(x * s)
b = True
c = False
print(type(b))
print(type(c))
d = 10 == 5
print(type(d))
print(d)
e = x > y
print(type(e))
print(e)
if e: print(f"{x} > {y}")
if e == True: print(f"{x} > {y}")
if x > y: print(f"{x} > {y}") 
# ==  != > >= < <= 
x = 5
print(x)
x += 10
print(x)
x = x + 10
print(x + 10)
print(x)
y = 25
if x > y: print(f"{x} > {y}")
else: 
  if x < y: print(f"{x} < {y}")
  else: print(f"{x} = {y}")  

if x > y: print(f"{x} > {y}")
elif x < y: print(f"{x} < {y}")
else: print(f"{x} = {y}")

for k in range(10):  #range(0, 10, 1)
  print(k, end="\t")
print()  
for k in range(20, 9, -2):
  print(k)
for k in range(0, 10, 3):
  print(k) 

k = 0
while(k < 10):
  print(k)
  k += 3
  
def soma(x, y):
  return x + y

print(soma(10, 20))
print(soma("10", "20"))
z = soma("10", "20")
print(type(z))

#print(soma(10, "20"))

def escreva(x):
  if x == 0: 
    print(x)
    return
  if x < 10: 
    print(x)
    escreva(x-1)

escreva(9) # print(5) escreva(4)
           # print(4) escreva(3)
           # print(3) escreva(2)
           # print(2) escreva(1)
           # print(1) escreva(0)
           # return






