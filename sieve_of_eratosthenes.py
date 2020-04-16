def sieve(n):
    ''' 
    find all primes less than n
    input: an integer n
    return: array of length n. 
        the ith element holds a binary flag that denotes if the natural number i is prime.
        (1 for prime, 0 for composite)
    ''' 

    # we start by naively flagging every number as prime, for this reason:
        # it is easier to find non-prime numbers than primes (just find another factor besides itself and 1)
        # so this algorithm will easily identify non prime numbers and update the flags to 0
    x = [1] * n

    # To avoid confusion, this array could skip 0 and 1 since these are exceptions to the prime definition. But they're included.
    # set 1 as NOT prime. 
    x[1] = 0
    n = n * 1.0
    
    # essentially here we're iterating over multiples of i and marking them as 0 (not prime). 
    # we can do this simply because a multiple of an integer inherently has factors other than itself and 1
    # from 2 to n/2 (non-inclusive)
    for i in range(2,int(n/2)):
            # start with the double of i. next will be the triple, and so on
            j = 2 * i
            while j < n:
                x[j]=0
                #print(i, j, x)
                j = j+i # increment by i. 
                    
    return x