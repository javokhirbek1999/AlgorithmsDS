class AircraftSpacingBottomUp:
	def __init__(self,passengers):
		self.passengers = passengers
		self.sub_solutions = [-1]*len(passengers)
		for i in range(len(passengers)-1,-1,-1):
			choosing_first = self.passengers[i] + (self.sub_solutions[i+2] if i + 2 < len(self.sub_solutions) else 0)
			skip_first = self.sub_solutions[i+1] if i+1 < len(self.sub_solutions) else 0
			self.sub_solutions[i] = max(choosing_first, skip_first)
	
	def max_passengers(self, i):
		return self.sub_solutions[0]
