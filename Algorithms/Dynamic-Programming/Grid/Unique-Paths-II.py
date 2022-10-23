"""
Time: O(n * m)
Space: O(n * m)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        
        dp = []
        
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(0)
            dp.append(row)
        

        flag = False
        
        # Fill first row
        for i in range(m):
            if flag or obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                flag = True
            else:
                dp[0][i] = 1
        
        
        flag = False
        
        # Fill first column
        for i in range(n):
            if flag or obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                flag = True
            else:
                dp[i][0] = 1
        
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
