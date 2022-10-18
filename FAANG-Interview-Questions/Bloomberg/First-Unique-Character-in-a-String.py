"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 1:
            return 0
        
        charFreq = {char:[0,math.inf] for char in "abcdefghijklmnopqrstuvwxyz"}
        
        curr = 1
        for char in s:
            charFreq[char][0] += 1
            
            if charFreq[char][1] == math.inf:
                charFreq[char][1] = curr
                curr += 1
        
        
        _min = math.inf
        ind = -1
        for index in range(len(s)):
            if charFreq[s[index]][0] == 1:
                if charFreq[s[index]][1] < _min:
                    _min = charFreq[s[index]][1]
                    ind = index
                
        return ind
    


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
