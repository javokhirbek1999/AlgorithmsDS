"""
Time: O(n * m)
Space: O(m)
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        heights = [0] * m
        
        globalMaxArea = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            globalMaxArea = max(globalMaxArea, self.lrh(heights))
        
        
        return globalMaxArea
    
    def lrh(self, heights: List[int]):
        
        m = len(heights)
        
        stack = []
        
        left = []
        right = []
        
        ptr = 0
        
        
        while ptr < m:
            
            while stack and heights[stack[-1]] >= heights[ptr]:
                stack.pop()
            
            
            if not stack:
                left.append(0)
            else:
                left.append(stack[-1] + 1)
            
            stack.append(ptr)
            ptr += 1
        
        
        while stack:
            stack.pop()
        
        ptr -= 1
        
        while ptr > -1:
            
            while stack and heights[stack[-1]] >= heights[ptr]:
                stack.pop()
            
            
            if not stack:
                right.append(m-1)
            else:
                right.append(stack[-1]-1)
            
            stack.append(ptr)
            ptr -= 1
        
        
        maxArea = 0
        
        right.reverse()
        
        
        for i in range(m):
            currentArea = (right[i]-left[i] + 1) * heights[i]
            
            maxArea = max(maxArea, currentArea)
        
        return maxArea
    
