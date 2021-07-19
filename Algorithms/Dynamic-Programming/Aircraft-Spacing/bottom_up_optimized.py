class AircraftSpacingBottomUpOptimized:
	def __init__(self,passengers):
		self.passengers = passengers

		self.at_i,self.at_i_1,self.at_i_2 = 0,0,0

		for i in range(len(passengers)-1,-1,-1):
			choosing_first = self.passengers[i] + self.at_i_2
			skip_first = self.at_i_1
			self.at_i = max(choosing_first, skip_first)
			self.at_i_1, self.at_i_2 = self.at_i, self.at_i_1

	def max_passengers(self):
		return self.at_i
