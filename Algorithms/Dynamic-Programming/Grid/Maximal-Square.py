"""
Time: O(n * m)
Space: O(n * m)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = []
        
        for _ in range(n+1):
            row = []
            for _ in range(m+1):
                row.append(0)
            dp.append(row)
        
        
        maxSize = 0
        for row in range(1, n+1):
            for col in range(1, m+1):
                if matrix[row-1][col-1] == '1':                 
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    maxSize = max(maxSize, dp[row][col])
        
        
        return maxSize * maxSize
        
