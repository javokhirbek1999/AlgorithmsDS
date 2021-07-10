# You’re going to Europe, and you have seven days to see everything
# you can. You assign a point value to each item (how much you want to see it) 
# and estimate how long it takes. How can you maximize the
# point total (seeing all the things you really want to see) during your
# stay? Come up with a greedy strategy. Will that give you the optimal
# solution?

def travelToEurope(cities, totalDays):
	total_days = totalDays
	cities.sort(key=lambda x:x[1], reverse=True)
	cities_to_visit = []

	for i in cities:
		if totalDays>=i[-1]:
			cities_to_visit.append(i[0])
			totalDays-=i[-1]

	return cities_to_visit
