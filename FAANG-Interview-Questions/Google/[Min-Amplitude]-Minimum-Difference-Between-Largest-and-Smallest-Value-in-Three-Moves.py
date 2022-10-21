"""
Time: O(n log n)
Space: O(1)
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n <= 4:
            return 0
        
        nums.sort()

        # Remove first 3
        mn1 = nums[3]
        mx1 = nums[-1]
        diff1 = mx1-mn1

        # Remove first 2 and last 1
        mn2 = nums[2]
        mx2 = nums[-2]
        diff2 = mx2-mn2


        # Remove first 1 and last 2
        mn3 = nums[1]
        mx3 = nums[-3]
        diff3 = mx3-mn3

        # Remove last 3
        mn4 = nums[0]
        mx4 = nums[-4]
        diff4 = mx4 - mn4

        return min(diff1, diff2, diff3, diff4)
