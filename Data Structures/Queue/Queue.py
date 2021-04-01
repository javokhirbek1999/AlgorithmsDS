class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next    

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return ' '.join(values)

    def isEmpty(self):
        return self.LinkedList.head is None

    def enqueue(self,value):
        node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            node.next = None
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Queue')
        else:
            return self.LinkedList.head.value

    def clear(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
