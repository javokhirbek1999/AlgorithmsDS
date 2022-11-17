"""
Time: O(n)
Space: O(1)
"""
from collections import Counter

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        topCount = Counter(tops)
        bottomCount = Counter(bottoms)
        
        topMaxCount = 0
        topMax = 0
        
        bottomMaxCount = 0
        bottomMax = 0
        
        
        for num, count in topCount.items():
            if topMaxCount < count:
                topMaxCount = count
                topMax = num
        
        for num, count in bottomCount.items():
            if bottomMaxCount < count:
                bottomMaxCount = count
                bottomMax = num
        
        
        swaps = 0
        
        for i in range(len(tops)):
            if topMaxCount >= bottomMaxCount:
                if topMax not in [tops[i], bottoms[i]]:
                    return -1
                else:
                    if tops[i] != topMax:
                        swaps += 1
            else:
                if bottomMax not in [tops[i], bottoms[i]]:
                    return -1
                else:
                    if bottoms[i] != bottomMax:
                        swaps += 1
        
        return swaps
      
"""
Time: O(n)
Space: O(1)
"""

from collections import defaultdict


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)
        
        topCount = defaultdict(int)
        bottomCount = defaultdict(int)
        
        sameCount = defaultdict(int)
        
        
        for i in range(n):
            
            t, b = tops[i], bottoms[i]
            
            topCount[t] += 1
            bottomCount[b] += 1
            
            if t == b:
                sameCount[t] += 1
        
        
        for i in range(1,7):
            if topCount[i] + bottomCount[i] - sameCount[i] == n:
                return n - max(topCount[i], bottomCount[i])
        
        return -1
