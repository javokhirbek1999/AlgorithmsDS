"""
Time: O(n^2)
Space: O(n)
"""

def lengthOfLIS(nums: List[int]) -> int:
        
        res = []
        
        n = len(nums)
        
        for _ in range(n):
            res.append(1)
        
        maxLen = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j] and res[i] >= res[j]:
                    res[j] += 1
                    maxLen = max(maxLen, res[j])  

        return maxLen
