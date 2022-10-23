"""
Time: O(n * m)
Space: O(n * m)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        dp = []
        
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(0)
                
            dp.append(row)
        
        # Starting cell
        dp[0][0] = grid[0][0]
        
        # Filling the first row
        for col in range(1,m):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        
        # Filling the first column
        for row in range(1, n):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        
        
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]
