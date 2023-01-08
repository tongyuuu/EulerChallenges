import math
a = math.factorial(100)
x = 0
y = 0
v = str(a)
print(len(v))
while x < len(v):
    y = y + int(v[x])
    x = x +1
print(y)
    
