
        
count = 0            
for num in range(1, 100000000000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           count = count + 1
           s = num
           
   if count == 10001:
       print(s)
       break


