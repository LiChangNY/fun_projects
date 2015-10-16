"""
A shortcut to solve this problem is to limit the search results. If you 
run process(9) below, the kernel will for sure die because there are too 
many combinations to check, let alone iterating from process(1) to 
process(9). Hence, we can test if the sum of the digits is divisible by 3. 
If it is, no matter how you arrange the digits, the number won't be
a prime number. You may ask why not checking 6,7....? I guess you can. 
But it's not worth it because by testing 3, it already narrows down to 
1-digit(Forget it. Nick already told us that 2143 is a prime pandigital and 
it's bigger than 1.), 4-digit(promising) and 7-digit(Oooh). 
"""
##########################################################################
############uncommment codes below to see sum of n-digit number###########
#for n in range(1, 10):
#    combo = [i for i in range(1,n+1)]
#    if sum(combo) % 3 == 0:
#        continue
#    else:
#        print("%i-digit number can't be evenly divisible by 3" % n)
##########################################################################

import time

#check if a number is pandigital
def pandigital_check(num, n):
    num_combo = [i for i in map(int, str(num))]
    #The first criteria ensures numbers composed of 1-n digit, 
    #thus eliminating numbers like 7652319
    #The second criteria checks if every digit appears once, 
    #thus eliminating numbers like 7654333
    if max(num_combo) == n and len(set(num_combo)) == n:
        return True
    else:    
        return False
            
##check if number is divisible by any odd number
def partial_prime_check(num):
    for i in range(3, num, 2 ): 
        if (num%i) == 0:
            return False
            break
    return True
        
def process(n):  
    #define the largest number to start with, e.g. 7654321
    num = int(''.join(map(str, [-i for i in range(-n, 0)])))
    
    #keep trying a smaller number if any of tests fails
    while n > 0 and \
          (pandigital_check(num, n) == False or 
           partial_prime_check(num) == False):
               num -=2 #decrease by 2 to keep trying odd numbers
    return num               

start_time = time.time()
#If process(7) finds a number, no need to check prcess(4). 
#If not, we know at least 2143 is a prime pandigital number,
#thanks to Nick.          
seven_digit = process(7)
if seven_digit > 0:
    print "The largest n-pandigital number is ", seven_digit 
else:
    print "The largest n-pandigital number is ", process(4)

print "processing time: ", (time.time() - start_time)," seconds" 
