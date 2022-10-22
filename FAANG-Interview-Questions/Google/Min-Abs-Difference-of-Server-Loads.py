"""
Time: O(n * m)
Space: O(n * m)
"""
from typing import List


def solve(serverLoads: List[int]) -> int:

    memo = {}

    return topDownRec(serverLoads, 0, 0, 0, memo)
  
def topDownRec(serverLoads: List[int], current_index: int, sum1: int, sum2: int, memo: dict) -> int:

    if current_index == len(serverLoads):
        return abs(sum1-sum2)

    key = (current_index, sum1, sum2)

    if key in memo:
        return memo[key]
    
    part1 = topDownRec(serverLoads, current_index+1, sum1+serverLoads[current_index], sum2, memo)
    part2 = topDownRec(serverLoads, current_index+1, sum1, sum2+serverLoads[current_index], memo)

    memo[key] = min(part1, part2)

    return memo[key]


#############################################
"""
Time: O(n * m)
Space: O(n * m)
"""
def bottomUp(serverLoads: List[int]) -> int:

    totalLoad = sum(serverLoads)

    target = totalLoad//2

    n = len(serverLoads)

    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    
    
    for i in range(1, n+1):
        for j in range(target+1):
            if serverLoads[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(serverLoads[i-1] + dp[i-1][j-serverLoads[i-1]], dp[i-1][j])
    

    return totalLoad - 2 * dp[n][target]
