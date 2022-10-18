"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        x = str(x)
        
        pt1, pt2 = 0, len(x)-1
        
        while pt1 < pt2:
            if x[pt1] != x[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
            
        return True
