class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

def zeroKnapsack(items, capacity, currentIndex):
	if capacity <= 0 or currentIndex < 0 or currentIndex>=len(items):
		return 0
	elif items[currentIndex].weight <= capacity:
		profit1 = items[currentIndex].profit + zeroKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
		profit2 = zeroKnapsack(items, capacity, currentIndex+1)
		return max(profit1, profit2)
	else:
		return 0
