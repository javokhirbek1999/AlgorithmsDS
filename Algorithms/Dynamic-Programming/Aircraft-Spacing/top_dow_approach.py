# Top-down approach 
# Memoization
class AircraftSpacing:
	def __init__(self, passengers):
		self.passengers = passengers
		self.sub_solutions = [-1] * len(self.passengers)


	def max_passengers(self,i):
		if i >= len(self.passengers):
			return 0
		if self.sub_solutions[i] != -1:
			return self.sub_solutions[i]
		choose_first = self.passengers[i] + self.max_passengers(i+2)
		skip_first = self.max_passengers(i+1)
		max_pass = max(choose_first,skip_first)
		self.sub_solutions[i] = max_pass
		return max_pass
