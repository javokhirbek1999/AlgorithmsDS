class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        return len(self.items)==0
    
    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Empty Queue')
        else:
            self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Queue')
        else:
            return self.items[0]

    def clear(self):
        self.items = []
