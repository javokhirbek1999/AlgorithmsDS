"""
Time: O(n)
Space: O(n)
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        
        if n != m:
            return False
        
        
        sCounter = Counter(s)
        tCounter = Counter(t)
        
        for char in t:
            if char not in sCounter or sCounter[char] != tCounter[char]:
                return False
        
        return True
        

"""
Time: O(n log n)
Space: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        
        if n != m:
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        
        sPtr, tPtr = 0, 0
        
        while sPtr < n and tPtr < m:
            
            if s[sPtr] != t[tPtr]:
                return False
            
            sPtr += 1
            tPtr += 1
        
        return True
