
##a = 600851475143
##n = 0
##while n*n < a:
##    if a % count == 0 and a % 1 == 0:
##        print(count)
##        
n = 600851475143
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i         
    i = i + 1

print (n)
