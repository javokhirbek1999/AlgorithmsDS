"""
Time: O(n log max(bloomDay))
Space: O(1)
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        
        if m * k > n:
            return -1
        
        low, high = 1, max(bloomDay)
        
        while low < high:
            day = low + (high-low) // 2
            
            if self.notPossible(day, bloomDay, m, k):
                low = day + 1
            else:
                high = day
        
        return low
        
    
    def notPossible(self, day: int, bloomDays: List[int], m: int, k: int):
        
        bouquets = 0
        prev_open = 0
        
        for d in bloomDays:
            if d <= day:
                prev_open += 1
            else:
                bouquets += prev_open//k
                prev_open = 0
        
        bouquets += prev_open//k
        
        return bouquets < m
        
