""""
DP - Memoization (Top-down)

N = # of items
M = knapsack weight

Time: O(N*M)
""""
def zeroOneKnapsack(values: List[int], weights: List[int],  knapsackWeight: int, n: int):
    
    dp = []

    for _ in range(n):
        row = []
        for _ in range(knapsackWeight+1):
            row.append(-1)
        dp.append(row)
    
    return solve(values, weights, knapsackWeight, n, dp)

def solve(values: List[int], weights: List[int], knapsackWeight: int, n: int, dp: List[List[int]]):

    if knapsackWeight == 0 or n == 0:
        return 0
    
    if dp[n-1][knapsackWeight] != -1:
        return dp[n-1][knapsackWeight]
    
    if weights[n-1] > knapsackWeight:
        dp[n-1][knapsackWeight] = solve(values, weights, knapsackWeight, n-1, dp)
    else:
        included = values[n-1] + solve(values, weights, knapsackWeight-weights[n-1], n-1, dp)
        excluded = solve(values, weights, knapsackWeight, n-1, dp)

        dp[n-1][knapsackWeight] = max(included, excluded)
    
    return dp[n-1][knapsackWeight]
