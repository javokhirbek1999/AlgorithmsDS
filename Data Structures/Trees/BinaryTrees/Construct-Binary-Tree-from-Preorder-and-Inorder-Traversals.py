class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder: 
            return 
        
        current = preorder.pop(0)
        
        root = TreeNode(current)
        
        index = inorder.index(current)
        
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        
        return root
