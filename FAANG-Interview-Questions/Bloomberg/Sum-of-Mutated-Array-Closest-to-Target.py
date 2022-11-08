"""
Time: O(n log n)
Space: O(1)
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort(reverse=True)
        
        maxArr = max(arr)
        
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        
        return self.customRound(target/len(arr)) if arr else maxArr
    
    
    def customRound(self, n):
        return math.ceil(n) if n % 1 > 0.5 else math.floor(n)
