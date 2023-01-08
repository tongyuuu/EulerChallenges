a = 2 ** 1000
print(a)
x = 0
y = str(a)
print(y)
g = 0

while x < len(y):
    g = g + int(y[x])
    x = x + 1

print(g)

