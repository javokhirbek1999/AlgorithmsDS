# Activities:
#  Columns: 
#         1. Activity name
#         2. Activity start time
#         3. Activity end time
activities = [
				['A1',0,6],
				['A2',3,4],
				['A3',1,2],
				['A4',5,8],
				['A5',5,7],
				['A6',8,9]
				]

def maxActivities(activities):
	activities.sort(key=lambda x:x[2])
	
	most_optimals = []
	most_optimals.append(activities[0])

	for i in range(len(activities)-1):
		if most_optimals[-1][2]<=activities[i+1][1]:
			most_optimals.append(activities[i+1])
	
	return most_optimals
