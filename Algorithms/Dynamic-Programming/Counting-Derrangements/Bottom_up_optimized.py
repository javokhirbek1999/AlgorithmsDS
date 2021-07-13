class CountDerrangementsRec:
	def __init__(self, set_size):
		self.set_size = set_size
		self.solution_n, solution_n_minus_1, solution_n_minus_2 = 0, 0, 0

		for n in range(1,set_size+1):
			if n == 1:
				self.solution_n = 0
			if n == 2:
				self.solution_n = 1
			else:
				self.solution_n = (n-1) * (solution_n_minus_1+solution_n_minus_2)
			solution_n_minus_2 = solution_n_minus_1
			solution_n_minus_1 = self.solution_n

	def count_derrangements_bottom_up(self):
		return self.solution_n
