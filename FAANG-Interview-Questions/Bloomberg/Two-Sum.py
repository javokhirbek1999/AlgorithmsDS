"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {target-nums[i]:i for i in range(len(nums))}
        
        
        for i in range(len(nums)):
            if nums[i] in d and d[nums[i]] != i:
                return [i, d[nums[i]]]

              
"""
Time: O(n log n)
Space: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort(key=lambda x:x[0])
        
        n = len(nums)
        
        low, high = 0, n-1
        
        while low < high:
            
            currentSum = nums[low][0] + nums[high][0]
            
            if currentSum == target:
                return [nums[low][1], nums[high][1]]
            
            if currentSum < target:
                low += 1
            else:
                high -= 1
        
        
