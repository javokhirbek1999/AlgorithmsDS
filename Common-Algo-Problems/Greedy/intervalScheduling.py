def scheduleInterval(intervals):
	intervals.sort(key=lambda x:x[-1])
	possible_intervals = []
	possible_intervals.append(intervals[0])
	for i in range(1,len(intervals)):
		if possible_intervals[-1][-1]<=intervals[i][0]:
			possible_intervals.append(intervals[i])
	return possible_intervals

r1 = (0,3)
r2 = (1,3)
r3 = (0,5)
r4 = (3,6)
r5 = (4,7)
r6 = (3,9)
r7 = (5,10)
r8 = (8,10)

R = [r1,r2,r3,r4,r5,r6,r7,r8]
print(scheduleInterval(R))
