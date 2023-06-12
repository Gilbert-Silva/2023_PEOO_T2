x = []
for i in range(10):
  n = int(input())
  if n <= 0: n = 1
  x.append(n) 
for i in range(10):
  #print("X[" + str(i) + "] = " + str(x[i]))
  print(f"X[{i}] = {x[i]}")
  
  