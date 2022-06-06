def get_factor(x):
    '''return a list of factors for the given number'''
    factors = []
    #iterate over range from 1 to x number itself.
    for i in range(1, x + 1):
        #check if i divide x evenly
        if (x % i == 0):
            factors.append(i)
    return factors
print(get_factor(10))
        