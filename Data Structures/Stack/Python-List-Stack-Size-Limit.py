class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values) 

    def isEmpty(self):
        return len(self.list)==0

    def isFull(self):
        return len(self.list)==self.maxSize

    def push(self,value):
        if self.isFull():
            raise Exception('Stack if full')
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self.list[-1]

    def clear(self):
        if self.isEmpty():
            raise Exception('Stack is empty')                        
        else:
            self.list = []
