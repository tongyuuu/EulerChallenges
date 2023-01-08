import math

def binomialcoefficient (n):
    return math.factorial(2*n)/math.factorial(n)**2

a = binomialcoefficient(20)
print(a)
