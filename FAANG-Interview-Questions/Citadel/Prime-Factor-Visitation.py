def primeFactVis(states, numbers):
    # get primes up to max(numbers)
    def _getPrimes(n):
        ret = set(range(2, n + 1))
        for i in range(2, n + 1):
            if i in ret:
                j = i*2
                while j <= n:
                    if j in ret:
                        ret.remove(j)
                    j += i
        
        return ret

    def _getPrimeFactors(n, primes):
        ret = set()
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                for d in (i, n // i):
                    if d in primes:
                        ret.add(d)
        
        return ret


    ma = max(max(numbers), len(states))
    primes = _getPrimes(ma)
    # if we see a prime factor an odd num of times, we
    # flip it. if not, we don't. we may flip more than once
    # even with this logic b/c we deal with multiples of primes
    allPrimes = set()
    for num in numbers:
        for p in _getPrimeFactors(num, primes):
            if p in allPrimes:
                allPrimes.remove(p)
            else:
                allPrimes.add(p)

    for i in range(len(states)):
        pos = i + 1
        pf = _getPrimeFactors(pos, primes)
        for p in pf:
            if p in allPrimes:
                states[i] = 1 - states[i]
    return states
