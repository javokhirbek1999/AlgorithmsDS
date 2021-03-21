class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            else:
                node = node.next 
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1    
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1
    
    def insert(self, value, index):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.size-1:
                self.append(value)
            else:
                current = self.head
                ind = 0
                while ind < index - 1:
                    current = current.next
                    ind += 1
                next_node = current.next
                current.next = node
                node.next = next_node
                self.size += 1
    
    def remove(self, value):
        if self.head is None:
            return None
        else:
            current = self.head
            prev = self.head
            while current:
                if current.value == value:
                    if current == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        prev.next = current.next
                    self.size -= 1
                    return
                else:
                    prev = current
                    current = current.next 
    
    def remove_by_index(self, index):
        if self.head is None:
            return None
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                self.size -= 1
            elif index == self.size-1:
                current = self.head
                while current:
                    if current.next == self.tail:
                        break
                    else:
                        current = current.next
                self.tail = current
                self.tail.next = self.head
                self.size -= 1 
            else:
                current = self.head
                ind = 0
                while ind < index-1:
                    current = current.next
                    ind += 1
                next_node = current.next
                current.next = next_node.next
                self.size -= 1
    
    def traverse(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current:
                if current.next == self.head:
                    break
                else:
                    print(current.value)
                    current = current.next
    
    def search(self, value):
        if self.head is None:
            return None
        else:
            current = self.head
            while current:
                if current.next == self.head:
                    break
                else:
                    if current.value == value:
                        return True
                    else:
                        current = current.next 
            return False
    
    def clear(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.size = 0
