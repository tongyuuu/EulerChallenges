s = 0
y = 0
for x in range(1, 101):
    s = s + x*x
    y = y + x
    x = x + 1

print (y)
t = y*y
print (t)
f = s - t
print(f)

