class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        return self.LinkedList.head is None

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        else:
            node = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        else:
            return self.LinkedList.head.value            

    def clear(self):
        self.LinkedList.head = None    
