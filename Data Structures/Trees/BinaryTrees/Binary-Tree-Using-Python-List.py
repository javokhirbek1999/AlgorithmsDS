class BinaryTree:
    def __init__(self, maxSize):
        self.list = maxSize*[None]
        self.lastUsedIndex = 0
        self.maxSize = maxSize

    def __str__(self):
        return str([str(node) for node in self.list])    
    
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            raise Exception("Binary Tree is full")
        self.list[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "Value inserted successfully"     

    def contains(self,value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return True
        return False       

    def preOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        print(self.list[index])    
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)    

    def inOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.inOrderTraversal(2*index)
        print(self.list[index])
        self.inOrderTraversal(2*index+1)     

    def postOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.list[index])   

    def levelOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        for i in self.list:
            if i: 
                print(i)  

    def removeNode(self,value):
        if self.lastUsedIndex == 0:
            raise Exception("Nothing to delete, empty tree")
        for i in range(1,self.lastUsedIndex+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex] = None                                        

    def clear(self):
        self.list = None
