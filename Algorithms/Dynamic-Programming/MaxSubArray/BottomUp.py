class MaxSubArrayBottomUp:
    def __init__(self, prices):
        self.prices = prices
        self.sub_solutions = [None] * len(prices)
        for i in range(len(self.prices)):
            if i == 0:
                self.sub_solutions[i] = self.prices[0]
            else:
                self.sub_solutions[i] = max(self.prices[i], self.sub_solutions[i-1]+self.prices[i])

    def max_sub_array(self):
        max_value = 0
        for j in range(len(self.prices)):
            max_value  = max(max_value, self.sub_solutions[j])
        return max_value
