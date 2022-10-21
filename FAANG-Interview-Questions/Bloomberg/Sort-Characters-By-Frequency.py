"""
Time: O(n log n)
Space: O(n)
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        charFreq = Counter(s)
        
        sortedCharsByFreq = sorted(charFreq.items(), key=lambda x:x[1], reverse=True)
        
        return "".join([char * charFreq[char] for char, _ in sortedCharsByFreq])
        
