from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

       # 1.Depth-First-Search
    #   * Preorder Traversal
    #   * Inorder Traversal
    #   * Post order Traversal
    # 2. Bread first search
    #   * Level order traversal

    """""
                        N1
                       /  \ 
                      /    \ 
                     /      \ 
                    N2      N3
                   / \      / \ 
                  /   \    /   \ 
                 /     \  N6   N7
                N4     N5        
               / \ 
              /   \ 
             N8   N9

    1. Preorder Traversal: [Root -> Left sub-tree -> Right sub-tree]
       Postorder: N1 -> N2 -> N4 -> N8 -> N9 -> N5 -> N3 -> N6 -> N7

    2. InOrder Traversal: [Left sub-tree -> Root -> Right sub-tree]
       InOrder: N8 -> N4 -> N9 -> N2 -> N5 -> N1 -> N6 -> N3 -> N7

    3. Postorder Traversal: [Left sub-tree -> Right sub-tree -> Root]
       Postorder: N8 -> N9 -> N4 -> N5 -> N2 -> N6 -> N7 -> N3 -> N1       

    4. LevelOrder Traversal: [Level 0 -> Level 1 -> Level 2 and so on]
       LevelOrder: N1 -> N2 -> N3 -> N4 -> N5 -> N6 -> N7 -> N8 -> N9  


    5. Inverting a Binary Tree:     Original:               Inverted:          
                                        N1                     N1
                                       /  \                   /  \ 
                                      /    \                 /    \               
                                     /      \               /      \ 
                                    N2      N3             N3       N2  
                                   / \      / \           / \       / \  
                                  /   \    /   \         /   \     /   \ 
                                 /     \  N6   N7       N7   N6   N5    N4     
                                N4     N5                               / \ 
                               / \                                     /   \   
                              /   \                                   N9   N8
                             N8   N9                   
                                                                                
    Original: N1 -> N2 -> N3 -> N4 -> N5 -> N6 -> N7 -> N8 -> N9                 
    Inverted: N1 -> N3 -> N2 -> N7 -> N6 -> N5 -> N4 -> N9 -> N8           
    """""
    def preOrderTraversal(self,root):
        if not root:
            return
        if root.value is not None:
            print(root.value)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right) 

    def inOrderTraversal(self,root):
        if not root:
            return 
        self.inOrderTraversal(root.left)
        if root.value is not None:
            print(root.value)  
        self.inOrderTraversal(root.right)
       
    def postOrderTraversal(self,root):
        if not root:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        if root:
            print(root.value, end=" ")    

    def levelOrderTraversal(self,root):
        if not root:
            return 
        
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)        

    # For large Binary Trees Inverting with preOrder Traversal 
    # may throw stack overflow because preOrder Traversal is rucursive 
    # For any recursive call, there is a huge potential 
    # for stack overflow if Tree is pretty large
    def invertTreePreOrder(self,root):
        if root:
            root.left,root.right = self.invertTreePreOrder(root.right), self.invertTreePreOrder(root.left)
        return root  

    # For all three cases of Inverting a Binary Tree costs O(n)
    # as we have to visit each node one by one
    # But in our last two cases, as we are using stack for the first case and
    # queue for the second case, we do not have to worry about the stack overflow anymore
    # Using Stack and Queue for inverting a binary would be robust solution  
    def invertTreeDFS(self,root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right = node.right,node.left
                stack.append(node.left)
                stack.append(node.right)
        return stack  

    def invertBFS(self,root):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left,node.right = node.right,node.left
                queue.append(node.left)
                queue.append(node.right)
        return root                   
