class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        return self.top == -1

    def enqueue(self,value):
        if self.isFull():
            raise Exception('Queue is full')
        else:
            if self.top+1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement 

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            return self.items[self.start]

    def clear(self):
        self.items = self.maxSize*[None]
        self.start = -1
        self.top = -1
