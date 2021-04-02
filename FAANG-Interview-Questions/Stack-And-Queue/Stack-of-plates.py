class StackOfPlates:
    def __init__(self,capacity):
        self.items = []
        self.capacity = capacity

    def __str__(self):
        return str(self.items)

    def push(self,value):
        if len(self.items) and len(self.items[-1])<self.capacity:
            self.items[-1].append(value)
        else:
            self.items.append([value])

    def pop(self):
        if len(self.items)>0 and len(self.items[-1])==0:
            self.items.pop()
        elif len(self.items)==0:
            return -1
        else:
            self.items[-1].pop()

    def pop_at(self,index):
        if len(self.items[index])>0:
            self.items[index].pop()
        else:
            return -1
