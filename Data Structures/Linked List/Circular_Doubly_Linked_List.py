class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            if current == self.tail.next:
                break
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            node.prev = node
            node.next = node
            self.head = node
            self.tail = node
            self.size += 1     
        else:
            node.prev = self.tail
            node.next = self.head
            self.head = node
            self.tail.next = self.head    
            self.size += 1     
             

    def append(self, value):
        node = Node(value)
        if self.head is None:
            node.prev = node
            node.next = node
            self.head = node
            self.tail = node
            self.size += 1     
        else:           
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head   
            self.size += 1     

    def insert(self, value, index):
        node = Node(value)
        if self.head is None:
            return Exception('List Does not exist')
        else:
            if index > self.size:
                raise Exception('Invalid index')
            if index == 0:
                self.prepend(value)
            elif index == self.size:
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
            raise Exception('List does not exist')
        else:
            current = self.head
            prev = self.head
            while current:
                if current.value == value:
                    if current == self.head:
                        self.head = self.head.next
                        self.head.prev = self.tail 
                        
                    elif current == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    else:
                        prev.next = current.next
                    self.size -= 1
                    return 
                else:
                    prev = current
                    current = current.next                      
     

    def remove_by_index(self, index):
        if self.head is None:
            raise Exception('List does not exist')
        elif index > self.size:
            raise Exception('Invalid index')    
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:    
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif index == self.size:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current = self.head
                ind = 0
                while ind < index-1:
                    current = current.next
                    ind += 1
                current.next = current.next.next
                current.next.prev = current
            self.size -= 1

    def traverse(self):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.next == self.head:
                    break
                else:
                    print(current.value)
                current = current.next     

    def contains(self, value):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:      
                if current.value == value:
                    return True
                if current.next == self.head:
                    break    
                current = current.next
            return False           

    def search(self, value):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            ind = 0
            while current:
                if current.value == value:
                    return ind
                if current.next == self.head:
                    break
                else:
                    current = current.next
                    ind += 1   

    def clear(self):
        if self.head is None:
            raise Exception('List does not exist')
        else:    
            self.head = None
            self.tail = None   
            self.size = 0    
