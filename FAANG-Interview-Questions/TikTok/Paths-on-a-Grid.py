"""
Time: O(n * m)
Space: O(n * m)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        return self.solve(m, n, dp)
    
    def solve(self, m: int, n: int, dp: dict):
        
        if m == 1 and n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0
        
        point = (m, n)
        
        if point in dp:
            return dp[point]
        
        dp[point] = self.solve(m-1, n, dp) + self.solve(m, n-1, dp)
        
        return dp[point]
