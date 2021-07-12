def lps(s,startIndex,endIndex):
	if startIndex > endIndex:
		return 0
	elif startIndex == endIndex:
		return 1 
	elif s[startIndex] == s[endIndex]:
		return 2 + lps(s,startIndex+1,endIndex-1)
	else:
		op1 = lps(s,startIndex,endIndex-1)
		op2 = lps(s,startIndex+1,endIndex)
		return max(op1,op2)
