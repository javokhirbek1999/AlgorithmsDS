"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        res = [""]
        
        s = s.upper()
        
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char != '-':
                if len(res[-1]) < k:
                    res[-1] = char + res[-1]
                else:
                    res.append(char)
        
        return "-".join(reversed(res))
