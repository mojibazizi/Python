#def iscomposite(x):
    #'''returns if given number is prime'''
    #factors = [] #find the factors of x
    #for i in range(1, x + 1):
        #if(x % i == 0):
            #factors.append(i)
    #num_factors = len(factors)
    
    #if num_factors > 2:
        #return True
    #else:
        #return False
#print(iscomposite(8))


#def isAbundant(x):
    #'''returns if given number is Abundant'''
    #factors = [] #find the factors of x
    #for i in range(1, x + 1):
        #if(x % i == 0):
            #factors.append(i)
    #sum_fact = (sum(factors) - x)
    
    #if  sum_fact > x :
        #return True
    #else:
        #return False
#print(isAbundant(12))

def isNarcissistic(x):
    if x == sum([int(i) ** len(str(x)) for i in str(x)]):
        return True
    else:
        return False

print(isNarcissistic(370))
#def isTriangular(x):
 
    #if (x < 0):
        #return False
 
    # A Triangular number must be sum of first n natural numbers
    #sum, n = 0, 1
 
    #while(sum <= x):
     
       # sum = sum + n
        #if (sum == x):
         #   return True
        #n += 1
 
    #return False
#print(isTriangular(3))
