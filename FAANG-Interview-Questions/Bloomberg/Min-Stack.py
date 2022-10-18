"""
Time: O(1)
Space: O(n)
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.size = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        
        self.size += 1
        

    def pop(self) -> None:
        if self.size > 0:
            self.stack.pop()
            self.minStack.pop()
            self.size -= 1
        

    def top(self) -> int:
        if self.size > 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.size > 0:
            return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
