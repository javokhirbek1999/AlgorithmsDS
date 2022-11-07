"""
Time: O(n)
Space: O(n)
"""
from random import sample

class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums

    def reset(self) -> List[int]:
        return self.org

    def shuffle(self) -> List[int]:
        return sample(self.org, len(self.org))
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
