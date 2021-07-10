# Algorithm 
# Weight, value, ratio (value/weight)
# 
# 1. Sort items by their ratio in descending order (from highest ratio to lowest ratio)
# 2. Keep track of used capacity and total value
# 3. Handle the used capacity by comparing in advance
# 4. If adding additional weight does not exceed the capacity, then add weight to used capacity and total value
# 5. If adding additional weight does exceed the capacity, then check how much unused capacity is left (usually check the the weight of the last item)
# 6. Multiply the unused capacity by the item ratio to calculate the remaining value
# 7. Then update the used weight and total value
# 8. Handle the infinite loop by checking whether the used capacity has reached the total capacity

class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value
		self.ratio = value/weight


def knapsack(items, capacity):
	items.sort(key=lambda x:x.ratio, reverse=True)
	usedCapacity = 0
	totalValue = 0
	for i in items:
		if usedCapacity+i.weight < capacity:
			usedCapacity += i.weight
			totalValue += i.value
		else:
			unusedWeight = capacity - usedCapacity
			value = i.ratio * unusedWeight
			usedCapacity += unusedWeight
			totalValue += value

		if usedCapacity == capacity:
			break
	return totalValue
