class BST:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def recursiveInsert(self,root,value):
        if root is None:
            return None
        elif value <= root.value:
            if root.left is None:
                root.left = BST(value)
            else:
                self.recursiveInsert(root.left,value)
        else:
            if root.right is None:
                root.right = BST(value)
            else:
                self.recursiveInsert(root.right,value)   

    def iterativeInsert(self,root,val):
        if root is None:
            root = BST(val)
        else:
            current = root
            parent = None
            while True:
                parent = current
                if val <= current.value:
                    current = current.left
                    if current is None:
                        parent.left = BST(val)
                        return     
                else:
                    current = current.right
                    if current is None:
                        parent.right = BST(val)
                        return
    # Delete Node:
    # 1.No Children
    # 2.One Child
    # 3.Two Children
    # Algorithm:
    #   1.Get the node by searching with its parent and return them
    #   2.Get the children count of the node
    #   3.Remove nodes according to the number of children
    #       1. No Children: if children count is 0:
    #           * Update the parent node left or right pointer to None 
    #       2. One Child: if children count is 1:
    #           * Get the next node of the node by checking if that one child is nodes left or right child        
    #           * Check if parent does exist and if it does, update the parent left or right pointer to the next node of node else update root if parent does not exist 
    #       3. Two Children: if children count is 2:    
    #           * Set the node as parent of leftmost node
    #           * Set the right child of node as leftmost node
    #           * Keep traversing till the leftmost node is the last node:
    #               1. Parent of leftmost node to leftmost node
    #               2. Leftmost node to the left of child of leftmost node
    #           * Once the traversal finished, update the node value with the leftmost node value
    #           * check if leftmost node is the rigth or left child of parent leftmost child 
    #           * In either cases, update the parent of leftmost node pointer to the right child of leftmost node so the last node will be removed

    def node_with_parent(self,root,value):
        parent = None
        current = root
        if current is None:
            return (parent,current)
        while True:
            if current.value == value:
                return (parent,current)
            elif current.value > value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return (parent,current)

    def remove(self,root,value):
        parent,node = self.node_with_parent(root,value)

        children_count = 0

        if parent is None and node is None:
            return False
        elif node.left and node.right:
            children_count = 2
        elif node.left is None and node.right is None:
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None

        elif children_count == 1:
            next_node = None
            if node.left:
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
            leftmost_parent = node
            leftmost = node.right
            while leftmost.left:
                leftmost_parent = leftmost
                leftmost = leftmost.left
            node.value = leftmost.value

            if leftmost_parent.left is leftmost:
                leftmost_parent.left = leftmost.right
            else:
                leftmost_parent.right = leftmost.right   

    def levelOrderTraversal(self,root):
        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                print(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def preOrderTraversal(self,root):
        if not root:
            return root
        print(root.value)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)     

    def inOrderTraversal(self,root):
        if not root:
            return root
        self.inOrderTraversal(root.left)
        print(root.value)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if not root:
            return root
        self.postOrderTraversal(self,root.left)
        self.postOrderTraversal(self,root.right)
        print(root.value)                               

    def clear(self,root):
        self.root = None
        self.left = None
        self.right = None    
