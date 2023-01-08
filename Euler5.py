##
##for x in range(1, 100000000000000):
##    if x % 11== 0 and x % 12== 0 and x % 13== 0 and x % 14== 0 and x % 15== 0 and x % 16== 0 and x % 17== 0 and x % 18== 0 and x % 19== 0 and x % 20== 0:
##        print(x)
##        break
##   


##for x in range (1, 100):
##   if x % 1 == 0 and x % 2 == 0 and x % 3 == 0:
##      print(x)
y = 0
x = 232792567

while x > 20:
   found = True
   for y in range (1,21):
      if x % y != 0:
         found = False
         break
   if found == True:
      print(x)
      break
   x = x-1      
         
         
         

        
    
