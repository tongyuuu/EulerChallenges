found = False
for a in range(50,1000):
    for b in range(a+1,1000):
        for c in range(b+1,1000):
            if a*a + b*b == c*c:
                if a + b + c == 1000:
                    print(a,b,c)
                    print(a*b*c)
                    found = True
                    break
        if found == True:
            break
    if found == True:
        break
                        
