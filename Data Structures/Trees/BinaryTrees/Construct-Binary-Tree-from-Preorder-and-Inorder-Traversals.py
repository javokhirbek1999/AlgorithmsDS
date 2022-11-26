class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder or not postorder:
            return 
        
        current = postorder.pop()
        
        root = TreeNode(current)
        
        index = 0
        if current in inorder:
            index = inorder.index(current)
        
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:])
        
        return root
