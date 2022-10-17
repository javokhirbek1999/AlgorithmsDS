"""
Time: O(n)
Space: O(n)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = {num:1 for num in nums}
        
        
        _max = max(nums)
        
        for num in range(1, _max+1):
            if num not in nums:
                return num
        
        return _max+1 if _max > 0 else 1

        
