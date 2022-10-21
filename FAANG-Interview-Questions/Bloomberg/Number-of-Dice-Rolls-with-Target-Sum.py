"""
n = # of dices
m = target

Time: O(n*m)
Space: O(n*m)
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = pow(10, 9) + 7
        
        dp = {}
        
        return self.solve(n, target, k, dp) % mod
    
    
    def solve(self, n: int, target: int, k: int, dp: dict) -> int:
        
        # Check if target lies within the range
        if target <= 0 or target > n * k:
            return 0
        
        # If we have only one dice
        if n == 1:
            return 1
        
        key = (n, target)
        
        if key in dp:
            return dp[key]
        
        
        curr = 0
        # Try out all combinations 
        for num in range(1, k+1):
            curr += self.solve(n-1, target-num, k, dp)

        dp[key] = curr
        
        return dp[key]
        
        
