"""
n = # of coins
m = amount

Time: O(n*m)
Space: O(n*m)
"""

def coinChange(coins: List[int], amount: int) -> int:
        
        dp = {}
        
        res = self.solve(coins, amount, 0, dp)
        
        return -1 if res == math.inf else res
    
def solve(coins: List[int], amount: int, index: int, dp: dict) -> int:

    if amount == 0:
        return 0

    if index == len(coins) or amount < 0:
        return math.inf

    key = (amount, index)

    if key in dp:
        return dp[key]

    if coins[index] > amount:
        dp[key] = self.solve(coins, amount, index+1, dp)
    else:
        dp[key] = min(1 + self.solve(coins, amount-coins[index], index, dp), self.solve(coins, amount, index+1, dp))

    return dp[key]
        
