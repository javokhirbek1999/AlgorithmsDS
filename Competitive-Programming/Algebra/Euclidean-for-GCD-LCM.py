"""
Time: O(log min(a,b))

Originally, the Euclidean algorithm was formulated as follows: subtract the smaller number from the larger one until one of the numbers is zero.
Indeed, if g divides a and b, it also divides a-b. On the other hand, if g divides a-b and b, then it also divides a = b + (a-b), which means that the sets of the common divisors of {a,b} and {b,a-b} coincide.

Note that a remains the larger number until b is subtracted from it at least floor(a/b) times. Therefore, to speed things up,
a-b is substituted with a-floor(a/b)*b = a mod b. 

Then the algorithm is formulated in an extremely simple way:

            gcd(a,b) = a, if b = 0 else gcd(b, a mod b)
            
"""

def gcdRec(a: int, b: int) -> int:

    if b == 0:
        return a
    
    return gcdRec(b, a % b)


def gcdIter(a: int, b: int) -> int:

    while b > 0:
        a = a % b
        a, b = b, a
    
    return a


def lcm(a: int, b: int) -> int:

    return (a * b)//gcdIter(a,b)


print(gcdIter(4,20))
