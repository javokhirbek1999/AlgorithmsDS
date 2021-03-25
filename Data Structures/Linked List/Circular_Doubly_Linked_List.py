class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
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
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.head.prev = self.tail
            self.tail.next = self.head 
        self.size += 1
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1
    
    def insert(self,value,index):
        node = Node(value)
        if self.head is None:
            raise Exception('List does not exist')
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.size-1 or index==-1:
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
    
    def remove(self,value):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.value == value:
                    if current == self.head:
                        self.head = self.head.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                    elif current == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    self.size -= 1
                    return
                current = current.next        

    def remove_by_index(self,index):
        if self.head is None:
            raise Exception('List does not exist')
        if index > self.size:
            raise Exception('Invalid Index')    
        else:
            if index == 0:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif index == self.size-1:
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
                self.size -=1 

    def search(self,value):
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

    def contains(self,value):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
                if current.next == self.head:
                    break
            return False       

    def traverse(self):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            current = self.head
            while current:
                if current.next == self.head:
                    break
                print(current.value)
                current = current.next  
              
            
    def clear(self):
        if self.head is None:
            raise Exception('List does not exist')
        else:
            self.head = None
            self.tail = None
            self.size = 0      
