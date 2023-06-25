"""
Sieve of Eratosthenes is an algorithm for finding all the prime numbers in a segment [1:n] using O(n log log n) operations

The idea behind is this: 
A number is prime, if none of the smaller prime numbers divides it. 
Since we iterate over the prime numbers in order, we already marked all numbers,
who are divisible by at least one of the prime numbers, as divisible.
Hence if we reach a cell and it is not marked,
then it isn't divisible by any smaller prime number and therefore has to be prime.

A number X is prime if none of the primes smaller than X divides it
                                                          
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
[F, F, T, T, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F]
                         
"""

def sieve_of_eratosthenes(n: int):

    isPrime = [True for _ in range(n+1)]

    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, n+1):
        if isPrime[i] and i * i <= n:
            for j in range(i*i,n+1,i):
                isPrime[j] = False
    
    
    primes = []

    for i in range(n+1):
        if isPrime[i]:
            primes.append(i)
    
    print(*primes)

sieve_of_eratosthenes(20)

