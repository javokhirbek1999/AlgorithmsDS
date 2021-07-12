def findMinCostToReachLastCell(arr, row, col):
	if row == -1 or col == -1:
		return float('inf')
	elif row == 0 or col == 0:
		return arr[0][0]
	else:
		op1 = findMinCost(arr, row-1, col)
		op2 = findMinCost(arr, row, col-1)
		return arr[row][col] + min(op1,op2)
