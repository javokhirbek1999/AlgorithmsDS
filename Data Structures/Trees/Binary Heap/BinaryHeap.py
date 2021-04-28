class Heap:
    def __init__(self,maxSize):
        self.heapList = (maxSize+1)*[None]
        self.heapSize = 0
        self.maxSize = maxSize
    
    def __str__(self):
        return str(self.heapList)
    
    def size(self,root):
        return root.heapSize
    
    def peek(self,root):
        if root.heapList[1] == None:
            return None
        else:
            return root.heapList[1]

    def levelOrderTraversal(self,root):
        if root.heapSize == 0:
            return
        else:
            for i in range(1,root.heapSize+1):
                print(root.heapList[i])
    
    def heapifyTreeInsert(self,root,index,heapType):
        parentIndex = index//2
        if index <= 1:
            return 
        if heapType == "Min":
            if root.heapList[index] < root.heapList[parentIndex]:
                temp = root.heapList[index]
                root.heapList[index] = root.heapList[parentIndex]
                root.heapList[parentIndex] = temp
            self.heapifyTreeInsert(root,parentIndex,heapType)
        elif heapType == "Max":
            if root.heapList[index] > root.heapList[parentIndex]:
                temp = root.heapList[index]
                root.heapList[index] = root.heapList[parentIndex]
                root.heapList[parentIndex] = temp
            self.heapifyTreeInsert(root,parentIndex,heapType)
    
    def insert(self,root,value,heapType):
        if root.heapSize == root.maxSize+1:
            return 'Binary Heap is full'
        root.heapList[root.heapSize+1] = value
        root.heapSize += 1
        self.heapifyTreeInsert(root,root.heapSize,heapType)
        return 'Inserted successfully'
    
    def heapifyTreeExtract(self,root,index,heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if leftIndex > root.heapSize:
            return
        elif root.heapSize == leftIndex:
            if heapType == "Min":
                if root.heapList[index] > root.heapList[leftIndex]:
                    temp = root.heapList[index]
                    root.heapList[index] = root.heapList[leftIndex]
                    root.heapList[leftIndex] = temp
                return
            elif heapType == "Max":
                if root.heapList[index] < root.heapList[leftIndex]:
                    temp = root.heapList[index]
                    root.heapList[index] = root.heapList[swapChild]
                    root.heapList[swapChild] = temp
                return
        else:
            if heapType == "Min":
                if root.heapList[leftIndex] < root.heapList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if root.heapList[index] > root.heapList[swapChild]:
                    temp = root.heapList[index]
                    root.heapList[index] = root.heapList[swapChild]
                    root.heapList[swapChild] = temp
            else:
                if root.heapList[leftIndex] > root.heapList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if root.heapList[index] < root.heapList[swapChild]:
                    temp = root.heapList[index]
                    root.heapList[index] = root.heapList[swapChild]
                    root.heapList[swapChild] = temp
            self.heapifyTreeExtract(root,swapChild,heapType)
            
    def extract(self,root,heapType):
        if root.heapSize == 0:
            return 
        else:
            extractedNode = root.heapList[1]
            root.heapList[1] = root.heapList[root.heapSize]
            root.heapList[root.heapSize] = None
            root.heapSize -= 1
            self.heapifyTreeExtract(root,1,heapType)
            return extractedNode

    def clear(self,root):
        root.binaryList.clear()
        root.heapSize = 0
