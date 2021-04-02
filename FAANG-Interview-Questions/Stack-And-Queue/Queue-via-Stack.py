class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def push(self,value):
        self.items.append(value)

    def pop(self):
        if len(self.items)==0:
            return -1
        else:
            return self.items.pop()

class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self,value):
        self.inStack.push(value)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        popped_item = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return popped_item    
