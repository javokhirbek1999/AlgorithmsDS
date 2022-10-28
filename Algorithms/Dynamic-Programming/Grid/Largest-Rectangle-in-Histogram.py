class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        stack = []
        left = []
        
        ptr = 0
        
        while ptr < n:
            
            while stack and heights[stack[-1]] >= heights[ptr]:
                stack.pop()
            
            if not stack:
                left.append(0)
            else:
                left.append(stack[-1]+1)
                
            stack.append(ptr)
            
            ptr += 1
        
        
        while stack:
            stack.pop()
        
        
        ptr -=1 
        
        right = []
        
        while ptr > -1:
            
            while stack and heights[stack[-1]] >= heights[ptr]:
                stack.pop()
            
            if not stack:
                right.append(n-1)
            else:
                right.append(stack[-1]-1)
            
            stack.append(ptr)
            
            ptr -= 1
        
        
        right.reverse()
        
        maxArea = 0
        
        for i in range(n):
            
            currentArea = (right[i]-left[i]+1) * heights[i]
            
            maxArea = max(maxArea, currentArea)
        
        return maxArea
            
        
"""
[2,1,5,6,2,3]
 0 1 2 3 4 5
   |
   
ls = [1,4,5] <= pop while top stack is greater than current
lt = [0,0,2,3,2,5] <= if stack is empty then append 0 else top of stack + 1


rs = [1,0] <= pop while current at top stack is greater than current
rt = [5,5,3,3,5,0] <= if stack is empty then append n-1 else top of stack - 1

rt = [0,5,3,3,5,5]


ls = [1,4,5]
lt = [0,0,2,3,2,5]


rs = [1,2]
rt = [5,5,3,3,5,0]

lt = [0,0,2,3,2,5]
rt = [0,5,3,3,5,5]
rs = [2,6,10,6,8,3]

"""
