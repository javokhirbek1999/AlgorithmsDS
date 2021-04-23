class BinaryHeap:
    def __init__(self,size):
        self.list = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size + 1
    
    def __str__(self):
        return str(self.list)

    def getSize(self):
        return self.heapSize
    
    def peek(self):
        return self.heapSize[1]

    def levelOrderTraversal(self,root):
        if not root:
            return None
        else:
            for i in range(1,self.heapSize+1):
                print(self.list[i])
    
    def heapifyTreeInsertion(self,root,index,heapType):
        parentIndex = index//2
        if index <= 1:
            return
        if heapType == "Min":
            if root.list[index] < root.list[parentIndex]:
                temp = root.list[index]
                root.list[index] = root.list[parentIndex]
                root.list[parentIndex] = temp
            self.heapifyTreeInsertion(root,parentIndex,heapType)
        else:
            if root.list[index] > root.list[parentIndex]:
                temp = root.list[index]
                root.list[index] = root.list[parentIndex]
                root.list[parentIndex] = temp
            self.heapifyTreeInsertion(root,parentIndex,heapType)
    
    def insert(self,root,value,heapType):
        if root.heapSize == root.maxSize:
            return "Heap is full"
        root.list[root.heapSize+1] = value
        root.heapSize += 1
        self.heapifyTreeInsertion(root,root.heapSize,heapType)
