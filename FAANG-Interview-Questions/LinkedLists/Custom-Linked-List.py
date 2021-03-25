from random import randint

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    # __str__ called when the instance is printed 
    # output: [2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10]
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    # overriding standard __len__ method 
    # returns the number of nodes of linked list
    def __len__(self):
        c = 0
        current = self.head
        while current:
            c += 1
            current = current.next
        return c    
      
    # append operator
    def add(self,value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    # generates a linked list with random nodes
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
