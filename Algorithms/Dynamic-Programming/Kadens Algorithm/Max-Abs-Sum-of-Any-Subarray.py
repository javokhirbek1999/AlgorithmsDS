"""
Time: O(n)
Space: O(1)
"""

def maxAbsoluteSum(nums: List[int]) -> int:

    maxSubarraySum = kadensMax(nums)
    minSubarraySum = kadensMin(nums)

    return max(abs(maxSubarraySum), abs(minSubarraySum))


def kadensMax(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    globalMax, localMax = -math.inf, -math.inf

    for num in nums:
        localMax = max(localMax + num, num)
        globalMax = max(globalMax, localMax)

    return globalMax


def kadensMin(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]


    globalMin, localMin = math.inf, math.inf

    for num in nums:
        localMin = min(localMin + num, num)
        globalMin = min(globalMin, localMin)

    return globalMin
