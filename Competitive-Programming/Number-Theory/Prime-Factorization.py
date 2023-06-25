"""

Goal: Break X down into its prime divisors

Naive - try all numbers up to X

A bit less naive - try only primes up to X

Even less naive - you can't have two primes larger than sqrt(x), so you only have to check up to sqrt(x),
                  then you can conclude that X is prime if it has no other prime factors

"""

primes = []

def factors(x):

    res = []

    for p in primes: # precompute list of primes

        if p * p > x:
            # CHECKED ALL PRIMES BELOW P, now x can't be a product of two unchecked primes since p^2 > x
            # so x must be prime

            if x > 1:
                res.append(x)
                x = 1
        else:
            # Get all primes up below P
            while (x % p == 0): # take as much of this prime as we have
                res.append(p) 
                x = x//p # make sure to divide x, that makes p^2 > x case work
 
    return res

