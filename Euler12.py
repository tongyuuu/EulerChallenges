from functools import reduce

x = 1
s = 0
a = 1
p = 0
y = 0

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while x < 100000000:
    s = s + x
    x = x+1
    f = len(factors(s))

    if f > 500:
        print(f)
        print(s)
        print(x)
        break

  

