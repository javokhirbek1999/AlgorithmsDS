class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
        else:
            node.prev = None
            node.next = self.head
            self.head = node
        self.size += 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def insert(self, value, index):
        node = Node(value)
        if self.head is None:
            if index == 0:
                self.prepend(value)
            else:
                return Exception('Invalid Index for an empty List')
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.size-1:
                self.append(value)
            else:
                current = self.head
                ind = 0
                while ind < index-1:
                    current = current.next
                    ind += 1
                node.next = current.next
                node.prev = current
                current.next = node
        self.size += 1

    def remove(self, value):
        if self.head is None:
            return Exception('List Does not exist')
        else:
            current = self.head
            while current:
                if current.value == value:
                    if current == self.head:
                        self.head = self.head.next
                        self.head.prev = None
                    elif current == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        current.prev.next = current.next
                    self.size -= 1
                    return     
                else:  
                    current = current.next

    def remove_by_index(self, index):
        if self.head is None:
            return Exception('List does not exist')
        else:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1
            elif index == self.size-1:
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -=1
            else:
                current = self.head
                ind = 0
                while ind < index-1:
                    current = current.next
                    ind += 1
                current.next = current.next.next 
                current.next.prev = current.prev
                self.size -= 1
    
    def traverse(self):
        if self.head is None:
            return Exception('List does not exist')
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next
    
    def contains(self, value):
        if self.head is None:
            return Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False  

    def search(self, value):
        if self.head is None:
            return Exception('Lis does not exist')
        else:
            current = self.head
            index = 0
            while current:
                if current.value == value:
                    return index
                else:
                    current = current.next
                    index += 1
            return -1        

    def clear(self):
        if self.head is None:
            return Exception('List does not exist')
        else:
            current = self.head
            while current:
                current.prev = None
                current = current.next
            self.head = None
            self.tail = None
            self.size = 0  
