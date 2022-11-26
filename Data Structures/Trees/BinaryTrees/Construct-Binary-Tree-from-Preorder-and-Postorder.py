class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.preIndex = 0
        self.postIndex = 0
        
        return self.construct(preorder, postorder)
    
    def construct(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[self.preIndex])
        
        self.preIndex+=1
        
        if root.val != postorder[self.postIndex]:
            root.left = self.construct(preorder, postorder)
        if root.val != postorder[self.postIndex]:
            root.right = self.construct(preorder, postorder)
        
        self.postIndex += 1
        
        return root
