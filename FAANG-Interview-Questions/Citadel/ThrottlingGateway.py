"""
Time: O(n ^ 2)
Space: O(n)
"""
from collections import Counter
from typing import List


def throttlingGateway(n: int, requests: List[int]) -> int:

    reqStates = [(1,3), (10,20), (60,60)]
    reqCount = Counter(requests)
    uniqueValues = set()
    maxLength = max(requests)
    presum_values = [0] * (maxLength + 1)
    res = 0

    if not requests:
        return 0
    

    for i in range(1, maxLength+1):
        presum_values[i] = presum_values[i-1] + reqCount[i]
    
    print(presum_values)
    for timeFrame, capacity in reqStates:

        windowValue = min(timeFrame, maxLength) # min(1, 12) => 1

        for i in range(maxLength - windowValue + 1): # 12 - 1 + 1 = 12 => [0,11]
            requestValue = presum_values[i + windowValue] - presum_values[i] # 4
            tempValue = max(0, requestValue - capacity) # max(0, 4-3) => 1

            for j in range(1, tempValue + 1): # [1, 2)
                uniqueValues.add(presum_values[i + windowValue] - j) # 4 - 1 = 3
    res = len(uniqueValues)

    return res

