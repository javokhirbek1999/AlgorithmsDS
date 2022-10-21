"""
Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        
        leftSubstring = defaultdict(int)
        rightSubstring = defaultdict(int)
        
        for char in s:
            rightSubstring[char] += 1
            
            
        leftSize, rightSize = len(leftSubstring.values()), len(rightSubstring.values())
        
        
        c = 0
        
        for index in range(len(s)):

            if leftSize == rightSize:
                c += 1
            
            current = s[index]
            
            rightSubstring[current] -= 1
            
            if rightSubstring[current] == 0:
                rightSize -= 1
            
            if current not in leftSubstring:
                leftSize += 1
                
            leftSubstring[current] += 1
        
        return c
            
