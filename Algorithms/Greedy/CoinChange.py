def coinChange(totalAmount, coins):
	n = totalAmount
	coins.sort()
	index = len(coins)-1
	min_coin_set = []
	while True:
		coinValue = coins[index]
		if n >= coinValue:
			min_coin_set.append(coinValue)
			n = n - coinValue

		if n < coinValue:
			index-=1

		if n==0:
			return min_coin_set
