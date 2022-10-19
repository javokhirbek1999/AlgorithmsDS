"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        
        if n == 1:
            return False
        
        stack = []
        
        for curr in s:
            if not stack:
                stack.append(curr)
            else:
                if stack[-1] == '(' and curr == ')' or stack[-1] == '[' and curr == ']' or stack[-1] == '{' and curr == '}':
                    stack.pop()
                else:
                    stack.append(curr)
        
        return len(stack) == 0
