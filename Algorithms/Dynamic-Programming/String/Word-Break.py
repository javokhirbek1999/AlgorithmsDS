"""
Time: O(n^3)
Space: O(n)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        
        dp = [False] * (n+1)
        
        dp[0] = True
        
        wDict = {word:1 for word in wordDict}
        
        
        for i in range(n+1):
            
            for j in range(i):
                
                if dp[j] and s[j:i] in wDict:
                    dp[i] = True
                    break
        
        return dp[n]
