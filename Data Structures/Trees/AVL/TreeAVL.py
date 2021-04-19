class AVLNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def preOrderTraversal(self,root):
        if root is None:
            return None
        print(root.value)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self,root):
        if root is None:
            return None
        self.inOrderTraversal(root.left)
        print(root.value)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if root is None:
            return None
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)

    def levelOrderTraversal(self,root):
        if root is None:
            return None
        else:
            queue = [root]
            while queue:
                node = queue.pop(0)
                print(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def search(self,root,value):
        if root is None:
            return None
        else:
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node.value == value:
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return False

    def getHeight(self,root):
        if root is None:
            return 0
        else:    
            return root.height

    def getBalance(self,root):
        if root is None:
            return None
        return self.getHeight(root.left)-self.getHeight(root.right)

    def rotateRight(self,disbalancedNode):
        newRoot = disbalancedNode.left
        disbalancedNode.left = disbalancedNode.left.right
        newRoot.right = disbalancedNode

        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.left),self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))

        return newRoot

    def rotateLeft(self,disbalancedNode):
        newRoot = disbalancedNode.right
        disbalancedNode.right = disbalancedNode.right.left
        newRoot.left = disbalancedNode

        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.left),self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))

        return newRoot

    def insert(self,root,value):
        if root is None:
            return AVLNode(value)
        
        elif value<root.value:
            root.left =  self.insert(root.left,value)  
        else:
            root.right = self.insert(root.right,value)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and value < root.left.value:
            return self.rotateRight(root)
            
        if balance > 1 and value > root.left.value:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and value > root.right.value:
            return self.rotateLeft(root)

        if balance < -1 and value < root.right.value:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root  

    def node_with_parent(self,root,value):
        parent = None
        current = root
        if current is None:
            return (parent,current)
        while current:
            if current.value == value:
                return (parent,current)
            elif current.value > value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right                
        return (parent,current)

    def remove_node(self,root,value):
        parent,node = self.node_with_parent(root,value)

        children_count = 0
        if parent is None and node is None:
            children_count = 0
        elif node.left and node.right:
            children_count = 2
        else:
            children_count = 1

        if children_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None 

        elif children_count == 1:
            next_node = None
            if parent.left is node:
                next_node = node.left
            else:
                next_node = node.right

            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                root = next_node

        else:
            leftmost_par = node
            leftmost = node.right
            while leftmost.left:
                leftmost_par = leftmost
                leftmost = leftmost.left
            node.value = leftmost.value

            if leftmost_par.left is leftmost:
                leftmost_par.left = leftmost.right
            else:
                leftmost_par.right = leftmost.right

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left)>=0:
            return self.rotateRight(root)

        if balance <-1 and self.getBalance(root.right)>=0:
            return self.rotateLeft(root)
        
        if balance > 1 and self.getBalance(root.left)< 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance <- 1 and self.getBalance(root.right)>0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        
        return root

    def clear(self,root):
        root.value = None
        root.left = None
        root.right = None
