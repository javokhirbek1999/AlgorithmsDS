# Recursive

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        
        return myPow(x*x, n//2) if n % 2 == 0 else x*myPow(x*x, n//2) 

      
# Iterative

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #Deal with negative power:
        if n < 0: 
            x = 1/x
            n = abs(n)
            
        #Iterate:
        res = 1
        while n:
            if n % 2 == 1:
                res = res*x
            x = x*x 
            n = n//2
            
        return res
