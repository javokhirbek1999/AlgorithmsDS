"""
Time: O(n)
Space: O(n)
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        charFreq = Counter(s)
        
        for index in range(len(s)):
            if charFreq[s[index]] == 1:
                return index
        
        return -1
