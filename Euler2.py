tab = 0
a,b = 0, 1
count = 0
while tab < 4500000:
    sequence = a+b
    a = b
    b = sequence
    count =+ 1
    if sequence % 2 == 0:
        tab = sequence + tab
        print(tab)
       
        
    
