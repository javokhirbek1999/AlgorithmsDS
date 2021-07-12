def numberOfPaths(arr,row,col,cost):
	if cost < 0:
		return 0
	elif row == 0 and col == 0:
		if arr[row][col] - cost == 0:
			return 1
		else:
			return 0
	elif row == 0:
		return numberOfPaths(arr,0,col-1,cost-arr[row][col])
	elif col == 0:
		return numberOfPaths(arr,row-1,0,cost-arr[row][col])
	else:
		op1 = numberOfPaths(arr,row-1,col,cost-arr[row][col])
		op2 = numberOfPaths(arr,row,col-1,cost-arr[row][col])
		return op1+op2
