n = int(input())
sub_solutions = [-1]*(n+1)

def cnt_derrangements(n):
	if sub_solutions[n] != -1:
		return sub_solutions[n]
	if n == 1:
		return 0
	if n == 2:
		return 1
	else:
		result = (n-1)*(cnt_derrangements(n-1)+cnt_derrangements(n-2))
		sub_solutions[n] = result
		return result
