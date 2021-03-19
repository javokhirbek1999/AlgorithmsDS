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

    # Creates Circular Singly Linked List
    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        self.size += 1   

    def prepend(self, value):
        if self.head is None:
            return None
        else:    
            node = Node(value)
            node.next = self.head
            self.head = node
            self.tail.next = self.head 
            self.size += 1

    def append(self, value):
        if self.head is None:
            return None
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.size += 1

    def insert(self, value, index):
        new_node = Node(value)
        if self.head is None:
            return None
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.size-1:
                self.append(value)
            else:
                node = self.head
                ind = 0
                while ind < index - 1:
                    node = node.next
                    ind += 1
                next_node = node.next
                node.next = new_node
                new_node.next = next_node 

    def remove(self, value):
        if self.head is None:
            return None
        else:
            current = self.head
            prev = self.head
        
            while current:
                if current.value == value:
                    if current == self.head:
                        self.head = self.head.next
                        self.tail.next = self.head
                    else:
                        prev.next = current.next
                    self.size -= 1
                    return 
                prev = current
                current = current.next
    
    def remove_by_index(self, index):
        if self.head is None:
            return None
        else:
            if index == 0:
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
                while ind < index - 1:
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
