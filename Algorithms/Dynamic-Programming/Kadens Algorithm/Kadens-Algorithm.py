"""
Time: O(n)
Space: O(1)
"""

def maxSubArray(self, nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    globalMax, localMax = -math.inf, -math.inf

    for num in nums:

        if localMax < 0:
            localMax = num
        else:
            localMax += num

        globalMax = max(globalMax, localMax)

    return globalMax
