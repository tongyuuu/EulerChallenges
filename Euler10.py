##s = 2
##count = 0
##isPrime = True
##for num in range(3,2000001,2):
##    isPrime = True
##    for y in range(3, num,2):
##        if (num % y) == 0:
##            isPrime = False
##            break
##
##    if(isPrime == True):
##        s = num + s
##        count = count + 1

##
##print(s)

def eratosthenes2(n):
    #Declare a set - an unordered collection of unique elements
    multiples = set()
    

    #Iterate through [2,2000000]
    for i in range(2, n+1):

        #If i has not been eliminated already 
        if i not in multiples:

            #Yay prime!
            yield i

            #Add multiples of the prime in the range to the 'invalid' set
            multiples.update(range(i*i, n+1, i))
           

#Now sum it up
iter = 0
ml = list(eratosthenes2(2000000))
for x in ml:
    iter = int(x) + iter
print('total')
print(iter)
