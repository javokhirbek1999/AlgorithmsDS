# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# First solution - Divide and Conquer Approach ( NOT EFFICIENT !!!!!!!! )
def houseRobber(houses, currentIndex):
	if currentIndex >= len(houses):
		return 0
	else:
		stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
		skipFirstHouse = houseRobber(houses, currentIndex+1)
		return max(stealFirstHouse,skipFirstHouse)

 # Second solution - DP ( More Efficient :) )
def houseRobber(houses):
	if len(houses)==0:
		return 0

	if len(houses)==1:
		return houses[0]

	dp = []
	dp.append(houses[0])
	dp.append(max(houses[0],houses[1]))

	for i in range(2,len(houses)):
		dp.append(max(dp[i-2]+houses[i], dp[i-1]))

	return dp[-1]
