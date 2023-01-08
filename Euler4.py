
def reverse(s):
    return s[::-1]


for x in range(999, 900, -1):
    found = False
    for y in range(999,900, -1):
        s = x*y
        if str(s) == reverse(str(s)):
            print(s)
            found = True
            break
            
    if(found == True):
        break
            
            
        
    



