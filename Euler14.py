

p = 1
s = 0
l = 0
m = 0


for x in range (1000000,0,-1):
    l = x
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        p = p+1
    if p > s:
        s = p
        m = l

    p = 1

print(s)
print(m)
