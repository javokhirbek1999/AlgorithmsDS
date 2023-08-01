class MinStack:

    """
    Minimum Stack implementation
    """

    def __init__(self) -> None:
        self.stack = []
        self.min = [] 
    

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min or val<self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
    

    def pop(self) -> any:
        
        if not self.isEmpty():
            popped = self.stack.pop()
            self.min.pop()
            return popped


    def isEmpty(self) -> bool:
        return len(self.stack) > 0
    

    def getMin(self) -> any:
        return self.min[-1] if self.min else None

