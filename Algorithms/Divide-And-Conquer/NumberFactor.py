# Problem Statement:
# Given N, find the number of ways to express N as a sum of 1,3 and 4	
# 
# Example:
# - N = 4
# - Number of ways = 4
# - Explanation: There are 4 ways we can express N, {4}, {1,3}, {3,1}, {1,1,1,1}
#
# Algorithm:
# Divide and Conquer method comes handy for solving this problem
# This can be solved by dividing into sub-problems using recursion
# and finally summing the solutions for sub-problems together to get the final solution
#
#

def numberFactor(n):
	if n in [0,1,2]:
		return 1
	elif n == 3:
		return 2
	else:
		sub1 = numberFactor(n-1)
		sub2 = numberFactor(n-3)
		sub3 = numberFactor(n-4)
		return sub1+sub2+sub3
