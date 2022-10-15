"""
Time: O(n)
Space: O(1)
"""

def maxSubArray(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    globalMax, localMax = -math.inf, -math.inf

    for num in nums:
        localMax = max(localMax+num, num)
        globalMax = max(globalMax, localMax)

    return globalMax
    



