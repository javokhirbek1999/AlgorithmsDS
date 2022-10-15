"""
Time: O(n)
Space: O(1)
"""

def maxSubarraySumCircular(nums: List[int]) -> int:

    totalSum = sum(nums)
    maxSubSum = self.kadensMax(nums)
    minSubSum = self.kadensMin(nums)

    if maxSubSum > 0:
        return max(maxSubSum, totalSum - minSubSum)
    return maxSubSum


def kadensMax(nums: List[int]) -> int:

    if len(nums) == 0:
        return nums[0]


    globalMax, localMax = -math.inf, -math.inf

    for num in nums:
        localMax = max(localMax + num, num)
        globalMax = max(globalMax, localMax)

    return globalMax


def kadensMin(nums: List[int]) -> int:

    if len(nums) == 0:
        return nums[0]

    globalMin, localMin = math.inf, math.inf

    for num in nums:
        localMin = min(localMin + num, num)
        globalMin = min(globalMin, localMin)

    return globalMin
