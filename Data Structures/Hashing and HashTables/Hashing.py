class HashTable:
    def __init__(self,size):
        self.table = [None]*size
        self.size = size 
        self.count = 0   
    
    def __str__(self):
        return str(self.table)

    def hashing(self,word):
        multi = 1
        value = 0
        for i in word:
            value += multi * ord(i)
            multi += 1
        return value%len(self.table)

    # If slot is not empty, it does an open addressing
    # In the case of open addressing, it takes O(n) otherwise it takes O(1)
    def add(self,item,price):
        if self.count == self.size:
            return 'Table is full'
        else:
            if self.count/self.size>=0.7:
                temp = self.table
                self.table = [None]*(self.size*2)
                for i in range(len(temp)):
                    self.table[i] = temp[i]
            ind = self.hashing(item)
            if self.table[ind] is None:
                self.table[ind] = price
            else:
                while self.table[ind] is not None:
                    ind += 1
                    if self.table[ind] is None:
                        self.table[ind] = price
                        break
            self.count+=1
    
    # O(1) 
    def get(self,item):
        ind = self.hashing(item)
        if self.table[ind] is not None:
            return self.table[ind]
        else:
            return 'Item does not exist'
