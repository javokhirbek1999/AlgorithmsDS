class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.next = None
            self.tail.next = node
            self.tail = node
            self.size += 1
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def remove(self, value):
        if self.head is None:
            return None
        else:
            current = self.head
            prev = self.head
            while current:
                if current.value == value:
                    if current == self.head:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    self.size -= 1
                    return 
                prev = current
                current = current.next
    
    def remove_by_index(self, index):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                ind = 0
                while ind < index-1:
                    current = current.next
                    ind += 1
                next_node = current.next
                current.next = next_node.next 
                
    
    def contains(self, value):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False  

    def search(self, value):
        if self.head is None:
            raise Exception('List does not exist')
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
            raise Exception('List does not exist')
        else:
            self.head = None
            self.tail = None
            self.size = 0
    
    def traverse(self):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next
